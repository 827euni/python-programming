def gcd(num1, num2, *nums):

    num=[num1, num2]

    for st in nums:
        num.append(st)

    small=min(num)
    result=0

    for i in range(1,small+1):
    
        for j in range(1,len(num)):
            if len(num)==2:
                if (num[1-j]%i==0) and (num[2-j]%i==0):
                    stack.append(i)
                    result=stack[-1]
                
                    
                

            elif len(num)==3:
                if (num[1-j]%i==0) and (num[2-j]%i==0) and (num[3-j]%i==0):
                    stack.append(i)
                    result=stack[-1]
                

            elif len(num)==4:
                if (num[1-j]%i==0) and (num[2-j]%i==0) and (num[3-j]%i==0) and (num[4-j]%i==0):
                    stack.append(i)
                    result=stack[-1]
                

            else:
                break

    return result
            
                
 

          


                    
                    
    

            
            


        









stack =[]

a=int(input("정수1 입력 : "))
b=int(input("정수2 입력 : "))
c=int(input("정수3 입력 : "))
d=int(input("정수4 입력 : "))
print(f"{a}, {b}의 최대공약수 : ", gcd(a,b))
print(f"{a}, {b}, {c}의 최대공약수 : ", gcd(a,b,c))
print(f"{a}, {b}, {c}, {d}의 최대공약수 : ", gcd(a,b,c,d))
