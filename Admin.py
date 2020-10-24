from View import AdminView as av


class Admin:
    """ 관리자의 동작을 정의합니다 """

    __slots__ = ['__user_obj'] # 관리자 인스턴스의 속성을 user_obj로 제한합니다.

    def __init__(self, user_obj):
        self.__user_obj = user_obj

    def run(self):
        ''' admin 인스턴스의 로직을 정의합니다 '''

        while True:
            user_choice = av.menu()

            if user_choice == 1:
                # 사용자 정보 조회
                av.user_data(self.__user_obj)
            elif user_choice == 2:
                # 거래 내역 조회
                av.transcation_data(self.__user_obj)
            elif user_choice == 3:
                # 로그 아웃
                self.__user_obj = None
                return
            else:
                # 아무 키
                continue
