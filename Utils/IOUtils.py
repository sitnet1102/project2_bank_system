import json
import os
from datetime import datetime


class IOBase:
    Base_dir = os.path.join(os.path.dirname(
        os.path.abspath(os.path.dirname(__file__))), 'data')
    # user_file = r'test_users.json'
    user_file = r'users.json'
    # accounts_file = r'test_accounts.json'
    accounts_file = r'accounts.json'
    # history_file = r'test_history.json'
    history_file = r'history.json'


class FileReader(IOBase):

    @classmethod
    def read_all_users(cls):
        file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(file_path, encoding='utf-8') as f:
            users = json.load(f)  # users.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
        return users

    @classmethod
    def read_all_accounts(cls, account_type='Savings'):
        file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(file_path, encoding='utf-8') as f:
            # accounts.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
            accounts = json.load(f)

        return accounts[account_type]

    @classmethod
    def read_all_accounts_in_deposit(cls, account_type='Deposits'):
        file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(file_path, encoding='utf-8') as f:
            # accounts.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
            accounts = json.load(f)

        return accounts[account_type]

    @classmethod
    def read_all_transactions(cls):
        file_path = os.path.join(cls.Base_dir, cls.history_file)

        with open(file_path, encoding='utf-8') as f:
            # history.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
            history = json.load(f)

        return history

    @classmethod
    def read_one_users(cls, account):
        file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(file_path, encoding='utf-8') as f:
            users = json.load(f)  # users.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
        try:
            result = users[account]
        except KeyError:
            result = False

        return result

    @classmethod
    def new_account_check(cls, account):
        file_path = os.path.join(cls.Base_dir, cls.user_file)
        result = False
        with open(file_path, encoding='utf-8') as f:
            users = json.load(f)  # users.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
        try:
            if users[account] == account:
                result = True
        except KeyError:
            result = False

        return result


class FileWriter(IOBase):

    @classmethod
    def cancel_saving(cls, user, account_num):

        account_file_path = os.path.join(cls.Base_dir, cls.accounts_file)
        user_file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(account_file_path, encoding='utf-8') as f:
            accounts = json.load(f)
        with open(user_file_path, encoding='utf-8') as f:
            users = json.load(f)

        # 1. accounts에서 기록 삭제 & 예금으로 이체
        balance = accounts['Savings'].get(account_num)['balance']
        accounts['Savings'].pop(account_num)
        accounts['Deposits'].get(user.deposits)['balance'] += balance

        with open(account_file_path, mode='w', encoding='utf-8') as f:
            json.dump(accounts, f, indent=4, ensure_ascii=False)

        # 2. users에서 적금 삭제
        users[user.deposits]['accounts'].remove(account_num)
        with open(user_file_path, mode='w', encoding='utf-8') as f:
            json.dump(users, f, indent=4, ensure_ascii=False)

    @classmethod
    def put_money(cls, account_num, amount):
        account_file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(account_file_path, encoding='utf-8') as f:
            accounts = json.load(f)

        accounts['Savings'][account_num]['balance'] += amount

        with open(account_file_path, mode='w', encoding='utf-8') as f:
            json.dump(accounts, f, indent=4, ensure_ascii=False)

    @classmethod
    def make_history(cls, sender, receiver, amount, account_type):
        file_path = os.path.join(cls.Base_dir, cls.history_file)

        now = datetime.now()
        now_date = now.strftime('%Y%m%d')
        now_time = now.strftime('%H%M%S')

        with open(file_path, encoding='utf-8') as f:
            history = json.load(f)

        # 송금 정보
        info = {
            "from": sender,
            "to": receiver,
            "date": now_date,
            "time": now_time,
            "amount": amount
        }

        # 적금
        if account_type == 'Savings':
            if sender not in history.keys():
                history[sender] = []
            history[sender].append(info)
        # 예금 종류별로 다른 히스토리가 기록됨

        elif account_type == 'Deposits_withdraw':
            if sender not in history.keys():
                history[sender] = []
            history[sender].append(info)
        elif account_type == 'Deposits_put':
            if receiver not in history.keys():
                history[receiver] = []
            history[receiver].append(info)
        # 계좌이체는 sender, receiver 모두 history에 기록해두어야함
        elif account_type == 'Deposits_send':
            if sender not in history.keys():

                if receiver not in history.keys():
                    history[sender] = []
                    history[receiver] = []
                else:

                    history[sender] = []
            else:
                if receiver not in history.keys():
                    history[receiver] = []
            history[receiver].append(info)
            history[sender].append(info)

        with open(file_path, mode='w', encoding='utf-8') as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

    @classmethod
    def make_user(cls, account, name, pw, date, savingsA):
        file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(file_path, encoding='utf-8') as f:
            user = json.load(f)

        # 유저 정보
        userInfo = {
            "name": name,
            "pw": pw,
            "sign_up_date": date,
            "accounts": [
                account,
                savingsA
            ]
        }

        if account not in user.keys():
            user[account] = []
        user[account].append(userInfo)

        with open(file_path, mode='w', encoding="utf-8") as f:
            json.dump(user, f, ensure_ascii=False, indent="\t")

    @classmethod
    def withdraw_money(cls, account_num, amount):
        account_file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(account_file_path, encoding='utf-8') as f:
            accounts = json.load(f)

        accounts['Deposits'][account_num]['balance'] -= amount

        with open(account_file_path, mode='w', encoding='utf-8') as f:
            json.dump(accounts, f, indent="\t")

    @classmethod
    def put_money_in_deposit(cls, account_num, amount):
        account_file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(account_file_path, encoding='utf-8') as f:
            accounts = json.load(f)

        accounts['Deposits'][account_num]['balance'] += amount

        with open(account_file_path, mode='w', encoding='utf-8') as f:
            json.dump(accounts, f, indent="\t")

    @classmethod
    def make_account(cls, account, date, account_type):
        file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(file_path, encoding='utf-8') as f:
            acc = json.load(f)

        balance = 0
        ex_date = int(date) + 30000  # 3년 추가
        # accountInfo = ""
        # 계좌 정보
        if account_type == "Deposits":
            accountInfo = {
                "balance": balance,
                "sign_up_date": date
            }
        elif account_type == "Savings":
            accountInfo = {
                "balance": balance,
                "sign_up_date": date,
                "expiration_date": ex_date
            }
        else:
            return False

        if account_type not in acc.keys():
            acc[account_type] = []
        if acc not in acc[account_type].keys():
            acc[account_type][account] = []
        acc[account_type][account].append(accountInfo)

        with open(file_path, mode='w', encoding="utf-8") as f:
            json.dump(user, f, ensure_ascii=False, indent="\t")
