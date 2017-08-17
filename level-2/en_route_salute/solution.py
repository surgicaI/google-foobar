def answer(s):
    result = 0
    right_dir_num = 0
    left_dir_number = 0
    for ch in s:
        if ch == '>':
            right_dir_num += 1
        elif ch == '<':
            left_dir_number += 1
            result = result + (2*right_dir_num)
    return result
