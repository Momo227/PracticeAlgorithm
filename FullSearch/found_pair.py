def main():

    N = int(input())
    K = int(input())

    min = int(20000000)

    data1 = []
    data2 = []


    for i in range(N):
        a = int(input())
        b = int(input())
        data1.append(a)
        data2.append(b)
 
    min_value = min
    for i in range(N):
        for j in range(N):
            if(data1[i] + data2[j] < K):
                continue

            if(data1[i] + data2[j] < min_value):
                min_value = data1[i]+data2[j]
    
    print(min_value) 

if __name__ == '__main__':
    main()