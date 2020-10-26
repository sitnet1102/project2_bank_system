import deposit
#import depositTest as deposit
import mySaving as savings
#import savingsTest as savings
from Utils.View import BankMainView as bmv
import myAdmin # as admin
import newAccount as New_account
import loginMain
from Utils.IOUtils import FileReader as fr
import myUser

class mainPrompt :  # Bank_main 에서 이름 변경함
    
    account = ""
    password = ""
    

    def __init__(self) :
        self.main()

    def getData(self, account) :
        userData = fr.read_one_users(account)
        result = ""
        if userData == False :
            return result
        else :
            id = account
            if id == "00000000000000" :
                # 관리자 
                admin = 0
                name = userData['name']
                pw = userData['pw']
                date = userData['sign_up_date']
                result = { 
                    'id' : id,
                    'name' : name,
                    'sign_up_date' : date,
                    'user_class' : admin,
                    'Deposits' : id,
                    'Savings' : 0
                }
                return result
            else :
                # 일반 사용자
                admin = 1
                name = userData['name']
                pw = userData['pw']
                date = userData['sign_up_date']
                depositAccount = userData['accounts'][0]
                savingsAccount = userData['accounts'][1]
                result = { 
                    'id' : id,
                    'name' : name,
                    'sign_up_date' : date,

                    'user_class' : admin,
                    'Deposits' : depositAccount,
                    'Savings' : savingsAccount
                }
                return result

    def wrongData(self) :
        bmv.wrong_data()

    def loginCheck(self, id, pw) :
        userData = fr.read_one_users(id)
        if userData['pw'] == pw :
            return True
        else : 
            return False

    def login(self) :
        bmv.account_input()
        self.account = input()
        # trim 해주는것 확인 
        bmv.password_input()
        self.password = input()
        
        loginmain = loginMain.Login_main()

        userCheck = self.getData(self.account)

        if userCheck == "" :
            self.wrongData()
        elif userCheck['user_class'] == 0:
            user = myUser.User(userCheck)
            admin =  myAdmin.Admin()
            if self.loginCheck(self.account, self.password) :
                admin.run()
            else :
                self.wrongData()
        else :
            # 아이디 비밀번호 확인 
            user = myUser.User(userCheck)
            if self.loginCheck(self.account, self.password) :
                loginmain.run(user)
            else :
                self.wrongData()
        '''
        #######################
        if self.account == "00000000000000" and self.password == "123" :
            #관리자로 연결 
            # "관리자 계좌번호" , "관리자 비밀번호"
            # 하드 코딩된 상태가 아닌 json에서 확인하는 형태로 변경할지 고민중 
            admin.run()

        #######################
        elif self.account == "1" and self.password == "1" :
            # json 파일에서 데이터 확인 후 연결 
            check = True
            if check :
                loginmain.run(self.account)  
            else : 
                pass
                #self.main()

        else :
            # 데이터 관리 
            pass
            #self.main() ## 수정 필요 
        '''

    
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
                na.run()
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


    