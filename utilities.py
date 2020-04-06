def check_name(name):
    name_without_space = name.replace(' ', '')
    if name_without_space.isalpha():
        return True
    else:
        return False


def check_if_valid(sympt):
    if sympt == "1" or sympt == "2":
        return True
    else:
     return False

def check_number(temp):
    temp_without_a_dot = temp.replace(".", "")
    if temp_without_a_dot.isdigit():
        return True
    else:
        return False

def check_fever(temp):
    if temp >= str(37.6):
        return True
    else:
        return False

