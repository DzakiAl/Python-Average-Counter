def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

print("Welcome to Python Average Counter")
print("1. Start")
print("2. Exit")
choice = int(input("Input your choice: "))

if choice == 1 :
    input = (input("Enter a list numbers seperate by spaces: "))
    numbers_list = [float(num) for num in input.split()]

    result = calculate_average(numbers_list)

    print("The Average is", result)
elif choice == 2 :
    print("Exiting...........")
else :
    print("Enter correct number")