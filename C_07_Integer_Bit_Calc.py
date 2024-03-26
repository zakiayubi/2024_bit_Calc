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


# Calculates number of bits needed to represent an integer
def integer_calc():
    # Ask the user to enter an integer (>= 0)
    integer = int_check("Integer", 0)

    # Convert the integer to a binary string and work out the number of bits needed
    raw_binary = bin(integer)

    # Remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = f"{integer} in binary is {binary}. We need {num_bits} to represent it."

    return answer

# Main routine starts here...
integer_ans = integer_calc()
print(integer_ans)
