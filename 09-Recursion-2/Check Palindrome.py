def check(n):
    if len(n) <= 1:
        return True
    return (n[0] == n[-1]) and check(n[1:-1])
c = check("radar")
print(f"Is Palindrome: {c}")