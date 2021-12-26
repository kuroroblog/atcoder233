# 標準入力を受け付ける。
L, R = map(int, input().split())
s = input()

# L ~ Rの間の文字列を反転する。
# L - 1としているのは、配列のインデックスの始まりが0からだから。
# 参考 : https://note.nkmk.me/python-str-extract/
center = s[L - 1:R]
# 参考 : https://note.nkmk.me/python-reverse-reversed/
center = ''.join(list(reversed(center)))

value = ''
flag = False
for i in range(len(s)):
    # L ~ Rの間だけ、反転処理を行う。
    # L - 1, R - 1としているのは、配列のインデックスの始まりが0からだから。
    if L - 1 <= i and i <= R - 1:
        if flag:
            continue

        flag = True

        # 一度だけ反転した文字列の値を格納する。
        value = value + center

        continue
    # それ以外の場合は反転処理を行わない。
    value = value + s[i]

print(value)
