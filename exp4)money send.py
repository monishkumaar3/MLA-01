def is_possible_mapping(arr, S):
    mapping = {}  # Dictionary to store mappings of characters to digits
    used_digits = set()  # Set to keep track of used digits

    # Function to encode a string using the given mapping
    def encode_string(string):
        num = 0
        for char in string:
            num = num * 10 + mapping[char]
        return num

    # Recursive function to backtrack and find the mapping
    def backtrack(index):
        if index == len(S):
            # Check if encoding the strings results in the number formed by S
            return sum(encode_string(string) for string in arr) == int(S)

        char = S[index]
        # If the character is already mapped, continue to the next character
        if char in mapping:
            return backtrack(index + 1)

        # Try mapping each digit to the character
        for digit in range(10):
            if digit not in used_digits:
                mapping[char] = digit
                used_digits.add(digit)
                if backtrack(index + 1):
                    return True
                # Backtrack
                del mapping[char]
                used_digits.remove(digit)

        return False

    return backtrack(0)


# Test case
arr = ["SEND", "MORE"]
S = "MONEY"
print("Output:", "Yes" if is_possible_mapping(arr, S) else "No")
