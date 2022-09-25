#add to github
from datetime import datetime, timedelta #import package datetime
#list for test
emp_list=[{'name':'Michael','birthday':datetime(year=2022, month=9,day=25)},
{'name':'Nastya','birthday':datetime(year=2022, month=9,day=28)},
{'name':'Sasha','birthday':datetime(year=2022, month=9,day=25)},
{'name':'Yulia','birthday':datetime(year=2022, month=9,day=26)},
{'name':'Orel','birthday':datetime(year=2022, month=9,day=27)},
{'name':'Anton','birthday':datetime(year=2022, month=9,day=28)},
{'name':'Serg','birthday':datetime(year=2022, month=10,day=1)},
{'name':'Oksana','birthday':datetime(year=2022, month=9,day=30)},]

def get_birthdays_per_week(users):
    current_day=datetime.today()
    birthsdays={"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
    week_days={1:"Monday",2:"Tuesday", 3:"Wednesday",4:"Thursday",5:"Friday"}
    for emp in users:
        if emp['birthday']<current_day or emp['birthday']>(current_day+timedelta(days=7)):
            pass
        else :
            birthday_day=emp['birthday'].weekday()
            day=(week_days.get(birthday_day,"Friday"))
            name=emp['name']
            birthsdays[day].append(name)
    for day,name in birthsdays.items():
        if name:
            print(f'{day}: {",".join(birthsdays[day])}')

#перевірка функції   
get_birthdays_per_week(emp_list)



