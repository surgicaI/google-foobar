def answer(l):
    if len(l) < 3:
        return 0
    divs = [0 for _ in l]
    none_found = True
    for index, num in enumerate(l):
        for j in range(index+1, len(l)):
            num2 = l[j]
            if num2 % num == 0:
                divs[index] += 1
                none_found = False

    if none_found:
        return 0
    result = 0
    for index, num in enumerate(l):
        for j in range(index+1, len(l)):
            num2 = l[j]
            if num2 % num == 0:
                result += divs[j]

    return result
