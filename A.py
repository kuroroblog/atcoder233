# 標準入力を受け付ける。
X, Y = map(int, input().split())

cnt = 0
while X < Y:
    cnt += 1
    # 10円切手をY円を超えるまで足していく。
    X += 10

# 10円切手を使った個数を出力する。
print(cnt)
