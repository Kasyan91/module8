from datetime import datetime, timedelta


def get_days_from_today(date):
    current_date=datetime.today()
    date_list=list()
    date_list=date.split('-')
    new_date=datetime(year=int(date_list[0]),month=int(date_list[1]),day=int(date_list[2]))
    differerence=new_date-current_date
    return differerence.days     

print(get_days_from_today('2020-09-01'))






