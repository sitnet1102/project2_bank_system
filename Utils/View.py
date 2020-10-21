from KeyInUtils import KeyIn as keyin
# from IOUtils import FileReader as reader


class ViewBase :
    '''공통된 화면요소를 여기에 정의합니다'''

    def confirm_check(step_name):
        print(f'{step_name}을 진행하시겠습니까?')

    def describe_current_stage(stage_name):
        print(f'{stage_name} 입니다')

class DepositView(ViewBase):
    '''예금 화면요소를 정의합니다. 공통 요소를 수정하고 싶을 땐 method override를 사용합니다'''

class AdminView(ViewBase):
    '''관리자 화면 요소를 정의합니다'''

    @classmethod
    def menu(cls):
        print('1. 사용자 정보조회')
        print('2. 전체 내역조회')
        print('3. 로그 아웃')

        # user_keyin = keyin.choose_menu()
        # return user_keyin

    @classmethod
    def user_data(cls):
        super().describe_current_stage('사용자 정보 조회')

        # 전체 사용자 정보 출력

        # return

    @classmethod
    def transaction_data(cls):
        super().describe_current_stage('전체 내역 조회')
        
        # 거래 내역 출력

        # return

class SavingView(ViewBase):
    '''적금 화면요소를 정의합니다'''


