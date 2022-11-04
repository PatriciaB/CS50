scores = []         #empty list
for i in range(3):
    score = int(input("What's your scores? "))
    scores.append(score)  # or scores += [score]     

average = sum(scores) / len(scores) #media
print(f"Average: {average}")    #usar sendo o f no inicio, codigo formatado