def main():
    N = int(input())
    W = int(input())

    weight = []
    value = []
    for i in range(N):
        x, y = map(int, input().split())
        weight.append(x)
        value.append(y)

    # 2次元配列でdpを表現　dp[i番目の品物][重さw]
    dp = [[0]*(W+1) for j in range(N+1)]


    # dpループ
    for i in range(N):
        for j in range(W+1):
            # i番目の品を選ばない時
            if weight[i] > j:
                dp[i + 1][j] = dp[i][j]
            # i番目の品を選ぶ時
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])


    print(dp[N][W])


if __name__ == '__main__':
    main()
