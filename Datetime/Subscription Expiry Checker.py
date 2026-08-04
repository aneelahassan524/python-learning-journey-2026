#You are developing software for an online learning platform.
# Every student buys a subscription.
# The software should calculate how many days are left until the subscription expires.

from datetime import datetime

print("=========== SUBSCRIPTION DETAILS ===========")
current_date = datetime.now()
expiry_date = datetime(2026, 12, 31)
print(f"Current Date: {current_date.strftime('%d %B %Y')}")
print(f"Expiry Date: {expiry_date.strftime('%d %B %Y')}")
difference = expiry_date-current_date
print(f"Remaining Days: {difference.days}")

if(difference.days<=30):
    print("Your subscription will expire soon.")
else:
    print("Your subscription is active.")