import json, os
from datetime import datetime


class IOBase : 
    Base_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'data')
    user_file = r'test_users.json'
    # user_file = r'users.json'
    accounts_file = r'test_accounts.json'
    # accounts_file = r'accounts.json'
    history_file = r'test_history.json'
    # history_file = r'history.json'

class FileReader(IOBase):
    
    @classmethod
    def read_all_users(cls):
        file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(file_path, encoding='utf-8') as f:
            users = json.load(f) # users.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
        return users


    @classmethod
    def read_all_accounts(cls, account_type = 'Savings'):
        file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(file_path, encoding='utf-8') as f:
            accounts = json.load(f) # accounts.json 파일의 내용을 dictionary 형식으로 읽어옵니다.

        return accounts[account_type]
            

    @classmethod
    def read_all_transactions(cls):
        file_path = os.path.join(cls.Base_dir, cls.history_file)

        with open(file_path, encoding='utf-8') as f:
            history = json.load(f) # history.json 파일의 내용을 dictionary 형식으로 읽어옵니다.

        return history


class FileWriter(IOBase):

    @classmethod
    def cancel_saving(cls, user_id, account_num):
        
        account_file_path = os.path.join(cls.Base_dir, cls.accounts_file)
        user_file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(account_file_path, encoding='utf-8') as f:
            accounts = json.load(f)
        with open(user_file_path, encoding='utf-8') as f:
            users = json.load(f)

        # 1. accounts에서 기록 삭제
        accounts['Savings'].pop(account_num)

        with open(account_file_path, mode='w', encoding='utf-8') as f:
            json.dump(accounts,f)

        # 2. users에서 적금 삭제
        users[user_id]['accounts'].remove(account_num)
        with open(user_file_path, mode='w',encoding='utf-8') as f:
            json.dump(users, f)

    @classmethod
    def put_money(cls, account_num, amount):
        account_file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(account_file_path, encoding='utf-8') as f:
            accounts = json.load(f)

        accounts['Savings'][account_num]['balance'] += amount

        with open(account_file_path, mode='w',encoding='utf-8') as f:
            json.dump(accounts, f)

    @classmethod
    def make_history(cls, sender, receiver, amount, account_type = 'Savings'):
        file_path = os.path.join(cls.Base_dir, cls.history_file)

        now = datetime.now()
        now_date = now.strftime('%Y%m%d')
        now_time = now.strftime('%H%M%S')

        with open(file_path, encoding='utf-8') as f:
            history = json.load(f)

        # 송금 정보
        info = {
            "from" : sender, 
            "to" : receiver,
            "date" : now_date,
            "time" : now_time,
            "amount" : amount
        }

        # 적금
        if account_type == 'Savings' : 
            if sender not in history.keys():
                history[sender] = []
            history[sender].append(info)
        # 다른 타입의 계좌인 경우 이곳에 정의
        # elif

        with open(file_path, mode='w', encoding='utf-8') as f:
            json.dump(history, f)