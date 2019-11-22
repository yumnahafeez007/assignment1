#Write a Python program to display the current date and time.

from datetime import datetime

now = datetime.now()
 
print("now =", now)
# dd/mm/YY H:M:S
date_time_format = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", date_time_format)	