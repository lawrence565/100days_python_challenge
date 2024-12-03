def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return  f"{f_name} {l_name}"

f_name = input("First name: ")
l_name = input("Last name: ")
print(format_name(f_name, l_name))