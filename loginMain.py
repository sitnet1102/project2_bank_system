from Utils.View import LoginMainView as lmv
import deposit
# import depositTest as deposit
import mySaving as savings
# import savingsTest as savings
# import bank_main
import myUser
from Utils.IOUtils import FileReader as fr


class Login_main :
    account = ""
    name = ""
    date = ""
    savings_account = ""
    #u = myUser.User()

    def run(self, account) :
        self.name = "이름" ## json 파일에서 이름 가져오기 
        d = deposit.Deposit(u)
        s = savings.Saving(u)

        while True :
            lmv.login_main(self.name)
            choice = input()
            if choice == '1' :
                d.run()   # 인자값으로 계좌번호 넘겨주기?
            elif choice == '2' :
                s.run()   # 인자값으로 계좌번호 넘겨주기?
            elif choice == '3' :
                ## json에서 이름, 가입일, 적금 계좌번호 가져오기 
                self.date = "20200101" #### 수정필요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                self.savings_account = "56785675678901" ### 수정필요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                ## 적금이 없을 때의 예외처리 필요 
                lmv.my_info(self.name, self.date, self.account, self.savings_account)
                self.press_anykey()
            elif choice == '4' :
                lmv.logout()
                self.press_anykey()
                break
  
    def getData(self, account) :
        userData = fr.read_one_users(account)
        if userData :
            name = userData['name']
            pw = userData['pw']
            return 
            
    def press_anykey(self) :
        lmv.press_anykey()
        anykey = input()
        