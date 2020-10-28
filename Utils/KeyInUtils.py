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
    def make_eight_digit_date(cls, stripped_string):
        if len(stripped_string) == 6:
            # under 40
            if int(stripped_string[0:2]) < 40:
                stripped_string = '20'+stripped_string
            # over 50
            elif int(stripped_string[0:2]) > 50:
                stripped_string = '19'+stripped_string
            # else
            else:
                stripped_string = '19'+stripped_string

        return stripped_string

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
    def is_leap_year(cls, year):
        if year%4 == 0 and year%100 == 0 and year%400 == 0:
            return True 
        if year%4 == 0 and year%100 == 0:
            return False # 평년
        if year%4 == 0:
            return True

        return False # 평년

    @classmethod
    def is_date(cls, type_in):
        thirty = {4,6,9,11}

        # 비정상
        # 허용된 특수문자만 제거했으므로, 모두 숫자가 아니면
        p = re.compile('[a-zA-Z]+')
        if p.search(type_in) is not None:
            return False
        
        # 6자리거나 8자리가 아니면
        if len(type_in) != 6 and len(type_in) != 8:
            return False

        # 8자리로 세팅
        mydate = cls.make_eight_digit_date(type_in)
        year = int(mydate[:4])
        month = int(mydate[4:6])
        day = int(mydate[6:])

        if month == 0 or day == 0:
            # 0월 0일
            return False
        if month > 12 or day > 31:
            # 13월 40일
            return False
        if year < 1900:
            # 자리 입력시 연도 제한
            return False
        
        # 월에 맞는 일인지
        if month in thirty:
            # 30일 월인데 31일로 입력한 경우
            if day == 31:
                return False

        # 윤년 체크
        if month == 4 :
            # 4월
            if cls.is_leap_year(year):
                # 윤년인데 28일로 입력한 경우
                if day == 28:
                    return False
            else :
                # 윤년 아닌데 29일로 입력한 경우
                if day == 29:
                    return False

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

        if len(typein) == 0:
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

        stripped_string = input()

        if cls.is_amount(stripped_string):
            return int(stripped_string)
        else:
            return False

    @classmethod
    def type_in_date(cls):

        keyin = input()
        stripped_string = cls.remove_puctuation(keyin,config='date')

        if cls.is_date(stripped_string):
            # 허용된 키보드 입력만 8자리로 출력한다.
            return cls.make_eight_digit_date(stripped_string)
        else:
            return False


# type_in_menu
# type_in_yes_or_no
# type_in_amount
# type_in_date
# while True:
#     result = KeyIn.type_in_date()
#     if result:
#         print('정확한 입력')
#         print(type(result))
#         print('result : ',result)
#     else:
#         print('부정확한입력')
#         print('False를 출력한다')