import datetime
x = datetime.datetime.now()

print(f"{x.strftime("%H")} {x.strftime("%M")} {x.strftime("%S")}")