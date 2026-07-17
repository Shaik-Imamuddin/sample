# n=int(input())
# rev=0
# while n!=0:
#     rev=rev*10+n%10 
#     n//=10 
# print(rev)


for i in range(1,10+1):
    if i==5:
        pass
    print(i,end=" ")
print("Hello")

# c=0
# while n!=0:
#     c+=1
#     n//=10
# print(c)

# sum=0
# while n!=0:
#     sum+=n%10
#     n//=10
# print(sum)




# range(start,stop,step)
# for i in range():
    # STATEMENT block

# while condition:
#     statment block


# match n:
#     case i if i>=90 and i<=100:
#         print("A")
#     case i if i>=75 and i<90:
#         print("B")
#     case i if i>=50 and i<75:
#         print("C")
#     case i if i>=35 and i<50:
#         print("D")
#     case _:
#         print("F")


# match(n):
#     case i if i in range(90,101):
#         print("A")
#     case i if i in range(75,90):
#         print("B")
#     case i if i in range(60,75):
#         print("C")
#     case i if i in range(35,60):
#         print("D")
#     case _:
#         print("F")



# match(n):
#     case 12|1|2|3:
#         print("Winter")
#     case 4|5|6|7:
#         print("Summer")
#     case 8|9|10|11:
#         print("Rainy")
#     case _:
#         print("No season")

# match(n):
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("No day")













'''
control structures


101
001
---
001



match(condtion):
    case-1:
        statement block-1
    ..  ..  ..  ..  ..  
    ..  ..  ..  ..  ..  
    ..  ..  ..  ..  ..  
    case-n:
        statement block-n
    case _:
        default case


Syntax:
    if conidition-1:
        statement block-1
    elif conidition-2:
        statement block-2
    ...   ...       ...
    ...   ...       ...
    ...   ...       ...
    elif conidition-n:
        statement block-n
    else:
        flase statement block;
        

        


    if conidition-1:
        if conidition-2:
            statement block-1
        elif condition-3:
            statement block-2
        else:
            statement block-3
    else:
        statement block-4





    conditional
        simple if
        if else
        if elif else
        if elif ladder
        nested if
        match

    looping
        for
        while
    
    un-conditional
        break
        continue
        pass


'''