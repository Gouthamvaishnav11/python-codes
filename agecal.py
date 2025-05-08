from datetime import datetime

def age_calculator(birth_date):
    today=datetime.today()
    age=today.year - birth_date.year

    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1  # Birthday hasn't occurred yet this year
    
    return age

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d")

age = age_calculator(dob)
print(f"Your age is: {age} years")

