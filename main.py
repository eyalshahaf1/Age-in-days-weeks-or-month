
age = input("What is your current age?  ")

age_as_int = int(age)
age = 90 - age_as_int

days = age * 365
weeks = age * 52
months  = age * 12

message = f"You have {days} days,{weeks} weeks and {months} months left"

print(message)





