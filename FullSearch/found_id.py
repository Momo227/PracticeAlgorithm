def main():

    N = int(input())
    v = int(input())

    data = []

    for i in range(N):
        a = int(input())
        data.append(a)


    found_id = -1
    for i in range(N):
        if(data[i] == v):
            found_id = i
            break
    
    print(found_id) 

if __name__ == '__main__':
    main()