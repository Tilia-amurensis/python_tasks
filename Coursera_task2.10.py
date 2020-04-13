if __name__ == "__main__":
    i = int(input())
    y = 1
    while True:
        r = y * y
        if r > i:
            break
        print(r, end=" ")
        y += 1
