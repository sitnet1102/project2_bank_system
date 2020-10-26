from Utils.View import SavingView as sv

class Saving:
    """ 적금 서비스의 동작을 정의합니다 """

    def __init__(self, user_obj):
        self.__user_obj = user_obj

    def run(self):
        """ Saving 인스턴스의 로직을 정의합니다 """

        while True:
            menu_choice = sv.menu()
                
            if menu_choice == 1:
                # 잔액 조회
                sv.show_saving_balance(self.__user_obj)
            elif menu_choice == 2:
                # 내역 조회
                sv.show_saving_history(self.__user_obj)
            elif menu_choice == 3:
                # 입금
                sv.put_money_in_saving(self.__user_obj)
            elif menu_choice == 4:
                # 해약
                sv.cancel_saving(self.__user_obj)
            elif menu_choice == 5:
                # 뒤로 가기
                return
            else:
                # 아무 키
                continue