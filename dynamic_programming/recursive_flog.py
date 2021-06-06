INF = 10 ** 18


def chmin(lis1: list, lis2: list) -> bool:
    assert len(lis1) == len(lis2) == 1, "1要素のlistを指定"
    if lis1[0] > lis2[0]:
        lis1[0] = lis2[0]
        return True
    return False


def main():
    N = int(input())
    data = [int(x) for x in input().split()]
    dp = [[INF] for _ in range(N)]
    dp[0] = [0]

    for i in range(1, N):
        lis = [dp[i - 1][0] + abs(data[i] - data[i - 1])]
        chmin(dp[i], lis)

        if i > 1:
            lis = [dp[i - 2][0] + abs(data[i] - data[i - 2])]
            chmin(dp[i], lis)


    print(*dp[-3])

if __name__ == '__main__':
     main()
