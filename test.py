import datetime



date_format = "%d/%m/%Y"

date1 = datetime.strptime("08/03/2010", date_format)
date2 = datetime.strptime("01/05/2010", date_format)

difference = date2 - date1

print(difference.days)
