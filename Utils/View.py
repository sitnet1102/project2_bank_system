import mainPrompt as mp
from Utils.KeyInUtils import KeyIn as keyin
from Utils.IOUtils import FileReader as reader
from Utils.IOUtils import FileWriter as writer
from dataType import BankAccountData as bd
from dataType import PriceData as prd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class ViewBase:
    '''공통된 화면요소를 여기에 정의합니다'''

    def confirm_check(step_name):
        print(f'{step_name}을(를) 진행하시겠습니까?(Yes or no)')

    def describe_current_stage(stage_name):
        print(f'{stage_name} 입니다')

    def AisB(a, b):
        print(f'{a} 은(는) {b} 입니다.')

    def Ais(a):
        print(f'{a}입니다.')

    def request_keyin(request_statement):
        print(f'{request_statement} 을(를) 입력하세요.')


class DepositView(ViewBase):
    '''예금 화면요소를 정의합니다. 공통 요소를 수정하고 싶을 땐 method override를 사용합니다'''
    @classmethod
    def menu(cls):
        print('''
                < 적금 >
                1. 예금 조회
                2. 내역 조회
                3. 입금
                4. 출금
                5. 계좌 이체
                6. 뒤로가기
                ''')

        # TODO 메뉴 선택결과 받기
        keyin_choice = keyin.type_in_menu(view_class='Deposit')
        return keyin_choice

    @classmethod
    def show_deposit_balance(cls, user):
        super().describe_current_stage('예금 조회')

        accounts = reader.read_all_accounts_in_deposit()
        # for user_deposit in user.deposits:
        balance = accounts[user.deposits]['balance']
        print(f'잔액은 {balance}원 입니다.\n\n')
        print('아무키나 입력하세요')
        input()
        

    @classmethod
    def __show_deposit_history_result(cls, user, start_date, end_date):
        super().Ais(user.name+'님의 내역')
        #10개씩 출력 --> 아무키나 입력시 다음 10개로
        transactions = reader.read_all_transactions()
        if user.deposits in transactions.keys():
            cnt = -1
            for history in transactions[user.deposits]:
                cnt = cnt + 1
                if int(history['date']) >= int(start_date) and int(history['date']) <= int(end_date):
                    print(
                        f"{history['from']} / {history['to']} / {history['date']} / {history['time']} / {history['amount']}")
                    if cnt == 10:
                        cnt = 0
                        input()
                        continue
                    else:
                        pass
            super().Ais('마지막 페이지')
        else:
            print('내역이 없습니다.')

    @classmethod
    def __show_deposit_history_sub(cls, user, start_date):
        end_date = keyin.type_in_date()
        
        if end_date:
            if int(end_date) >= int(start_date):
                cls.__show_deposit_history_result(user, start_date, end_date)
            else:
                print('시작 시점이 종료 시점보다 늦습니다. 아무키나 입력하세요.....\n\n')
                input()
        else:
            print('올바르지 않은 날짜 입력입니다. 아무키나 입력하세요......\n\n')
            input()

    @classmethod
    def show_deposit_history(cls, user):
        super().describe_current_stage('내역 조회')
        super().request_keyin('시작 날짜')

        start_date = keyin.type_in_date()

        if start_date:
            super().request_keyin('종료 날짜')
            cls.__show_deposit_history_sub(user, start_date)
        else:
            print('올바르지 않은 날짜 입력입니다. 아무키나 입력하세요......\n\n')
            input()


    def __put_money_in_deposit_result(user, amount):
        print(f'{amount} 이 입금되었습니다.')

        # 예금 계좌 갱신
        writer.put_money_in_deposit(user.deposits, amount)
        accounts = reader.read_all_accounts_in_deposit()
        balance = accounts[user.deposits]['balance']
        print(f"잔액은 {balance}원 입니다.")

        # 거래 내역 저장
        writer.make_history('00000000000000', user.deposits, amount, "Deposits_put")

    @classmethod
    def __put_money_in_deposit_sub(cls, user):
        money_amount = input()
        if money_amount:
            if prd.dataConfirm(money_amount):
                money_amount = int(prd.dataToBasicType(money_amount))
                cls.__put_money_in_deposit_result(user, money_amount)
            else:
                print('잘못된 형식입니다\n아무키나 입력하세요')
                input()
                return
        else:
            print('잘못된 형식입니다. 아무키나 입력하세요.')
            input()
            return

    @classmethod
    def put_money_in_deposit(cls, user):
        super().confirm_check('입금')

        # TODO keyin_result = keyin.yes_or_no()
        keyin_result = keyin.type_in_yes_or_no()
        if keyin_result == 'y' or keyin_result == 'yes':
            super().request_keyin('금액')
            cls.__put_money_in_deposit_sub(user)

        elif keyin_result == 'n' or keyin_result == 'no':
            print('취소하셨습니다\n아무키나 입력하세요')
            input()

        else:
            print('아무키나 입력하세요')
            input()

    def __withdraw_money_in_deposit_result(user, amount):
        print(f'{amount} 이 출금되었습니다.')

        # 예금 계좌 갱신
        writer.withdraw_money(user.deposits, amount)
        accounts = reader.read_all_accounts_in_deposit()
        balance = accounts[user.deposits]['balance']
        print(f"잔액은 {balance}원 입니다.")

        # 거래 내역 저장
        writer.make_history(user.deposits, '00000000000000', amount, "Deposits_withdraw")

    @classmethod
    def __withdraw_money_in_deposit_sub(cls, user):
        # TODO 올바른 금액 입력 keyin utils

        money_amount = input()
        if money_amount:
            if prd.dataConfirm(money_amount):
                money_amount = int(prd.dataToBasicType(money_amount))
            else:
                print('잘못된 형식입니다\n아무키나 입력하세요')
                input()
                return
        else:
            print('잘못된 형식입니다\n  아무키나 입력하세요')
            input()
            return
        accounts = reader.read_all_accounts_in_deposit()
        balance = accounts[user.deposits]['balance']

        if money_amount < balance:
            cls.__withdraw_money_in_deposit_result(user, money_amount)
        else:
            print('''잔액이 부족합니다 아무키나 입력하세요''')
            input()

    @classmethod
    def withdraw_money_in_deposit(cls, user):
        super().confirm_check('출금')

        keyin_result = keyin.type_in_yes_or_no()
        if keyin_result == 'y' or keyin_result == 'yes':
            super().request_keyin('금액')
            cls.__withdraw_money_in_deposit_sub(user)

        elif keyin_result == 'n' or keyin_result == 'no':
            print('취소하셨습니다\n아무키나 입력하세요')
            input()

        else:
            print('아무키나 입력하세요')
            input()


    
    def send_money_result(user, amount):
        print(f'{amount}원 이 이체되었습니다.')

        # 완료 메세지를 위해 예금 계좌 잔액 다시 로드
        accounts = reader.read_all_accounts_in_deposit()
        balance = accounts[user.deposits]['balance']
        print(f'잔액은 {balance}원 입니다.')

        

    @classmethod
    def __send_money_sub1(cls, user):
        # TODO 금액입력형식 / 계좌번호 입력형식

        money_amount = input()
        if money_amount:
            if prd.dataConfirm(money_amount):
                money_amount = int(prd.dataToBasicType(money_amount))
            else:
                print('잘못된 형식입니다\n아무키나 입력하세요')
                input()
                return
        else:
            print('잘못된 형식입니다\n  아무키나 입력하세요')
            input()
            return
        accounts_sender = reader.read_all_accounts_in_deposit()
        balance = accounts_sender[user.deposits]['balance']

        super().request_keyin('계좌번호')
        account_receiver = input()
        confirm = bd.dataConfirm(account_receiver)
        if confirm:
            account_receiver = bd.dataToBasicType(account_receiver)
            print(f'\n입금액 : {money_amount} 원')
            print(f'계좌번호 : {account_receiver}')
            super().confirm_check('이체')
            keyin_result = keyin.type_in_yes_or_no()
            if keyin_result == 'y' or keyin_result == 'yes':
                pass
            else:
                print('취소하였습니다')
                input()
                return
        else:
            print('잘못된 계좌번호입니다.  아무키나 입력하세요')
            input()
            return

        user_receiver = reader.read_one_users(account_receiver)

        if money_amount < balance:
            writer.withdraw_money(user.deposits, money_amount)
            writer.put_money_in_deposit(user_receiver['accounts'][0], money_amount)
            writer.make_history(user.deposits, user_receiver['accounts'][0], money_amount, 'Deposits_send')
            cls.send_money_result(user, money_amount)
        else:
            print('''잔액이 부족합니다 아무키나 입력하세요''')
            input()

    @classmethod
    def send_money(cls, user):
        super().request_keyin('금액')
        cls.__send_money_sub1(user)
        super().request_keyin('계좌번호')

        # TODO keyin_result inputY/N
        keyin_result = 'y'
        if keyin_result == 'y':
            pass
        else:
            print('아무키나 입력하세요')
            input()


class AdminView(ViewBase):
    '''관리자 화면 요소를 정의합니다'''

    @classmethod
    def menu(cls):
        print('1. 사용자 정보조회')
        print('2. 전체 내역조회')
        print('3. 로그 아웃')

        keyin_choice = keyin.type_in_menu(view_class = 'Admin')
        return keyin_choice

    @classmethod
    def show_user_datas(cls):
        super().describe_current_stage('사용자 정보 조회')

        users = reader.read_all_users()
        all_deposits = reader.read_all_accounts(account_type='Deposits')
        all_savings = reader.read_all_accounts()

        for info in users.values():
            deposits, savings = [], []
            # 적금, 예금 분리
            for account_num in info['accounts']:
                if int(account_num[0]) < 5:  # 예금
                    deposits.append(account_num)
                else:  # 적금
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
        print(f"총 {len(users)} 명 입니다.\n\n")

        print('아무키나 입력하세요\n')
        input()

    @classmethod
    def show_transaction_datas(cls):
        super().describe_current_stage('전체 내역 조회')

        transactions = reader.read_all_transactions()
        transactions_without_redundancy = []
        for one_account_history in transactions.values():
            for history in one_account_history:
                stamp = history['date']+history['time']  # exclude redundancy
                if stamp not in transactions_without_redundancy:
                    transactions_without_redundancy.append(stamp)
                    print(
                        f"{history['from']} / {history['to']} / {history['date']} / {history['time']} / {history['amount']}")

        print(f"총 {len(transactions_without_redundancy)} 건 입니다.")

        print('아무키나 입력하세요.....\n')
        input()


class SavingView(ViewBase):
    '''적금 화면요소를 정의합니다'''

    @classmethod
    def menu(cls):
        print('''
                < 적금 >
                1. 적금 조회
                2. 내역 조회
                3. 입금
                4. 해약
                5. 뒤로가기
                ''')

        keyin_choice = keyin.type_in_menu(view_class = 'Saving')
        return int(keyin_choice)

    @classmethod
    def show_saving_balance(cls, user):
        super().describe_current_stage('적금 조회')

        savings = reader.read_all_accounts()
        if user.savings in savings.keys():
            balance = savings[user.savings]['balance']
            due_date = savings[user.savings]['expiration_date']
            print(f'잔액은 {balance}원 입니다.')
            print(f'만기일은 {due_date} 입니다.\n\n')
        else:
            print(f'{user.name}님의 적금 계좌가 존재하지 않습니다.')

        print('아무키나 입력하세요....\n')
        input()

    @classmethod
    def __show_saving_history_result(cls, user, start_date, end_date):
        super().Ais('<'+user.name+'님의 내역>\n')

        transactions = reader.read_all_transactions()
        if user.savings in transactions.keys():
            for history in transactions[user.savings]:
                if int(history['date']) > int(start_date) and int(history['date']) < int(end_date):
                    print(
                        f"{history['from']} / {history['to']} / {history['date']} / {history['time']} / {history['amount']}\n")
            super().Ais('마지막 페이지')
            print('아무키나 입력하세요....\n\n')
            input()
        else:
            print('내역이 없습니다.\n\n')

    @classmethod
    def __show_saving_history_sub(cls, user, start_date):

        end_date = keyin.type_in_date()
        
        if end_date:
            if int(end_date) >= int(start_date):
                cls.__show_saving_history_result(user, start_date, end_date)
            else:
                print('시작 시점이 종료 시점보다 늦습니다. 아무키나 입력하세요.....\n\n')
                input()
        else:
            print('올바르지 않은 날짜 입력입니다. 아무키나 입력하세요......\n\n')
            input()

    @classmethod
    def show_saving_history(cls, user):
        super().describe_current_stage('내역 조회')
        super().request_keyin('시작 날짜')


        start_date = keyin.type_in_date()
        
        if start_date:
            super().request_keyin('종료 날짜')
            cls.__show_saving_history_sub(user, start_date)
        else:
            print('올바르지 않은 날짜 입력입니다. 아무키나 입력하세요......\n\n')
            input()


    def __put_money_in_saving_result(user, amount):
        print(f'{amount}원이 입금되었습니다.')

        # 적금 계좌 갱신
        writer.put_money(user.savings, amount)
        accounts = reader.read_all_accounts()
        balance = accounts[user.savings]['balance']
        print(f"잔액은 {balance}원 입니다.")
        print('아무키나 입력하세요.....\n\n')
        input()

        # 거래 내역 저장
        writer.make_history(user.savings, user.savings, amount, account_type='Savings')

    @classmethod
    def __put_money_in_saving_sub(cls, user):

        money_amount = keyin.type_in_amount()
        if money_amount:
            cls.__put_money_in_saving_result(user, money_amount)
        else:
            print('금액이 올바르지 않습니다. 아무키나 입력하세요......\n')
            input()

    @classmethod
    def put_money_in_saving(cls, user):
        super().confirm_check('입금')

        keyin_result = keyin.type_in_yes_or_no()
        if keyin_result == 'y' or keyin_result == 'yes':
            super().request_keyin('금액')
            cls.__put_money_in_saving_sub(user)
        else:
            print('아무키나 입력하세요......\n\n')

    def __cancel_saving_result(user):
        print('해약이 완료되었습니다.')
        writer.cancel_saving(user, user.savings)
        print('아무키나 입력하세요....\n')
        input()


    @classmethod
    def cancel_saving(cls, user):
        super().confirm_check('해약')

        keyin_result = keyin.type_in_yes_or_no()
        if keyin_result == 'y' or keyin_result == 'yes':
            cls.__cancel_saving_result(user)
        else:
            print('해약이 완료되지 않았습니다. 메뉴로 돌아갑니다.\n\n')


class NewAccountView(ViewBase):
    ''' 회원가입 화면요소를 정의합니다'''

    @classmethod
    def entry_confirm(cls):
        print("신규 가입을 진행하시겠습니까?(Y/N)\n")

    @classmethod
    def name_confirm(cls):
        print("신규 회원 등록입니다.\n")
        print("이름을 입력하세요.\n")

    @classmethod
    def password_confirm(cls):
        print("비밀번호를 입력하세요. (비밀번호는 1 2.....)\n")
        # 비밀번호 형식에 대해서 설명 해줄건지???

    @classmethod
    def wrong_name(cls):
        print("잘못된 이름입니다.\n")

    @classmethod
    def wrong_password(cls):
        print("잘못된 비밀번호 입니다.\n")
        print("비밀번호는 숫자, 영어 소문자, 영어 대문자, \n")
        print("특수문자( !@#$%^&*() )중 하나씩을 반드시 포함하며\n")
        print("10자 이상 20자 이하이어야 합니다.\n")

    @classmethod
    def press_anykey(cls):
        print("아무키나 누르세요\n")

    @classmethod
    def info_confirm(cls, name, date, password):
        print("회원 정보는 다음과 같습니다.\n"
              + "이름 : " + name
              + "\n가입일 : " + date
              + "\n비밀번호 : " + password
              + "\n입력하신 정보가 맞다면 Y, 일치하지 않는다면 N\n")

    @classmethod
    def cancel(cls):
        print("가입이 취소되었습니다.\n")

    @classmethod
    def join(cls, name, account):
        print("가입이 완료되었습니다.\n"
              + name + " 님의 계좌번호는 " + account + " 입니다.\n")


class LoginMainView(ViewBase):
    ''' 로그인 화면요소를 정의합니다'''
    @classmethod
    def login_main(cls, name):
        print("         " + name +

              " 님 안녕하세요.\n" +
              '''
             1. 예금 조회\n
             2. 적금 조회\n
             3. 내 정보 조회\n
             4. 로그 아웃\n
        ''')

    @classmethod
    def my_info(cls, name, date, account, savings_account):
        print(name + " 님의 정보입니다.\n"
              + "이름 : " + name
              + "\n가입일 : " + date
              + "\n예금 계좌번호 : " + account
              + "\n적금 계좌번호 : " + savings_account
              + "\n"
              )

    @classmethod
    def logout(cls):
        print("로그아웃\n")

    @classmethod
    def press_anykey(cls):
        print("아무키나 누르세요\n")


class BankMainView(ViewBase):
    ''' 주 프롬프트 화면요소를 정의합니다'''
    @classmethod
    def bank_main(cls):
        print('''
            은행 전산 시스템 입니다.\n
            1. 로그인\n
            2. 신규가입\n
            3. 종료\n
        ''')

    @classmethod
    def exit(cls):
        print("시스템을 종료합니다.\n")

    @classmethod
    def account_input(cls):
        print("계좌번호를 입력하세요.\n")

    @classmethod
    def password_input(cls):
        print("비밀번호를 입력하세요.\n")

    @classmethod
    def wrong_data(cls):
        print("잘못된 계좌번호나 비밀번호 입니다.\n")
