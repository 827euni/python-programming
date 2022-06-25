def binary(n):
    global count
    count+=1
    if n>=1:
        binary(n//2)
        bin = n%2
        list.append(bin)
        return list


    


            
while True:

    list=[]
    count = 0

    num=int(input("양의 정수 입력(음수입력시 종료) : "))



    if num < 0:
            break

    else:  
            print(f"{num}의 이진수 : ", end = "")
            for i in range(len(binary(num))):
                print(list[i], end = "")
            
            print("   binary() 함수 반복횟수 : ", count)
            print()
  

