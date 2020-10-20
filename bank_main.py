##
import deposit
import savings
import view
import admin


import time
# import 

## 클래스 명은 대문자 시작, 메소드 명은 소문자 시작 


class New_account :
    name = ""
    password = ""
    date = ""
    account = ""

    def run(self) :
        self.entry_confirm()

    def entry_confirm(self) :
        view.entry_confirm()
        check = input()
        if check == "Y" :
            self.name_confirm()
        elif check == "N" :
            main_self.main()

    def name_confirm(self) :
        view.name_confirm()
        self.name = input()
        check = True
        # check에 이름이 올바른 형식인지 확인 
        if check :
            self.password_confirm()
        else :
            self.wrong_name()

    def wrong_name(self) : 
        view.wrong_name()
        self.press_anykey()
        self.name_confirm()

    def password_confirm(self) :
        view.password_confirm()
        self.password = input()
        check = True
        # check에 비밀번호가 올바른 형식인지 확인 
        if check :
            self.info_confirm()
        else :
            self.wrong_password()

    def wrong_password(self) :
        view.wrong_password()
        self.press_anykey()
        self.password_confirm()

    def press_anykey(self) :
        view.press_anykey()
        anykey = input()
        
    def info_confirm(self) :
        self.today() # 데이터 형식에 대한 클래스를 따로 정할지 고민중
        view.info_confirm(self.name, self.date, self.password)
        check = input()
        if check == "Y" :
            self.join()
        elif check == "N" :
            self.cancel()

    def today(self) :   # 데이터 형식에 대한 클래스를 따로 정할지 고민중
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))

    def join(self) :
        self.account = self.give_account()
        view.join(self.name, self.account)
        self.save_info(self.name, self.password, self.date, self.account)
        main_self.main()

    def give_account(self) :
        # 계좌번호 생성기 
        tmp = "12341231234567"
        return tmp

    def cancel(self) :
        view.cancel()
        self.press_anykey()
        main_self.main()
    
    def save_info(self, name, password, date, account) :
        ## 데이터 json 파일에 저장 
        ## 컨트롤로 연결??? 
        print()













class Login_main :
    account = ""
    name = ""
    date = ""
    savings_account = ""
    def run(self, account) :
        #account = account
        self.name = "이름" ## json 파일에서 이름 가져오기 
        view.login_main(self.name)
        choice = input()
        if choice == '1' :
            deposit.run()   # 인자값으로 계좌번호 넘겨주기?
        elif choice == '2' :
            savings.run()   # 인자값으로 계좌번호 넘겨주기?
        elif choice == '3' :
            ## json에서 이름, 가입일, 적금 계좌번호 가져오기 
            self.date = "20200101" #### 수정필요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            self.savings_account = "56785675678901" ### 수정필요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ## 적금이 없을 때의 예외처리 필요 
            view.my_info(self.name, self.date, self.account, self.savings_account)
            self.press_anykey()
        elif choice == '4' :
            view.logout()
            main_self.main()
        else :
            self.run(self.account)

            
    def press_anykey(self) :
        view.press_anykey()
        anykey = input()
        self.run(self.account)














class Bank_main :
    
    account = ""
    password = ""

    def main(self) :
        ## 무결성 검사 
        #integrity_check()


        view.bank_main()
        choice = input()

        if choice == '1' :
            self.login()
        elif choice == '2' :
            new_account.run()
        elif choice == '3' :
            self.exit()
        else :
            self.main()
        
    """
    def integrity_check(self) :
        # ??????
        return ??? 
    """ 

    def exit(self) :
        view.exit()
        # 시스템 종료 연결 
        # atexit()

    def login(self) :
        view.account_input()
        self.account = input()
        # trim 해주는것 확인 
        view.password_input()
        self.password = input()

        if self.account == "00000000000000" and self.password == "123" :
            #관리자로 연결 
            # "관리자 계좌번호" , "관리자 비밀번호"
            # 하드 코딩된 상태가 아닌 json에서 확인하는 형태로 변경할지 고민중 
            admin.run()
        elif self.account == "1" and self.password == "1" :
            # json 파일에서 데이터 확인 후 연결 
            check = True
            if check :
                login_main.run(self.account) 
            else : 
                main_self.main()

        else :
            main_self.main() ## 수정 필요 




        

        



if __name__ == "__main__":
    
   


    ## try - finally - like this ????
    main_self = Bank_main()
    view = view.View()
    new_account = New_account()
    login_main = Login_main()
    admin = admin.Admin()
    deposit = deposit.Deposit()
    savings = savings.Savings()
    main_self.main()
    
