from Utils.View import NewAccountView as nav
import time
import mainPrompt
from dataType import NameData
from dataType import PasswordData
from random import random
from Utils.IOUtils import FileReader as fr
from Utils.IOUtils import FileWriter as fw

class New_account :
    __name = ""
    __password = ""
    __date = ""
    __account = ""
    def entry_confirm(self) :
        nav.entry_confirm()
        
        check = input()
        if check == "Y" :
            self.name_confirm()
        elif check == "N" :
            pass

    def name_confirm(self) :
        # check에 이름이 올바른 형식인지 확인 
        while True :
            nav.name_confirm()
            self.name = input()
            self.name = self.name.strip(' ')
            check = NameData.dataConfirm(self.name)
            if check :
                self.password_confirm()
                break
            else :
                self.wrong_name()

    def wrong_name(self) : 
        nav.wrong_name()
        self.press_anykey()

    def password_confirm(self) :
        # check에 비밀번호가 올바른 형식인지 확인
        while True :
            nav.password_confirm()
            self.password = input()
            check = PasswordData.dataConfirm(self.password)
            if check :
                self.info_confirm()
                break
            else :
                self.wrong_password()

    def wrong_password(self) :
        nav.wrong_password()
        self.press_anykey()

    def press_anykey(self) :
        nav.press_anykey()
        anykey = input()
        
    def info_confirm(self) :
        self.today() # 데이터 형식에 대한 클래스를 따로 정할지 고민중
        nav.info_confirm(self.name, self.date, self.password)
        check = input()
        if check == "Y" :
            self.join()
        else :
            self.cancel()

    def today(self) :   # 데이터 형식에 대한 클래스를 따로 정할지 고민중
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))

    def join(self) :
        self.account = self.give_account()
        num1 = int(self.account[:1]) + 5
        savingsA = str(num1) + self.account[1:]
        #print(self.account)
        #print(savingsA)
        nav.join(self.name, self.account)
        self.save_info(self.account, self.name, self.password, self.date, savingsA)
        self.press_anykey()

    def give_account(self) :
        # 계좌번호 생성기  
        # user.json에서 키값으로 확인하고 없는것 체크
        # random 
        # 계좌 생성기     
        while True :
            result = ""
            for i in range(14) :
                num = random()
                num = int(num * 10)
                if i == 0 :
                    num = num % 4 + 1
                    '''
                    if typeNum == 1 :   # 예금 계좌번호
                        num = num % 4 + 1
                    elif typeNum == 2 : # 적금 계좌번호
                        num = num % 5 + 5
                    '''
                num = str(num)
                result = result + num
            if fr.new_account_check(result) : 
                pass
            else :
                break
        return result

    def cancel(self) :
        nav.cancel()
        self.press_anykey()
    
    def save_info(self, account, name, pw, date, savingsA) :
        ## 데이터 json 파일에 저장 
        ## 컨트롤로 연결??? 
        #######################################################################
        # 계좌에 저장으로 연결 ???
        #######################################################################
        fw.make_user(account, name, pw, date, savingsA)
        fw.make_account(account, date, "Deposits")
        fw.make_account(savingsA, date, "Savings")

    def run(self) :
        self.entry_confirm()