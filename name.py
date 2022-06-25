mylist=[]


while 1:
    
    

    print("*******************")
    print("1. 이름 추가")
    print("2. 이름 삭제")
    print("3. 이름 수정")
    print("4. 종료")
    
    human_select=int(input("메뉴 선택 : "))

                 

    if human_select == 1:
                     name_add=input("이름 : ")
                 

                     if name_add in mylist:
                         print("이미 있는 이름")
                         print(" ")
                     
                     else:
                         mylist.append(name_add)

                         print(mylist)
                         print(" ")
                        
                         continue
                
                 
                 
                
    elif human_select == 2:
                     name_delete=input("이름 : ")
                 

                     if name_delete in mylist:
                         mylist.remove(name_delete)
                         print(mylist)
                         print(" ")
                         
                         continue
                     
                     else:
                        print("해당 이름 없음")
                        print(" ")

                        
    elif human_select == 3:
        name_edit=input("이름 : ")
        name_editNEW=input("새이름 : ")
        if name_edit in mylist:
            num_edit=mylist.index(name_edit)
            mylist[num_edit]=name_editNEW
            print(mylist)
            print("")
            continue

        else:
            print("해당 이름 없음")
            print(" ")

    elif human_select == 4:
        break

    else:
        print("올바른 번호를 선택해주세요.")
        print(" ")

