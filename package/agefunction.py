import datetime

def age():
    # d= int(input('Enter day'))
    # m= int(input('Enter month'))
    # y= int(input('Enter year'))

    y,m,d = map(int,input('Enter your date of birth as  ''year,month,date').split(','))
    k = datetime.date(y,m,d)
    print('your age = ',k)
    x = datetime.date.today()
    print('current date = ',x)
    age = x.year - k.year
    print('current age = ', age)
    


