import os

folder = os.getcwd()
print(f"Current Folder: {folder}")

data_folder = "data"

if os.path.exists(data_folder):
    print("Data folder exists.")
else:
    os.mkdir(data_folder)
    print("Data folder created.")

print(f"Items inside data folder: {os.listdir(data_folder)}")

print(f"Before:{os.getcwd()}")

os.chdir("data")

print(f"After:{os.getcwd()}")

print(f"New Folder:{os.getcwd()}")
print(f"Items inside folder: {os.listdir()}")

print(f"Back to:{os.getcwd()}")

structure = "data_structures/reports/2026"

if not os.path.exists(structure):
    os.makedirs(structure)
    print("Folder created.")
else:
    print("Folder already exists.")

print(os.path.isdir(structure))


structure = "data_structures/reports/2026"

file_path = os.path.join(structure, "report.txt")

with open(file_path, "w") as file:
    file.write("Company Annual Report")

os.remove(file_path)
os.rmdir(structure)
 
