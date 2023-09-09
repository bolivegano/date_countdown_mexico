from datetime import date
from termcolor import colored

today = date.today()

arrival_date = date(2023, 9, 8)
exit_date = date(2024, 3, 5)

days_here = today - arrival_date
delta = exit_date - today

print(f"\n\nYou arrived on {colored(arrival_date.strftime('%A %B %d, %Y'), 'green')}.")
print(f"You have been here for {colored(days_here.days + 1, 'blue')} days.")
print(f"You have {colored(delta.days, 'yellow')} days remaining.")
print(f"Your latest exit date is {colored(exit_date.strftime('%A %B %d, %Y'), 'red')}\n\n.")


