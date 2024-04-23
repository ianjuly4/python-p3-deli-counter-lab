katz_deli = []

def line(katz_deli):
    if len(katz_deli) >= 1:
        line_status = "The line is currently:"
        for index, person in enumerate(katz_deli, start=1):
            line_status += f" {index}. {person}"
        print(line_status)
    elif len(katz_deli) == 0:
        print("The line is currently empty.")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    index = len(katz_deli)
    print(f'Welcome, {name}. You are number {index} in line.')
    
def now_serving(katz_deli):
    if len(katz_deli) >= 1:
        customer = katz_deli.pop(0)
        print(f'Currently serving {customer}.')
    else:
        print("There is nobody waiting to be served!")