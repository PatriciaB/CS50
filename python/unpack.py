def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts



coins = {"galleons": 100, "sickles":50, "knuts":25}

print(total(**coins), "Knuts")          #unpacking using a dictionary
"""
coins = [100, 50, 25]

print(total(*coins), "Knuts")           #unpacking using a list
"""












"""
first, last = input("Whats's you name: ").split(" ")
print(f"hello, {first}")
"""