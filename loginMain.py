from Utils.View import LoginMainView as lmv
import deposit
# import depositTest as deposit
import mySaving as savings
# import savingsTest as savings
# import bank_main
import myUser


class Login_main :
    def run(self, user) :
        d = deposit.Deposit(user)
        s = savings.Saving(user)
        while True :
            lmv.login_main(user.name)
            choice = input()
            if choice == '1' :
                d.run()
                pass
            elif choice == '2' :
                s.run()
            elif choice == '3' :
                ## json에서 이름, 가입일, 적금 계좌번호 가져오기 
                #self.date = "20200101" #### 수정필요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                #self.savings_account = "56785675678901" ### 수정필요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!
                ## 적금이 없을 때의 예외처리 필요 
                lmv.my_info(user.name, user.date, user.deposits, user.savings)
                self.press_anykey()
            elif choice == '4' :
                lmv.logout()
                self.press_anykey()
                break
  
    
            
    def press_anykey(self) :
        lmv.press_anykey()
        anykey = input()
        