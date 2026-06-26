def count_uppercase(s):
    if s == "":
        return 0
    if 'A' <= s[0] <= 'Z':
        return 1 + count_uppercase(s[1:])
    return count_uppercase(s[1:])
result = count_uppercase("PyTHon")
print(f"Uppercase Letters: {result}")