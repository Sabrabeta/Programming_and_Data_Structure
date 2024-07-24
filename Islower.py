def islower(c):
    # Get the ASCII value of the character
    ascii_value = ord(c)
    
    # Check if the ASCII value is within the range of lowercase letters
    if 97 <= ascii_value <= 122:
        return True
    else:
        return False

# Test cood
print(islower('a'))  # Should return True
print(islower('A'))  # Should return False
