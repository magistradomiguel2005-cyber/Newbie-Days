import datetime, bday_messages

date1 = datetime.date.today()

date2 = datetime.date(2027,1,20)

days_away = date2 - date1

if date1 == date2:
    print(bday_messages.message)
else:
    print('My next birthday is ' ,days_away, ' days away!')