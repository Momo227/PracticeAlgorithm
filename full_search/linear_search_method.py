def main():

    N = int(input())
    v = int(input())

    data = []

    for i in range(N):
        a = int(input())
        data.append(a)


    bool = False
    for i in range(N):
        if(data[i] == v):
            bool = True

    if(bool):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()