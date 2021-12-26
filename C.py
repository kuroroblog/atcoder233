import itertools
# 袋に入っているボールの個数の総積は10の5乗を超えない。 ⏩ 袋の中からボールを1つずつ選ぶ組み合わせは10の5乗を超えないを意味する。 ⏩ 普通に全通り検証して問題ない。

# 標準入力を受け付ける。
N, X = map(int, input().split())

# 袋の中に入っている、ボール情報を格納する。
baggages = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    baggages.append(tmp[1:])

# 参考 : https://note.nkmk.me/python-itertools-product/
product_list = itertools.product(*baggages)
ans = 0
for product in product_list:
    value = 1
    for p in product:
        if value > X:
            break
        value *= p

    if X == value:
        ans += 1

print(ans)
