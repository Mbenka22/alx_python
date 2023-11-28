import random
number = random.randint(-10000, 10000)

last_digit=abs(number)%10
print(f"last digitof{number}is {last_digit}")


print(f"The number is:{number}")
if number>0:
    print("the number is positive")
elif number<0:
    print("the number is negative")
else:
    print("the number is zero")

number=random.randint(-10000,10000)
output_string=f"is{number}"
print(output_string)

number1=-10000
number2=10000

def check_last_digit(number):
    last_digit=abs(number)%10
    if last_digit>5:
      return f"is{last_digit}and is greater than 5"
    else:
        return f"is{last_digit}and is not greater than 5"
    
    output1=check_last_digit(number1)
    output2=check_last_digit(number2)

    print(output1)
    print(output2)#


number1=-10000
number2=10000  
def get_last_digit(number):
    #convert the number to a string and extract the last digit
    return str(number)[-1]
last_digit1=get_last_digit(number1)
last_digit2=get_last_digit(number2)

if last_digit1=='0':
    print(f"is{last_digit1} and is 0")
else:
    print(f"is{last_digit1}")
if last_digit2=='0':
    print(f"is{last_digit2}and is 0")
else:
    print(f"is{last_digit2}")

number=random.randint(-10000,10000)
last_digit=abs(number)%10  #getting the last digit using modulo
if last_digit!=0 and last_digit<6:
    print(f"the last digit of{number}is {last_digit}and is less than 6 and not 0")
else:
    print(f"the last digit of {number}is last digit")    