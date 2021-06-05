def func(i, w, data):
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False

        # data[i-1]を選ばない時
    if func(i-1, w, data):
        return True

    # a[i-1]を選ぶ時
    if func(i-1, w - data[i-1], data):
        return True

    # どちらもfalse
    return False


def main():

    N = int(input())
    W = int(input())
    data = []

    for i in range(N):
        s = int(input())
        data.append(s)

    # 再帰的に解く
    if func(N, W, data):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()