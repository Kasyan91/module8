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
    final_list=list()
    monday=[]
    tuesday=[]
    wednesday=[]
    thursday=[]
    friday=[]
    for emp in users:
        if emp['birthday']<current_day or emp['birthday']>(current_day+timedelta(days=7)):
            pass
        elif emp['birthday'].strftime('%A') in ('Saturday','Sunday','Monday'):
            monday.append(emp['name'])
        elif emp['birthday'].strftime('%A') in ('Tuesday'):
            tuesday.append(emp['name'])
        elif emp['birthday'].strftime('%A') in ('Wednesday'):
            wednesday.append(emp['name'])
        elif emp['birthday'].strftime('%A') in ('Thursday'):
            thursday.append(emp['name'])
        elif emp['birthday'].strftime('%A') in ('Friday'):
            friday.append(emp['name'])  
    if len(monday)>=1:
        monday_str='Monday: '+', '.join(monday)
        final_list.append(monday_str)
    if len(tuesday)>=1:
        tuesday_str='Tuesday: '+', '.join(tuesday)
        final_list.append(tuesday_str)
    if len(wednesday)>=1:
        wednesday_str='Wednesday: '+', '.join(wednesday)
        final_list.append(wednesday_str)
    if len(thursday)>=1:
        thursday_str='Thursday: '+', '.join(thursday)
        final_list.append(thursday_str)
    if len(friday)>=1:
        friday_str='Friday: '+', '.join(friday)
        final_list.append(friday_str)
    return final_list

#перевірка функції   
print(get_birthdays_per_week(emp_list))