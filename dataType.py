
'''
데이터 타입과 관련된 메소드들은 기획서를 기반으로 합니다.
'''


class dataTypeBase :
    ''' 데이터 타입 추상 클래스입니다. '''

    @classmethod
    def dataConfirm(cls, data) : 
        #데이터 문법 확인 매소드
        pass

    @classmethod
    def dataToBasicType(cls, data) :
        #기본형 변환 메소드
        #if self.dataConfirm(data) :
        return data.strip(' ') # 양쪽 공백 지우기

    @classmethod
    def dataCompare(cls, A, B) :
        A = cls.dataToBasicType(A)
        B = cls.dataToBasicType(B)
        
        if A == B :
            return True
        else :
            return False

class DateData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        if len(data) == 6 :
            for i in range(len(data)) :
                if ord('0') <= ord(data[i]) <= ord('9') :
                    pass
                else : 
                    return False
            year = int(data[:2])
            month = int(data[2:4])
            day = int(data[4:])
            if 40 <= year <= 50 :
                return False
            if 1 <= month <= 12 :
                pass
            else :
                return False
            if 1 <= day <= 31 :
                pass
            else :
                return False       
        elif len(data) == 8 :
            if ord(data[2]) == ord('-') or ord(data[2]) == ord('/') or ord(data[2]) == ord('.') :
                for i in range(len(data)) :
                    if i == 2 or i == 5 :
                        if ord(data[2]) == ord(data[5]) :
                            pass
                        else :
                            return False
                    else : 
                        if ord('0') <= ord(data[i]) <= ord('9') :
                            pass
                        else : 
                            return False
                year = int(data[:2])
                month = int(data[3:5])
                day = int(data[6:])
                if 40 <= year <= 50 :
                    return False
                if 1 <= month <= 12 :
                    pass
                else :
                    return False
                if 1 <= day <= 31 :
                    pass
                else :
                    return False
            else : 
                for i in range(len(data)) :
                    if ord('0') <= ord(data[i]) <= ord('9') :
                        pass
                    else : 
                        return False
                year = int(data[:4])
                month = int(data[4:6])
                day = int(data[6:])
                if 1900 <= year <= 2100 :
                # 구간 변경??? 1950 <= year <= 2040
                    pass
                else :
                    return False
                if 1 <= month <= 12 :
                    pass
                else :
                    return False
                if 1 <= day <= 31 :
                    pass
                else :
                    return False
        elif len(data) == 10 :
            if ord(data[4]) == ord('-') or ord(data[4]) == ord('/') or ord(data[4]) == ord('.') :
                for i in range(len(data)) :
                    if i == 4 or i == 7 :
                        if ord(data[4]) == ord(data[7]) :
                            pass
                        else :
                            return False
                    else : 
                        if ord('0') <= ord(data[i]) <= ord('9') :
                            pass
                        else : 
                            return False
                year = int(data[:4])
                month = int(data[5:7])
                day = int(data[8:])
                if 1900 <= year <= 2100 :
                # 구간 변경??? 1950 <= year <= 2040
                    pass
                else :
                    return False
                if 1 <= month <= 12 :
                    pass
                else :
                    return False
                if 1 <= day <= 31 :
                    pass
                else :
                    return False
        else :
            return False
        return True

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        if cls.dataConfirm(data) :
            if len(data) == 6 :
                tmp = ""
                if int(data[:2]) < 40 :
                    tmp = "20"
                elif int(data[:2]) > 50 :
                    tmp = "19"
                result = tmp + data
            elif len(data) == 8 :
                if ord(data[2]) == ord('-') or ord(data[2]) == ord('/') or ord(data[2]) == ord('.') :
                    tmp = ""
                    if int(data[:2]) < 40 :
                        tmp = "20"
                    elif int(data[:2]) > 50 :
                        tmp = "19"
                    result = tmp + data[:2] + data[3:5] + data[6:]
                else : 
                    result = data

            elif len(data) == 10 :
                result = data[:4] + data[5:7] + data[8:]
        return result



class BankAccountData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        if len(data) == 16 :
            if ord(data[4]) == ord('-') or ord(data[2]) == ord(' ') or ord(data[2]) == ord('.') :
                for i in range(len(data)) :
                    if i == 4 or i == 8 :
                        if ord(data[4]) == ord(data[8]) :
                            pass
                        else :
                            return False
                    else : 
                        if ord('0') <= ord(data[i]) <= ord('9') :
                            pass
                        else : 
                            return False
        elif len(data) == 14 : 
            for i in range(len(data)) :
                if ord('0') <= ord(data[i]) <= ord('9') :
                    pass
                else : 
                    return False
        else : 
            return False
        return True

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        if cls.dataConfirm(data) :
            if len(data) == 14 :
                result = data
            elif len(data) == 16 :
                if ord(data[4]) == ord('-') or ord(data[4]) == ord(' ') or ord(data[4]) == ord('.') :
                    result = data[:4] + data[5:8] + data[9:]
        return result


class PasswordData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        check = True 
        num = 0
        sEng = 0
        bEng = 0
        sChar = 0
        otherChar = 0
        if len(data) < 10 or len(data) > 20 :
            return False
        for i in range(len(data)) :
            if ord('0') <= ord(data[i]) <= ord('9') :
                num = num + 1
            elif ord('a') <= ord(data[i]) <= ord('z') :
                sEng = sEng + 1
            elif ord('A') <= ord(data[i]) <= ord('Z') :
                bEng = bEng + 1
            elif ord(data[i]) == ord('!') or ord(data[i]) == ord('@') or ord(data[i]) == ord('#') or ord(data[i]) == ord('$') or ord(data[i]) == ord('%') or ord(data[i]) == ord('^') or ord(data[i]) == ord('&') or ord(data[i]) == ord('*') or ord(data[i]) == ord('(') or ord(data[i]) == ord(')') :
                sChar = sChar + 1
            else : 
                otherChar = otherChar + 1
        '''
        print(num)
        print(sEng)
        print(bEng)
        print(sChar)
        '''
        if num == 0 or sEng == 0 or bEng == 0 or sChar == 0 :
            check = False

        if otherChar == 0 :
            pass
        else : 
            check = False
        return check



class NameData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        check = True
        if len(data) <= 1 or len(data) > 10 :
            check = False
        for i in range(1, len(data)) :
            if data[i] == " " :
                check = False
            if ord('가') <= ord(data[i]) <= ord('힣') :
                pass
            else :
                check = False   
        return check





class TimeData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        if len(data) == 8 :
            for i in range(len(data)) :
                if i == 2 or i == 5 :
                    if ord(data[i]) == ord(':') :
                        pass
                    else :
                        return False
                else : 
                    if ord('0') <= ord(data[i]) <= ord('9') :
                        pass
                    else : 
                        return False
            h = int(data[:2])
            min = int(data[3:5])
            sec = int(data[6:-1])
            if 0 <= h <= 23 :
                pass
            else :
                return False
            if 0 <= min <= 59 :
                pass
            else :
                return False
            if 0 <= sec <= 59 :
                pass
            else :
                return False
        else :
            return False
        return True


    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        if cls.dataConfirm(data) :
            return data[:2] + data[3:5] + data[6:]
        else :
            return result



class PriceData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        intdata = int(data)
        if intdata >= 0 and intdata < 1000000000000000 :
            if data == 0 :
                return True
            else :
                if ord(data[0]) == ord('0'):
                    return False
                else :
                    return True
        else :
            return False