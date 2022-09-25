from datetime import date, timedelta

month=2
year=2021


def get_days_in_month(month, year):
    if month==12:
        new_date=date(year=int(year+1),month=1,day=1)
    elif month in range(13) :
        new_date=date(year=int(year),month=int(month+1),day=1)
    else:
        return('not correct month or year')
    diference=timedelta(days=1)
    search_date=new_date-diference
    return search_date.strftime('%d')
print(get_days_in_month(month, year))

