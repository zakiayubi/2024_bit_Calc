# Ask user for widht and loop untill they enter a number that is more than zero

def int_check (question, low):


    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # asking the user far a number
            response = int(input(question))

            # checking that the num is > 0
            if response >= low:
                return response
            else:
                print("error")

        except ValueError:
            print(error)


# Main Routine Goes Here
for item in range(0, 2):
    integer = int_check("Integer: ", 0)
    print(integer)

print()

for item in range(0, 2):
    width = int_check("width: ", 1)
    print(width)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)
