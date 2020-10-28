from Utils.View import AdminView as av


class Admin:
    """ 관리자의 동작을 정의합니다 """

    def run(self):
        ''' admin 인스턴스의 로직을 정의합니다 '''

        while True:
            user_choice = av.menu()

            if user_choice == 1:
                # 사용자 정보 조회
                av.show_user_datas()
            elif user_choice == 2:
                # 거래 내역 조회
                av.show_transaction_datas()
            elif user_choice == 3:
                # 로그 아웃
                self.__user_obj = None
                return
            else:
                # 아무 키
                continue
