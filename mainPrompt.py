import deposit
#import depositTest as deposit
import mySaving as savings
#import savingsTest as savings
from Utils.View import BankMainView as bmv
import myAdmin # as admin
import newAccount as New_account
import loginMain
from Utils.IOUtils import FileReader as fr
from Utils.IOUtils import FileMaker as fm
import myUser
from dataType import PasswordData
from dataType import BankAccountData

class mainPrompt :  # Bank_main 에서 이름 변경함
    
    __account = ""
    __password = ""
    

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
        self.account = self.account.strip(' ')
        if BankAccountData.dataConfirm(self.account) :
            self.account = BankAccountData.dataToBasicType(self.account)

        bmv.password_input()
        self.password = input()
        self.password = self.password.strip(' ')
        if PasswordData.dataConfirm(self.password) :
            self.password = PasswordData.dataToBasicType(self.password)
        

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
    def integrity_check(self) :
        
        # 무결성 검사 
        errorCheck = True   # 에러가 있으면 False로 변경

        # 홈 경로에 데이터 파일이 있는지 확인 
        # 없으면 경고문구 출력, 빈 데이터 파일 생성 
        # 있으면 다음 단계
        fm.make_users()
        fm.make_history()
        fm.make_accounts()


        # 데이터 파일 확인 
        # accounts.json, history.json, users.json
        # 예금, 적금 계좌번호 중복확인 
        # 이름, 비밀번호 중복 확인 
        # 문법 규칙 확인 
        ################## keys가 자동으로 중복을 처리해버리는 문제 
        ## json 자체에서 중복이 오류 처리됨
        users_data = fr.read_all_users()
        if len(set(users_data.keys())) == len(users_data.keys()) :
            pass
        else :
            errorCheck = False
    
        history_data = fr.read_all_transactions()
        if len(set(history_data.keys())) == len(history_data.keys()) :
            pass
        else :
            errorCheck = False
            
        savings_data = fr.read_all_accounts()
        if len(set(savings_data.keys())) == len(savings_data.keys()) :
            pass
        else :
            errorCheck = False

        deposits_data = fr.read_all_accounts_in_deposit()
        if len(set(deposits_data.keys())) == len(deposits_data.keys()) :
            pass
        else :
            errorCheck = False



        # 오류가 있으면 종료 
        
        
        if errorCheck :
            pass
        else :
            self.programExit()


    
    def main(self) :
        ## 무결성 검사 
        self.integrity_check()
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
        
    
    

    

    @classmethod
    def programExit(cls) :
        bmv.exit()
        # 시스템 종료 연결 
        # atexit()


    