def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if not y:
        return "Division by Zero"

    return x / y


if __name__ == "__main__":
    # x = input("Enter the 1st number")
    # y = input("Enter the 2nd number")
    # operator = input("Enter +, -, or *")
    # if operator == "+":
    #     z = Addition(x, y)
    # elif operator == "-":
    #     z = Subtraction(x, y)
    # elif operator == "/":
    #     z = Multiplication(x, y)
    # print("The answer is ", z)
    print("1 + 2 : {}".format(addition(1, 2)))
    print("1 - 2 : {}".format(subtraction(1, 2)))
    print("1 * 2 : {}".format(multiplication(1, 2)))
    print("1 / 2 : {}".format(division(1, 2)))
    print("1 / 0 : {}".format(division(1, 0)))
