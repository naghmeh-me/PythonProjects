#"Write a function that takes a variable number of arguments (*arga), and returns both the sum of all arguments and the total number of arguments.

def count_sum(*args):
    count_ = len(args)
    sum_ = sum(args)

    return f"Count numbers = {count_}\nSum numbers = {sum_}"


print("For exit from the program enter 0.")

while True:
    try:
        numbers = input("Enter numbers separated by space: ")

        if numbers == "0":
            break

        numbers = list(map(int, numbers.split()))

    except ValueError:
        print("Error! Enter only numbers.")
        continue

    else:
        print(count_sum(*numbers))
