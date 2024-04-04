
import datetime

# Get the current day of the week (Monday is 0 and Sunday is 6)
current_day = datetime.datetime.now().weekday()

# Check if it's a weekday (Monday to Friday)
if current_day<= current_day <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
