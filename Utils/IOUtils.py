import json, os
from View import AdminView as av


class IOBase : 
    pass

class FileReader(IOBase):

    Base_dir = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'data')
    user_file = r'users.json'
    accounts_file = r'accounts.json'
    history_file = r'history.json'
    
    @classmethod
    def read_all_users(cls):
        file_path = os.path.join(cls.Base_dir, cls.user_file)

        with open(file_path, encoding='utf-8') as f:
            users = json.load(f) # users.json 파일의 내용을 dictionary 형식으로 읽어옵니다.


    @classmethod
    def read_all_accounts(cls):
        file_path = os.path.join(cls.Base_dir, cls.accounts_file)

        with open(file_path, encoding='utf-8') as f:
            accounts = json.load(f) # accounts.json 파일의 내용을 dictionary 형식으로 읽어옵니다.
            

    @classmethod
    def read_all_transactions(cls):
        file_path = os.path.join(cls.Base_dir, cls.history_file)

        with open(file_path, encoding='utf-8') as f:
            history = json.load(f) # history.json 파일의 내용을 dictionary 형식으로 읽어옵니다.


class FileWriter(IOBase):
    pass


