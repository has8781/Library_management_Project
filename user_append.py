from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


# 추가 버튼을 클릭했을 때 호출되는 이벤트 핸들러
def append():
    print('추가 버튼 클릭')
    # 빈칸이 있으면
        # 메시지박스 출력 후 등록화면창으로 돌아감

    # 전화번호가 중복 되면 (아직 구현 x)
        # 메시지박스 출력 후 등록화면창으로 돌아감

    # 등록을 묻는 메시지박스 출력 (예, 아니오)
        # '예'를 누를경우
            # 등록되었다는 메시지박스 출력 (확인)
            # 엔트리와 텍스트의 내용을 비움

        # '아니오'를 누를경우
            # 메시지 박스를 뜨운 후 등록화면창으로 돌아감 (내용을 비우지 않음)


# 임시화면
main = Tk()
main.geometry("800x500")
# def user_append(main) :    #회원등록(매개변수 = 초기화면)  #나중에 다른파일과 함수로 연결할거임

# '회원등록' 레이블 생성 글자크기 설정
# '회원등록' 레이블을 main에 부착

# '이름' 레이블 생성
# '이름' 레이블을 main에 부착

# '이름' 엔트리(텍스트박스) 생성
# '이름' 엔트리를 main에 부착

# '생년월일' 레이블 생성
# '생년월일' 레이블을 main에 부착

# '생년월일' 엔트리(텍스트박스) 생성
# '생년월일' 엔트리를 main에 부착

# 성별 라디오버튼 생성
# 성별 라디오버튼 부착

# '전화번호' 레이블 생성
# '전화번호' 레이블을 main에 부착

# '전화번호' 첫번째 엔트리(텍스트박스) 생성
# '전화번호' 첫번째 엔트리를 main에 부착


# '전화번호' 두번째 엔트리(텍스트박스) 생성
# '전화번호' 두번째 엔트리를 main에 부착

# '전화번호' 세번째 엔트리(텍스트박스) 생성
# '전화번호' 세번째 엔트리를 main에 부착


# '이메일' 이블 생성
# '이메일' 레이블을 main에 부착

# '이메일' 엔트리(텍스트박스) 생성
# '이메일' 엔트리를 main에 부착



# '추가'버튼 생성 (command = append)
# 버튼을 main 부착


main.mainloop()