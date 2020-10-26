from Utils.View import NewAccountView as nav
import time
import mainPrompt

class New_account :
    name = ""
    password = ""
    date = ""
    account = ""

    #tmp = mainPrompt.mainPrompt()
    

    def entry_confirm(self) :
        nav.entry_confirm()
        
        check = input()
        if check == "Y" :
            self.name_confirm()
        elif check == "N" :
            #mainPrompt.mainPrompt.main(tmp)
            pass

    def name_confirm(self) :
        nav.name_confirm()
        self.name = input()
        check = True
        # check에 이름이 올바른 형식인지 확인 
        while True :
            if check :
                self.password_confirm()
                break
            else :
                self.wrong_name()

    def wrong_name(self) : 
        nav.wrong_name()
        self.press_anykey()
        self.name_confirm()

    def password_confirm(self) :
        nav.password_confirm()
        self.password = input()
        check = True
        # check에 비밀번호가 올바른 형식인지 확인
        while True :
            if check :
                self.info_confirm()
                break
            else :
                self.wrong_password()

    def wrong_password(self) :
        nav.wrong_password()
        self.press_anykey()
        self.password_confirm()

    def press_anykey(self) :
        nav.press_anykey()
        anykey = input()
        
    def info_confirm(self) :
        self.today() # 데이터 형식에 대한 클래스를 따로 정할지 고민중
        nav.info_confirm(self.name, self.date, self.password)
        check = input()
        if check == "Y" :
            self.join()
        elif check == "N" :
            self.cancel()

    def today(self) :   # 데이터 형식에 대한 클래스를 따로 정할지 고민중
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))

    def join(self) :
        self.account = self.give_account()
        nav.join(self.name, self.account)
        self.save_info(self.name, self.password, self.date, self.account)
        self.press_anykey()
        #mainPrompt.mainPrompt.main(tmp)

    def give_account(self) :
        # 계좌번호 생성기  
        tmp = "12341231234567"
        return tmp

    def cancel(self) :
        nav.cancel()
        self.press_anykey()
        #mainPrompt.mainPrompt.main(tmp)
    
    def save_info(self, name, password, date, account) :
        ## 데이터 json 파일에 저장 
        ## 컨트롤로 연결??? 
        print()

    def run(self) :
        self.entry_confirm()