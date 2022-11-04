import utils

if __name__ == '__main__':
    while True:
        user_input = input("Enter a number: ")
        if user_input == 'q':
            exit(1)
        if not user_input.isdigit():
            exit(2)
        print("Given number least prime number greater than him is: " + utils.process_item(int(user_input)))
