word = input().upper()

cnt_list = []

for letter in set(word):
    cnt_list.append(word.count(letter))

idx = [i for i, x in enumerate(cnt_list) if x == max(cnt_list)]

if len(idx) == 2:
    print("?")

else:
    print(list(set(word))[cnt_list.index(max(cnt_list))])
    print(list(set(word))[idx[0]])