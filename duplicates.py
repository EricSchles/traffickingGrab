national = open("national_links.txt","r")

to_check = []
double = {}

for i in national:
    name = i.split(",")[1].lstrip().rstrip()
    to_check.append(name)

for i in to_check:
    double[i] = 0
    for j in to_check:
        if i == j:
            double[i] += 1

for i in double:
    if double[i] > 1:
        print i
