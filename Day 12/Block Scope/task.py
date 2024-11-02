my_global_var = 1

def my_function():
    my_local_var = 2
    print(my_local_var)

for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

my_function()