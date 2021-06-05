memo = [-1 for _ in range(50)]

def fibo(n):

    # ベースケース
    if(n == 0):
        return 0
    elif (n == 1):
        return 1

    # メモをチェック
    if(memo[n] != -1):
        return memo[n]

    # メモを見ながら再帰呼び出しÅ
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

def main():

    fibo(49)

    for n in range(2, 50):
        print(n-1, '項目 = ', memo[n])



if __name__ == '__main__':
    main()