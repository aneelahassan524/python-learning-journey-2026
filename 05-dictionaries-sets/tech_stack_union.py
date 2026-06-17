python_dev = {}
p1 = input("Enter Python skill 1:")
p2 = input("Enter Python skill 2:")
p3 = input("Enter Python skill 3: ")
python_dev = {p1,p2,p3}
print(f"First Set:{python_dev}")
web_dev = {}
w1 = input("Enter web skill 1:")
w2 = input("Enter web skill 2:")
w3 = input("Enter web skill 3: ")
web_dev = {w1,w2,w3}
print(f"Second Set:{web_dev}")
print(f"Unique technologies:{python_dev.union(web_dev)}")