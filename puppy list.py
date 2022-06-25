list=[]


for i in range(3):

    name = input("강아지 이름 : ")
    age=int(input("강아지 나이 : "))
    kind=input("강아지 종류 : ")

    dic={}
    dic[i] ={'name':name , 'age':age , 'kind':kind}
    list.append(dic[i])


print("리스트 내용")
print("0번째 :" , list[0])
print("1번째 :" , list[1])
print("2번째 :" , list[2])


print("나이가 3살 이상인 강아지")


for st in list:
    if st['age']>=3:
        print(st)



