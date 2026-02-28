import datetime

x = datetime.datetime(2018, 6, 1, 17, 17, 35)
y = datetime.datetime(2018, 6, 1, 17, 17, 38)
print(int(x.strftime("%S"))-int(y.strftime("%S")))
