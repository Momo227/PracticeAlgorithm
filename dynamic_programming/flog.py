def main():
    n = int(input())
    data = []

    for i in range(n):
        a = int(input())
        data.append(a)

        # 配列 dp を定義（配列全体を無限大を表す値に初期化）
        dp = [0 for _ in range(n)]

        dp[0] = 0

    for i in range(1, n):
        if i == 1:
            dp[i] = abs(data[i]-data[i-1])
        else:
            dp[i] = min(dp[i-1] + abs(data[i]-data[i-1]), dp[i-2] + abs(data[i]-data[i-2]))

    print(dp[n-1])



if __name__ == '__main__':
    main()