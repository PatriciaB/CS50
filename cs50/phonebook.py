people = {
    "Carter":"+1-123",
    "David":"+1-321"
}         

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")