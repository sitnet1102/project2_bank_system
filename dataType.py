
'''
데이터 타입과 관련된 메소드들은 기획서를 기반으로 합니다.
'''


class dataTypeBase :
    ''' 데이터 타입 추상 클래스입니다. '''

    def dataConfirm(self, data) : 
        #데이터 문법 확인 매소드
        pass

    def dataToBasicType(self, data) :
        #기본형 변환 메소드
        #if self.dataConfirm(data) :
        return data.strip() # 양쪽 공백 지우기

    def dataCompare(self, A, B) :
        A = self.dataToBasicType(A)
        B = self.dataToBasicType(B)
        
        if A == B :
            return True
        else :
            return False

class DateData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :

        return True
        return False
        pass

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        return result
        pass



class BankAccountData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :

        return True
        return False
        pass

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        return result
        pass


class PasswordData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :

        return True
        return False
        pass

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        return result
        pass



class NameData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :

        return True
        return False
        pass

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        return result
        pass




class TimeData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :

        return True
        return False
        pass

    @classmethod
    def dataToBasicType(cls, data) :
        result = ""
        return result
        pass



class PriceData(dataTypeBase) :

    @classmethod
    def dataConfirm(cls, data) :
        if data >= 0 and data < 1000000000000000 :
            if data == 0 :
                return True
            else :
                if data[:1] != 0 :
                    return True
                else :
                    return False
        else :
            return False
        pass


