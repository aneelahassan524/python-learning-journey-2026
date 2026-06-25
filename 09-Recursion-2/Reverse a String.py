def reverse_string(n):
    if(n==""):
        return ""
    return reverse_string(n[1:]) + n[0]
r = reverse_string("5678")
print(f"Reverse of a string is:{r}")