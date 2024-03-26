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
    

# Main routine starts here...
while True:
    file_type = get_file_type()

    # if user chose 'i', ask if they want an image / integer
    if file_type == "i":

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"


    print(f"You have chosen {file_type} file type.")

    if file_type == "xxx":
        break
