patients = ["Ali","Sara","Ahmed","Bilal","Ayesha"]
it = iter(patients)

while True:
    try:
        patient = next(it)
        print(f"Treating patient:{patient}")

    except StopIteration:
        print("All patients have been treated.")
        break