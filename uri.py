for t in range(int(input())):
    set1 = []
    for n in range(int(input())):
        set1.append(set(input().split()[1:]))

    for q in range(int(input())):
        op = [int(x) for x in input().split()]
        if op[0] == 1:
            result = set1[op[1] - 1] & set1[op[2] - 1]
        elif op[0] == 2:
            result = set1[op[1] - 1] | set1[op[2] - 1]

        print(len(result))
