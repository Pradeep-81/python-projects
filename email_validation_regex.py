import re

email = input("Enter email:")
email_condition = "^[a-z]+[\._]?[a-z0-9]+[@][a-z]+[.]+[a-z]{2,3}$"

if re.search(email_condition, email):
    print("Valid Email.")
else:
    print("Invalid email.")
