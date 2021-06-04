def main():

    N = int(input())
    min = int(20000000)

    data = []

    for i in range(N):
        a = int(input())
        data.append(a)


    min_value = min
    for i in range(N):
        if(data[i] < min_value):
            min_value = data[i]
    
    print(min_value) 

if __name__ == '__main__':
    main()