def cut_string(some_str: str):
    if len(some_str) <= 2:
        print("NOt enoughth chars ", end='')
        return ''
    return "result is " + some_str[:2] + some_str[-2:]


def check_operators(phone_number):
    if phone_number[:3] == '050' or phone_number[:3] == '067':
        return True
    return False


def valid_phone_number():
    while True:
        phone_number = input("Write phone number: ")
        if phone_number and phone_number.isdigit() and len(phone_number) == 10 and check_operators(phone_number):
            print("Thanks for your answer! ")
            return phone_number

        else:
            print("Wrong format! Try again. ")
            continue


def yes(answer: str):
    if answer.isalpha() and len(answer) == 1:
        if answer == 'Y' or answer == 'y' or answer == 'Д' or answer == 'д':
            return True
    return False


if __name__ == '__main__':
    """
    Task 1
    
    String manipulation
    
    Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. 
    If the string length is less than 2, return instead of the empty string.
    
    Sample String: 'helloworld'
    
    Expected Result : 'held'
    
    Sample String: 'my'
    
    Expected Result : 'mymy'
    
    Sample String: ' x'
    
    Expected Result: Empty String
    
    Tips:
    
    Use built-in function len() on an input string
    Use positive indexing to get the first characters of a string and negative indexing to get the last characters
    """
    print(" Task 1 ".center(40, '*'))
    print(cut_string(input("Write a some string: ")))

    """
    Task 2
    
    The valid phone number program.
    
    Make a program that checks if a string is in the right format for a phone number. 
    The program should check that the string contains only numerical characters and is only 10 characters long. 
    Print a suitable message depending on the outcome of the string evaluation.
    """
    print(" Task 2 ".center(40, '*'))
    valid_phone_number()

    """
    Task 3

    The name check.
    
    Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
    The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
    if your input is “Anton” and the stored name is “anton”, it should return True.
    """
    print(" Task 3 ".center(40, '*'))

    my_name = "alex"
    while my_name != (input("Write your name: ")).lower():
        print("Not correct! Try again! ")
    else:
        print("Correct! ")

    print(" Task * ".center(40, '*'))
    delivery = ('NP', 'UkrPoshta', 'Self')
    order_info = {"name": "Nadya", "phone_number": "0508573631", "order": {"fruits": True, "vegetables": False},
                  "delivery": delivery[0]}
    while True:
        print(f"Ask: Is his name {order_info.get('name')}?")

        if yes(input("Is it a correct name?")):
            pass
        else:
            order_info.update({'name': input("Ask name and write.")})
            print(order_info)
        if not yes(input("Ask: Is it convenient for you to say?")):
            print("Say sorry and Good bye")
            break
        print(f"Ask: Is it your phone number {order_info.get('phone_number')}?")
        if yes(input("Is it a correct?")):
            pass
        else:
            print("Ask a correct number in special format")
            order_info.update({"phone_number": valid_phone_number()})

        print(f"Ask: Is it him/his order{order_info.get('order')}")
        if not yes(input("Is it a correct?")):
            print("Ask: Is would like to buy some Fruits")
            if yes(input("is it?")):
                order_info['order']['fruits'] = True
            else:
                order_info['order']['fruits'] = False

            print("Ask: Is would like to buy some Vegetables")
            if yes(input("is it?")):
                order_info['order']['vegetables'] = True
            else:
                order_info['order']['vegetables'] = False
        print(f"Your order: \n{order_info}")
        break
