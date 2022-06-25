total=0
def total(student):
    total=sum(student[1:4])
    student.append(total)
    return total


def ave(student):
    total=sum(student[1:4])
    ave=(total/3)
    student.append(ave)
    return ave
def grade(student):
    total=sum(student[1:4])
    ave=(total/3)

    if ave>=90:
        grade="A"

    elif ave>=80:
        grade="B"

    elif ave>=70:
        grade="C"

    elif ave>=60:
        grade="D"
    else:
        grade="F"
    student.append(grade)
    return grade

def output(student):
    print("{}: 국어:{} 영어:{} 수학:{} 총점:{} 평균:{:.2f} 학점:{}".format(*student))
def max_student(*student):
    name = 0
    max=0

    for st in student:
        if max<total(st):
            name=st
        max=total(st)
    return name