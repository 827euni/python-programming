blood_list=[]
num=0


while num < 10:
    blood=input("헌혈할 혈액형(a, b, ab, o) : ")
    if blood == "a":
        blood_list.append(blood)
        num+=1
        
    elif blood == "a":
        blood_list.append(blood)
        num+=1        

    elif blood == "b":
        blood_list.append(blood)
        num+=1
    elif blood == "ab":
        blood_list.append(blood)
        num+=1

    elif blood == "o":
        blood_list.append(blood)
        num+=1  
        
    else:
        print("혈액형 오류!!!")
        
print(" ")
print("저장된 혈액형")

for i in range(0,10):
    print(blood_list[i], ' ', end=' ')

print(" ")
print("A  혈액형 수 : ", blood_list.count("a"))
print("B  혈액형 수 : ", blood_list.count("b"))
print("AB 혈액형 수 : ", blood_list.count("ab"))
print("O  혈액형 수 : ", blood_list.count("o"))

    
