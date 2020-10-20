class View :

    def bank_main(self) :
        print('''
            은행 전산 시스템 입니다.\n
            1. 로그인\n
            2. 신규가입\n
            3. 종료\n
        ''')

    def login_main(self, name) :
        print("         " + name + 
            
            " 님 안녕하세요.\n" +
            '''
             1. 예금 조회\n
             2. 적금 조회\n
             3. 내 정보 조회\n
             4. 로그 아웃\n
        ''')

    def my_info(self, name, date, account, savings_account) :
        print(name + " 님의 정보입니다.\n"
            + "이름 : " + name 
            + "\n가입일 : " + date
            + "\n예금 계좌번호 : " + account
            + "\n적금 계좌번호 : " + savings_account
            + "\n"
        )
    
    def exit(self) :
        print("시스템을 종료합니다.\n")

    def account_input(self) :
        print("계좌번호를 입력하세요.\n")

    def password_input(self) :
        print("비밀번호를 입력하세요.\n")

    def logout(self) :
        print("로그아웃\n")

    def entry_confirm(self) :
        print("신규 가입을 진행하시겠습니까?(Y/N)\n")

    def name_confirm(self) :
        print("신규 회원 등록입니다.\n")
        print("이름을 입력하세요.\n")

    def password_confirm(self) :
        print("비밀번호를 입력하세요. (비밀번호는 1 2.....)\n")
        ## 비밀번호 형식에 대해서 설명 해줄건지???

    def wrong_name(self) : 
        print("잘못된 이름입니다.\n")

    def wrong_password(self) :
        print("잘못된 비밀번호 입니다.\n")

    def info_confirm(self, name, date, password) :
        print("회원 정보는 다음과 같습니다.\n"
            + "이름 : " + name 
            + "\n가입일 : " + date
            + "\n비밀번호 : " + password
            + "\n입력하신 정보가 맞다면 Y, 일치하지 않는다면 N\n")

    def cancel(self) :
        print("가입이 취소되었습니다.\n")
    
    def join(self, name, account) :
        print("가입이 완료되었습니다.\n"
            + name + " 님의 계좌번호는 " + account + " 입니다.\n")
        
    def press_anykey(self) :
        print("아무키나 누르세요\n")