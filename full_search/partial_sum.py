def main():

    N = int(input())
    W = int(input())

    data = []

    for i in range(N):
        a = int(input())
        data.append(a)
 
    bool = False
    for bit in range((1 << N)):
        sum = 0
        for i in range(N):
            if(bit & (1 << i)):
                sum += data[i]
        if(sum == W):
            bool = True
    

    if(bool==True): 
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()