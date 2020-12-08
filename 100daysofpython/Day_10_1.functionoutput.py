# Functions with Outputs

def format_name(f_name, l_name):
    proc_f_name = f_name.title()
    proc_l_name = l_name.title()
    return f"{proc_f_name} {proc_l_name}"

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

name = format_name(f_name,l_name)
print(name)