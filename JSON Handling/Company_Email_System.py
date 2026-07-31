emails = [
    "Ali@company.com",
    "Sara@company.com",
    "Ali@company.com",
    "Ahmed@company.com",
    "Bilal@company.com",
    "Sara@company.com"
]
unique  = {
    email.lower()
    for email in emails
}
print(unique)