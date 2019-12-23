while True:
    try:
        s = int(input())
        if s%2 == 0:
            print("Even")
        else:
            print("Odd")
    except EOFError:
        break
