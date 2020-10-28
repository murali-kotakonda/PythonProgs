print("************************program to print yesterday, today, tomorrow.**********************************")
# n program to print yesterday, today, tomorrow.
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
dt = today - datetime.timedelta(5)

print('Yesterday : ', yesterday)
print('Today : ', today)
print('Tomorrow : ', tomorrow)
print('5 days before Current Date :', dt)

print("************************print next 5 days starting from today.**********************************")