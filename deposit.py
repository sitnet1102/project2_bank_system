class Deposit:
    
    def view_deposit_main():
        print("1. 예금조회\n2.내역조회\n3.입금\n4.출금\n5.계좌이체\n6.뒤로가기\n\n")
        main_input = input()
        if main_input == 1 :
            look_deposit()
        elif main_input == 2:
            look_history
        elif main_input == 3:
            put_money()
        elif main_input == 4:
            withdraw
        elif main_input == 5:
            transfer_money()
        elif main_input == 6:
            #뒤로가기 - 로그인메인
            pass
        else:
            view_deposit_main()
        
    def press_anykey():
        print("아무키나 누르시면 예금 페이지로 돌아갑니다.")
        pressanykey = input()
        if pressanykey:
            view_deposit_main()

    
    def look_deposit():
        #json에서 해당 회원의 deposit을 가져오는 부분 필요
        #deposit = something
         print("예금 조회입니다.\n")
         print("잔액은 %d 원입니다.\n" % deposit)
         
         press_anykey()

    def look_history():
        #시작날짜-종료날짜-내역출력
        print("내역 조회입니다.\n")
        print("시작 날짜를 입력하세요\n")
        start_date = input()
        print("종료 날짜를 입력하세요\n")
        end_date = input()
        if start_date > end_date:
            print("종료 날짜는 시작 날짜를 앞설 수 없습니다.")
            press_anykey()
        
        #내역 출력
    

    def put_money():
        #확인 -> 금액입력 -> 입금완료메세지
        confirmation("입금")
        print("금액을 입력하세요")
        money = input()

        #if 형식오류:
        #   print("오류")
        #   press_anykey()
        #else
        #   입금 실행
        #   print("결과메세지")
        #   press_anykey()

    
    def withdraw():
        #확인 -> 금액입력 -> 출금완료메세지
        confirmation("출금")
        print("금액을 입력하세요")
        money = input()

        #if 금액 > 잔액:
        #   print("잔액부족")
        #   press_anykey()
        #else
        #   출금 실행
        #   print("결과메세지")
        #   press_anykey()




    def transfer_money():
        #금액 -> 계좌 -> 이체확인 -> 이체 -> 결과메세지
        print("금액을 입력하세요\n")
        money = input()
        print("이체하실 계좌번호를 입력하세요\n")
        account = input()
        #account에 대한 형식 처리
        #if 잔액 < 금액
        #   print("잔액부족")
        #else
        #   print(이체 진행할것?)
        #   confirmation 변형
        #   이체 진행코드

        


    def confirmation(prm):
        print(prm + "을 진행하시겠습니까?")
        while(True):
            answer = input()
            if(answer == Y):
                break
            elif(answer == N):
                view_deposit_main()
            else:
                print("잘못 입력하셨습니다 Y혹은 N을 입력해주세요")
                continue
        
