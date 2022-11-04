answer = input("Do you agree? ").lower()


#if answer == "y" or answer =="Y":
if answer in ["y", "yes"]:
    print("Agree")
elif answer in ["n", "not"]:
    print("Not agree")