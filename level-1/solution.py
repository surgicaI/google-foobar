import collections

def answer(data, n):
    my_dict = collections.Counter()
    for element in data:
        my_dict[element] += 1

    result = []

    for element in data:
        if my_dict[element] <= n:
            result.append(element)

    return result

data_list = [[5, 10, 15, 10, 7],
        [1, 2, 3],
        [1, 2, 2, 3, 3, 3, 4, 5, 5],
        [1, 2, 3]]
n_list = [1, 0, 1, 6]

for data, n in zip(data_list, n_list):
    print(answer(data, n))
