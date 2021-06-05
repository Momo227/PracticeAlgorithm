def gcd(m, n):
    # ベースケース
    if(n == 0):
        return m

    # 再帰呼び出し
    return gcd(n, m % n)


def main():
    print(gcd(51, 15))
    print(gcd(15, 51))



if __name__ == '__main__':
    main()