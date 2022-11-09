import utils

if __name__ == '__main__':
    while True:
        user_input = input("Enter a number: ")
        if user_input == 'q':
            exit("Bye!")
        if not user_input.isdigit():
            exit("Input is not a digit...")
        print("Given number least prime number greater than him is:", utils.process_item(int(user_input)))
