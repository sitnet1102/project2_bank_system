# import deposit
import depositTest as deposit
# import mySaving as savings
import savingsTest as savings
from Utils.View import BankMainView as bmv
import myAdmin # as admin
import newAccount as New_account
import loginMain

class mainPrompt :  # Bank_main 에서 이름 변경함
    
    account = ""
    password = ""
    

    def __init__(self) :
        self.main()

    def login(self) :
        bmv.account_input()
        self.account = input()
        # trim 해주는것 확인 
        bmv.password_input()
        self.password = input()
        admin =  myAdmin.Admin()
        loginmain = loginMain.Login_main()

        if self.account == "00000000000000" and self.password == "123" :
            #관리자로 연결 
            # "관리자 계좌번호" , "관리자 비밀번호"
            # 하드 코딩된 상태가 아닌 json에서 확인하는 형태로 변경할지 고민중 
            myAdmin.Admin.run(admin)
        elif self.account == "1" and self.password == "1" :
            # json 파일에서 데이터 확인 후 연결 
            check = True
            if check :
                loginMain.Login_main.run(loginmain, self.account) 
            else : 
                pass
                #self.main()

        else :
            # 데이터 관리 
            pass
            #self.main() ## 수정 필요 


    
    def main(self) :
        ## 무결성 검사 
        #integrity_check()
        na = New_account.New_account()

        
        while True :
            bmv.bank_main()
            choice = input()
            if choice == '1' :
                self.login()
            elif choice == '2' :
                New_account.New_account.run(na)
            elif choice == '3' :
                self.programExit()
                break
        
    """
    def integrity_check(self) :
        # ??????
        return ??? 
    """ 

    @classmethod
    def programExit(cls) :
        bmv.exit()
        # 시스템 종료 연결 
        # atexit()


    