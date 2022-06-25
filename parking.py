
import datetime

today=datetime.datetime.now()
day=today.day


number=int(input("차량번호 입력 : "))



if number%2==0: 
    if day%2==0: #짝수번호이면서 짝수날 = 주차가능
        print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 입니다.")
        print(f"오늘은 {today.day}일 짝수날로 {number}번호는 주차가능합니다.")
    else: #짝수번호이면서 홀수날 = 주차불가능
        print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 입니다.")
        print(f"오늘은 {today.day}일 홀수날로 {number}번호는 주차가 불가능합니다. ")


else:
    if day%2==0: #홀수번호이면서 짝수날 = 주차불가능
        print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 입니다.")
        print(f"오늘은 {today.day}일 짝수날로 {number}번호는 주차가 불가능합니다.")
    else: #홀수번호이면서 홀수날 = 주차가능
        print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 입니다.")
        print(f"오늘은 {today.day}일 홀수날로 {number}번호는 주차가능합니다. ")
        
        
