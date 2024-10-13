import os

def create_args_directory():

    if not os.path.exists("args"):
        os.mkdir("args")
    return "args"

def sum_args(*args):

    total = 0
    for arg in args:
        total += arg
    return total

# example usage:
args_dir = create_args_directory()
print(f"Created directory: {args_dir}")

print(sum_args(1, 2, 3))  # Output: 6
print(sum_args(10, 20, 30, 40))  # Output: 100
print(sum_args())  # Output: 0
print(sum_args(5.5, 4.5, -10))  # Output: 0