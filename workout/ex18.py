def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

def print_two_again(arg1, arg2)-> str:
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1)->str:
    print(f"arg1 : {arg1}")

def print_none()-> None:
    print("I got nothin'.")

print_two('zed', 'shaw')
print_two_again('zed', 'shaw')
print_one('first')
print_none()
