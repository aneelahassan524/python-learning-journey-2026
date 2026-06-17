A = {}
p1 = input("Enter Python skill 1:")
p2 = input("Enter Python skill 2:")
p3 = input("Enter Python skill 3: ")
A = {p1,p2,p3}
print(f"First Set:{A}")
B = {}
w1 = input("Enter web skill 1:")
w2 = input("Enter web skill 2:")
w3 = input("Enter web skill 3: ")
B = {w1,w2,w3}
print(f"Second Set:{B}")
print(f"Skills Python developer has but Web developer doesn't:{A.difference(B)}")