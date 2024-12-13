def percentage(placeholder):
    while True: 
        try:
            name = int(input(placeholder))  
            return name  
        except ValueError:  
            print("Please enter a valid number.")

def calculate(M2, M3, M4, M5):
    total = M2 + M3 + M4 + M5
    percentage = (total / 400) * 100
    return percentage

print("Welcome to the percentage calculator")

M2 = percentage("Enter your OOP marks\n")
M3 = percentage("Enter your DLD marks\n")
M4 = percentage("Enter your DSA marks\n")
M5 = percentage("Enter your CS marks\n")

result = calculate(M2, M3, M4, M5)
print("Your percentage is", result)

if result >= 80:
    print("Your grade is A+")
elif result >= 60:
    print("Your grade is A")
elif result >= 40:
    print("Your grade is B")
elif result >= 30:
    print("Your grade is C") 
else:
    print("You have failed.")    
