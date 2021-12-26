################################
# <方針>
# 連続部分列 ⏩ 連続部分列の一番左のインデックスをl, 連続部分列の一番右のインデックスをrとした場合に、0インデックス~rの数列の総和 - 0インデックス~lの数列の総和になる。
# r - l = kになればいいので、l = r - kになるlの位置がどれくらいあるのか探せば良い。
################################

from collections import Counter

# 標準入力を受け付ける。
N, K = map(int, input().split())

A = list(map(int, input().split()))

cnt = Counter([0])
ans = 0
r = 0
for a in A:
    r += a
    ans += cnt[r - K]
    cnt[r] += 1

print(ans)
