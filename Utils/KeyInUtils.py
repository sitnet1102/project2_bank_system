import re

class KeyIn :
    # ''' CLI 입력을 받아들입니다 '''
    
    @classmethod
    def remove_puctuation(cls, type_in, config):

        if config == 'integer':
            pattern = '[\D]'# 숫자가 아닌 모든것 제거

        elif config == 'date' : 
            pattern = '[./-]' # 허용된 특수문자만 제거

        elif config == 'character':
            pattern == '[^a-zA-Z]' # 문자가 아닌 것 제거
        
        elif config == 'general':
            pattern = '[\W]' # 숫자와 문자만 허용. 나머지 제거

        sub = re.sub(pattern,'',type_in)

        return sub

    @classmethod
    def has_only(cls, type_in, config):
        if config == 'integer':
            pattern = '[\D]'# 숫자가 아닌 모든것

        elif config == 'character':
            pattern = '[^a-zA-Z가-힣ㄱ-ㅎㅏ-ㅣ]' # 알파벳, 한글이 아닌 모든것

        p = re.compile(pattern)

        if p.search(type_in) is not None:
            # 이외의 것이 들어있으면
            return False
        return True

    @classmethod
    def is_date(cls, type_in):

        # 비정상
        # 허용된 특수문자만 제거했으므로, 모두 숫자가 아니면
        p = re.compile('[a-zA-Z]+')
        if p.search(type_in) is not None:
            return False
        # 6자리거나 8자리가 아니면
        if len(type_in) != 6 and len(type_in) != 8:
            return False
        # 6자리일때 2,3번째가 13이상일 경우, 8자리일때 4,5번째가 13이상일 경우
        if len(type_in) == 6:
            if int(type_in[2:4]) > 12 or int(type_in[4:6]) > 31:
                return False

        if len(type_in) == 8:
            if int(type_in[4:6]) > 12 or int(type_in[6:8]) > 31:
                return False
        
        # TODO 월에 맞은 일이 있는경우. 윤년...

        # 정상
        return True

    @classmethod
    def is_amount(cls, type_in):

        # 비정상
        if not cls.has_only(type_in, config = 'integer'):
            # 숫자가 아닌게 들어있으면 : 음수 까지 제외가능
            return False
        if type_in[0] == '0':
            # 0이거나 0으로 시작하면 
            return False

        # 정상
        return True


    @classmethod
    def is_yn(cls, type_in):
        yn_set = {'y','yes','n','no'}

        if not cls.has_only(type_in, config='character'):
            # 문자 이외의 것을 갖는다면
            return False
        if type_in not in yn_set:
            # 정해진 yes, no 세트 안에 포함되지 않는다면
            return False

        return True

    @classmethod
    def is_menu(cls, typein, view_class):
        

        # set menu_set
        if view_class == 'Admin':
            menu_set = set(range(1,4))

        elif view_class == 'Saving':
            menu_set = set(range(1,6))
            

        # check typein is in menu_set
        if not cls.has_only(typein, config='integer'):
            # 숫자 이외의 것이 들어있으면
            return False
            
        if int(typein) not in menu_set:
            # 허용된 숫자 범위를 벗어나면
            return False

        return True
                

    @classmethod
    def type_in_menu(cls, view_class = 'Admin'):

        while True:
            typein = input()

            if cls.is_menu(typein, view_class):
                return int(typein)
            else:
                print('메뉴 입력 범위를 벗어났습니다. 다시 입력하세요.')


    @classmethod
    def type_in_yes_or_no(cls):

        while True:
            stripped_string = input().lower()

            if cls.is_yn(stripped_string):
                return stripped_string
            else:
                print('잘못된 입력입니다.(yes or no)')

    @classmethod
    def type_in_amount(cls):

        while True:
            stripped_string = input()

            if cls.is_amount(stripped_string):
                return int(stripped_string)
            else:
                print('잘못된 입력입니다.(0 이상의 양의 정수만 입력)')

    @classmethod
    def type_in_date(cls):

        while True:
            keyin = input()
            stripped_string = cls.remove_puctuation(keyin,config='date')

            if cls.is_date(stripped_string):
                return stripped_string
            else:
                print('잘못된 입력입니다.(허용된 날짜 형식만 입력)')


# type_in_menu
# type_in_yes_or_no
# type_in_amount
# type_in_date
# result = KeyIn.type_in_amount()
# print(type(result))
# print('result : ',result)