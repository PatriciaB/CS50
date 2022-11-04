points = int(input("How many points did you lose? "))

if points < 2:
    print("lost fewer points")
elif points > 2:
    print("lost more points")
else:
    print("lost the same")