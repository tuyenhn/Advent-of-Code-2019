cands = []
for num in range(136818, 685979+1):
    num = str(num)
    flag = True
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            flag = False

    # PART 2 - SOLVED
    for uniq in set(str(num)):
        if str(num).count(uniq) == 2:
            if flag and len(set(num)) != 6:
                cands.append(num)


# print(set(cands))
print(len(set(cands)))
