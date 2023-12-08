
num_int = int(input('Enter the number:'))
num_str = str(num_int)
print(type(num_str))

num_str = input('Entet the string:')
num_int = int(num_str)
print(type(num_int))

def check_value(input_value):
    if input_value > 100: 
        print("CONGRATS")  
    print("HAVE A NICE DAY")  
user_input = int(input("Enter a number: "))  
check_value(user_input)

def add_marks(m1, m2):
    m1 += 10
    m2 += 20
    return m1, m2  
M1 = int(input("Enter M1: "))
M2 = int(input("Enter M2: "))
s=add_marks(M1, M2)
print("Orginal marks:",M1,M2)
print("Added marks:",s)

def display_product_info():
    product_code = input("Enter the product code: ")
    product_name = input("Enter the product name: ")
    price = input("Enter the price: ")
    print("The {} with {} is sold as Rs. {}".format(product_name, product_code, price))
# Call the function to execute
display_product_info()


def display_friend_name():
    letter = input("Enter the first letter of your friend's name: ")
    if letter.lower() == 'b':
        print("Bastin")
    elif letter.lower() == 'g':
        print("George")
    elif letter.lower() == 'p':
        print("Peo")
    else:
        print("Try another letter")
# Call the function to execute
display_friend_name()

  
def calculate_square():
    for i in range(5):
        value = float(input(f"Enter value {i+1}: "))
        square = value ** 2
        print(f"The square of {value} is: {square}")
# Call the function to execute
calculate_square()


def check_characters():
    my_string = "JOSEPH"
    if 'S' in my_string:
        print("The character 'S' exists in the string.")
    else:
        print("The character 'S' does not exist in the string.")
    if 'T' in my_string:
        print("The character 'T' exists in the string.")
    else:
        print("The character 'T' does not exist in the string.")
# Call the function to execute
check_characters()


def find_largest():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = float(input("Enter the third number: "))
    largest_number = max(x, y, z)
    print("The largest number:",largest_number)
# Call the function to execute
find_largest()

def count_values_greater_than_10():
    count = 0
    for i  in range(5):
        value = float(input("Enter a value: "))
        if value > 10:
            count += 1
    print("The number of values greater than 10 is:", count)
# Call the function to execute
count_values_greater_than_10()

def print_full_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + " " + last_name
    print("Your full name is:", full_name)
# Call the function to execute
print_full_name()


def check_divisibility():
    num = int(input("Enter a number: "))
    if num % 2 == 0 and num % 3 == 0:
        print(f"The number {num} is divisible by both 2 and 3.")
    else:
        print(f"The number {num} is not divisible by both 2 and 3.")
# Call the function to check divisibility for user input
check_divisibility()

def sum_even_numbers():
    start = 100
    end = 200
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num
    print(f"The sum of even numbers between {start} and {end} is: {total_sum}")
# Call the function to calculate the sum of even numbers
sum_even_numbers()


def  sum_even_numbers():
    total_sum = 0
    for num in range(100, 201, 2):
        total_sum += num
    return total_sum
# Call the function to calculate the sum of even numbers
result = sum_even_numbers()
print("The sum of even numbers between 100 and 200 is:", result)
sum_even_numbers()
