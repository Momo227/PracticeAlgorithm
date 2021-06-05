def fibo(n):
    # 再起関数を呼び出したことを報告
    print("fibo(", n, ")を呼び出しました。")

    # ベースケース
    if(n == 0):
        return 0
    elif (n == 1):
        return 1

    # 再帰呼び出し
    result = fibo(n-1) + fibo(n-2)
    print(n, '項目 = ', result)
    return result

def main():
    fibo(6)



if __name__ == '__main__':
    main()