sample = sorted("AAAACCCGGT", reverse = True)
answer = []
for x in sample:
    t = ""
    if x == "A":
        x == t + "T"
        answer.append(x)
    elif x == "T":
        x == t + "A"
        answer.append(x)
    elif x == "G":
        x == t + "C"
        answer.append(x)
    else:
        x == t + "G"
        answer.append(x)

print("".join(answer))
