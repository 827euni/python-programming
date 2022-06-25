i=0

password="python"

PW=input("비밀번호 : ")
i=1

    
while i<=3:
    if i<=2:
        if PW != password:
            print("비밀번호를 다시 입력하세요.")
            PW=input("비밀번호 : ")
            i+=1
        else:
            print("로그인 되었습니다!")
            break
            

    else:
        if PW != password:
            print("로그인 실패! 횟수초과!")
            break            
            
        else:
            print("로그인 되었습니다!")
            break
        

    
       
    

