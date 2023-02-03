from copy import deepcopy


def is_changable(un: str):
    un_num = []
    for i in un:
        un_num.append(ord(i))
    un_num_s = deepcopy(un_num)
    un_num_s.sort()
    print(un_num, un_num_s)
    for i in range(len(un_num)):
        if un_num[i] != un_num_s[i]:
            return "YES"
    return "NO"
