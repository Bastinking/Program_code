"""This python program for any ten string
functions asking input from user """
print('\tSTRING OPERATION LIST')
print('-------------------------')
print('1.Uppercase')
print('2.Lowercase')
print('3.Swapcase')
print('4.Reverse')
print('5.Length')
print('6.Titlecase')
print('7.Check alphabetic or not')
print('8.Check lowercase or not')
print('9.Check Uppercase or not')
print('10.Check Numeric or not')
print('-------------------------')
while True:
    a=int(input('Enter your choice:'))
    s=input('Enter the string:')
    if a==1:
        print(s.upper())
    elif a==2:
        print(s.lower())
    elif a==3:
        print(s.swapcase())
    elif a==4:
        print(s[::-1])
    elif a==5:
        print(len(s))
    elif a==6:
        print(s.title())
    elif a==7:
        print(s.isalpha())
    elif a==8:
        print(s.islower())
    elif a==9:
        print(s.isupper())
    elif a==10:
        print(s.isnumeric())
    else:
        print("Enter the valid option")#Enter 1 t0 10 digit allowed
    rep=input('Do you want to continue?(Yes/No)')
    if rep.lower()!='yes':
        break