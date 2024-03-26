# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")



# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
- Say File Type
- Enter info about the file
- Then you will receive the amount of bits you need
- Enter the next file type
    ''')

# asks user for file type (integer / image / text / xxx)
def get_file_type():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "i" or response == "xxx":
            return response
        
        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"
        
        # check if it's an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"
        
        # check if it's a text file
        elif response in ['text', 'txt', 't']:
            return "text"
        
        # if the response is invalid output an error message
        else:
            print("Please enter a valid file type.")
    
# Ask user for widht and loop untill they enter a number that is more than zero
# Enter a number that is more than zero
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
def image_calc():
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)
    
    # Calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} * {height} = {num_pixels}" 
              f"\nNumber of bits: {num_pixels} * 24 = {num_bits}")

    return answer

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

# Calculates number of bits needed to represent text in ascii
def calc_text_bits():
    
    #Get text from user
    response = input("Enter some text: ")

    # Calculate bits needed to represent
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"\n{response} has {num_chars} characters."
              f"\nWe need {num_chars} × 8 bits to represent it." 
              f"\nwhich is {num_bits} bits.")
    
    return answer


# Main routine starts here...
            
# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")

if want_instructions == "":
    instructions()            


while True:
    file_type = get_file_type()

    if file_type == "xxx":
        break

    # if user chose 'i', ask if they want an image / integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"


    if file_type == "image":
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print (text_ans)
