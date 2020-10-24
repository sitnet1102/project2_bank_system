from KeyInUtils import KeyIn as keyin
from IOUtils import FileReader as reader


class ViewBase :
    '''공통된 화면요소를 여기에 정의합니다'''

    def confirm_check(step_name):
        print(f'{step_name}을(를) 진행하시겠습니까?')

    def describe_current_stage(stage_name):
        print(f'{stage_name} 입니다')

    def AisB(a,b):
        print(f'{a} 은(는) {b} 입니다.')

    def Ais(a):
        print(f'{a}입니다.')

    def request_keyin(request_statement):
        print(f'{request_statement} 을(를) 입력하세요.')

class DepositView(ViewBase):
    '''예금 화면요소를 정의합니다. 공통 요소를 수정하고 싶을 땐 method override를 사용합니다'''

class AdminView(ViewBase):
    '''관리자 화면 요소를 정의합니다'''

    @classmethod
    def menu(cls):
        print('1. 사용자 정보조회')
        print('2. 전체 내역조회')
        print('3. 로그 아웃')

        # TODO keyin_choice() 받기
        keyin_choice = 1
        return keyin_choice

    @classmethod
    def user_data(cls, user):
        super().describe_current_stage('사용자 정보 조회')

        # TODO 전체 사용자 정보 출력

    @classmethod
    def transaction_data(cls):
        super().describe_current_stage('전체 내역 조회')
        
        # TODO 거래 내역 출력

class SavingView(ViewBase):
    '''적금 화면요소를 정의합니다'''

    @classmethod
    def menu(cls):
        print('1. 적금 조회')
        print('2. 내역 조회')
        print('3. 입금')
        print('4. 해약')
        print('5. 뒤로가기')
        # TODO 메뉴 선택 결과 받기
        keyin_choice = 1
        return keyin_choice


    @classmethod
    def show_saving_balance(cls, user):
        super().describe_current_stage('적금 조회')
        # TODO 잔액, 만기일 가져오기 IOutils
        balance = 10
        due_date = 10
        print(f'잔액은 {balance}원 입니다.')
        print(f'만기일은 {due_date} 입니다.')


    def show_saving_history_result(user):
        super().Ais(user.__name+'님의 내역')
        # TODO 내역 출력

    def show_saving_history_sub(user):
        # TODO 올바른 날짜 keyin utils
        if True:
            show_saving_history_result(user)
        else:
            print('''올바르지 않은 날짜 입력입니다.
            아무키나 입력하세요.''')
            input()

    @classmethod
    def show_saving_history(cls, user):
        super().describe_current_stage('내역 조회')
        super().request_keyin('시작 날짜')

        # TODO 올바른 날짜 kyein utils
        if True:
            super().request_keyin('종료 날짜')
            show_saving_history_sub(user)
        else:
            print('''올바르지 않은 날짜 입력입니다.
            아무키나 입력하세요.''')
            input()

    def put_money_in_saving_result(user, amount):
        print(f'{amount} 이 입금되었습니다.')
        # TODO 입금 완료 + 현재 잔액 출력


    def put_money_in_saving_sub(user):
        # TODO 올바른 금액 입력 keyin utils
        money_amount = keyin
        if money_amount:
            put_money_in_saving_result(user, money_amount)
        else:
            print('''금액이 올바르지 않습니다.
            아무키나 입력하세요.''')
            input()

    @classmethod
    def put_money_in_saving(cls, user):
        super().confirm_check('입금')

        keyin_result = keyin.yes_or_no()
        if keyin_result == 'y':
            super().request_keyin('금액')
            put_money_in_saving_sub(user)
        else:
            print('아무키나 입력하세요')
            input()

    def cancel_saving_result(user):
        print('해약이 완료되었습니다.')
        # TODO 해약 결과 IOUtils

    @classmethod
    def cancel_saving(cls, user):
        super().confirm_check('해약')

        keyin_result = keyin.yes_or_no()
        if keyin_result == 'y':
            cancel_saving_result(user)
        else:
            print('''해약이 완료되지 않았습니다.
            메뉴로 돌아갑니다.''')



