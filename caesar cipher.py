def encrypt(password):

    key = 'abcdefghijklmnopqrstuvwxyz'
    answer1=""
    


    for st in password:

        if st == "y":
            answer1 += "a"


        elif st == "z":
            answer1 += "b"

        else:
            answer1 += key[key.index(st)+2]
    return answer1
        
        
def decrypt(password):

    key = 'abcdefghijklmnopqrstuvwxyz'
    answer2=""
    
    for st in password:

        if st == "a":
            answer2 += "y"


        elif st == "b":
            answer2 += "z"

        else:
            answer2 += key[key.index(st)-2]
    return answer2

   



with open("password.txt","w") as file1:


    for i in range(3):
        pw=input("문자열 입력 (대문자, 빈칸, 특수기호 불가) : ")
        file1.write("%s\n" %pw)

    

    
    print("암호 저장 완료!!!")
    print()


        
      

with open('password.txt','r') as file2:

    for i in range(3):
        line=file2.readline()
        word=line.split()


        for j in range(len(word)):
            print("암호 : ", end=" ")
            print(encrypt(word[j]))
            print("해독 : ", end=" ")
            print(decrypt(encrypt(word[j])))
