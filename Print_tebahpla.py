def print_alphabet():
    # Use a single print statement with string formatting
    print(''.join(
        chr(i).lower() if (26 - (i - 65)) % 2 == 0 else chr(i).upper()
        for i in range(90, 64, -1)
    ), end='')

# Call the function to execute
print_alphabet()
