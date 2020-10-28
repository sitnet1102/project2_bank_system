from Utils.View import DepositView as dv

class Deposit:
    """ 적금 서비스의 동작을 정의합니다 """

    def __init__(self, user_obj):
        self.__user_obj = user_obj

    def run(self):
        """ Saving 인스턴스의 로직을 정의합니다 """

        while True:
            menu_choice = dv.menu()
                
            if menu_choice == 1:
                # 잔액 조회
                dv.show_deposit_balance(self.__user_obj)
            elif menu_choice == 2:
                # 내역 조회
                dv.show_deposit_history(self.__user_obj)
            elif menu_choice == 3:
                # 입금
                dv.put_money_in_deposit(self.__user_obj)
            elif menu_choice == 4:
                # 출금
                dv.withdraw_money_in_deposit(self.__user_obj)
            elif menu_choice == 5:
                # 이체
                dv.send_money(self.__user_obj)
            elif menu_choice == 6:
                # 뒤로가기
                return
            else:
                # 아무 키
                continue