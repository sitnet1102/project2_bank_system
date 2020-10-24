class User:
    """ 현재 시스템 사용자 객체 """

    def __init__(self, kwargs):
        '''사용자 정보를 딕셔너리 자료구조 kwargs로 받아 User 인스턴스 초기화'''

        self.__id = kwargs['id']
        self.__name = kwargs['name']

        # admin, general user
        if kwargs['user_class'] == 0 :# 0:admin, 1:general_user
            self.__admin = True
        else:
            self.__admin = False

        self.__deposits = kwargs['Deposits']
        self.__savings = kwargs['Savings']

    # getter
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def admin(self):
        return self.__admin

    @property
    def deposits(self):
        return self.__deposits

    @property
    def savings(self):
        return self.__savings