from KeyInUtils import KeyIn as keyin
from IOUtils import FileReader as reader
from IOUtils import FileWriter as writer


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
    def show_user_datas(cls):
        super().describe_current_stage('사용자 정보 조회')

        users = reader.read_all_users()
        all_deposits = reader.read_all_accounts(account_type = 'Deposits')
        all_savings = reader.read_all_accounts()

        for info in users.values():
            deposits, savings = [], []
            # 적금, 예금 분리
            for account_num in info['accounts']:
                if int(account_num[0]) < 5: # 예금
                    deposits.append(account_num)
                else: # 적금
                    savings.append(account_num)

            # 출력
            print(f"{info['name']} / {info['sign_up_date']}", end=' / ')

            for deposit in deposits:
                balance = all_deposits[deposit]['balance']
                print(f"{deposit} / {balance}", end=' / ')
            for saving in savings:
                balance = all_savings[saving]['balance']
                print(f"{saving} / {balance}", end=' / ')

            print()
        print(f"총 {len(users)} 명 입니다.")


    @classmethod
    def show_transaction_datas(cls):
        super().describe_current_stage('전체 내역 조회')
        
        transactions = reader.read_all_transactions()
        transactions_without_redundancy = []
        for one_account_history in transactions.values():
            for history in one_account_history:
                stamp = history['date']+history['time'] # exclude redundancy
                if stamp not in transactions_without_redundancy:
                    transactions_without_redundancy.append(stamp)
                    print(f"{history['from']} / {history['to']} / {history['date']} / {history['time']} / {history['amount']}")

        print(f"총 {len(transactions_without_redundancy)} 건 입니다.")

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

        savings = reader.read_all_accounts()
        for user_saving in user.savings:
            balance = savings[user_saving]['balance']
            due_date = savings[user_saving]['expiration_date']
            print(f'잔액은 {balance}원 입니다.')
            print(f'만기일은 {due_date} 입니다.')

    @classmethod
    def __show_saving_history_result(cls, user, start_date, end_date):
        super().Ais(user.name+'님의 내역')

        transactions = reader.read_all_transactions()
        if user.savings in transactions.keys():
            for history in transactions[user.savings]:
                if int(history['date']) > int(start_date) and int(history['date']) < int(end_date):
                    print(f"{history['from']} / {history['to']} / {history['date']} / {history['time']} / {history['amount']}")
            super().Ais('마지막 페이지')
        else:
            print('내역이 없습니다.')


    @classmethod
    def __show_saving_history_sub(cls, user, start_date):
        # TODO 올바른 날짜 keyin utils
        end_date = '20201231'

        if True:
            cls.__show_saving_history_result(user, start_date, end_date)
        else:
            print('''올바르지 않은 날짜 입력입니다.
            아무키나 입력하세요.''')
            input()

    @classmethod
    def show_saving_history(cls, user):
        super().describe_current_stage('내역 조회')
        super().request_keyin('시작 날짜')

        # TODO 올바른 날짜 kyein utils
        start_date = '20000101'

        if True:
            super().request_keyin('종료 날짜')
            cls.__show_saving_history_sub(user, start_date)
        else:
            print('''올바르지 않은 날짜 입력입니다.
            아무키나 입력하세요.''')
            input()

    def __put_money_in_saving_result(user, amount):
        print(f'{amount} 이 입금되었습니다.')

        # 적금 계좌 갱신
        writer.put_money(user.savings, amount)
        accounts = reader.read_all_accounts()
        balance = accounts[user.savings]['balance']
        print(f"잔액은 {balance}원 입니다.")

        # 거래 내역 저장
        writer.make_history(user.savings, user.savings, amount)


    @classmethod
    def __put_money_in_saving_sub(cls, user):
        # TODO 올바른 금액 입력 keyin utils
        money_amount = 1000
        if money_amount:
            cls.__put_money_in_saving_result(user, money_amount)
        else:
            print('''금액이 올바르지 않습니다.
            아무키나 입력하세요.''')
            input()

    @classmethod
    def put_money_in_saving(cls, user):
        super().confirm_check('입금')

        # TODO keyin_result = keyin.yes_or_no()
        keyin_result = 'y'
        if keyin_result == 'y':
            super().request_keyin('금액')
            cls.__put_money_in_saving_sub(user)
        else:
            print('아무키나 입력하세요')
            input()

    def __cancel_saving_result(user):
        print('해약이 완료되었습니다.')
        writer.cancel_saving(user.id, user.savings)
        print(reader.read_all_users())

    @classmethod
    def cancel_saving(cls, user):
        super().confirm_check('해약')

        # TODO keyin_result = keyin.yes_or_no()
        keyin_result = 'y'
        if keyin_result == 'y':
            cls.__cancel_saving_result(user)
        else:
            print('''해약이 완료되지 않았습니다.
            메뉴로 돌아갑니다.''')