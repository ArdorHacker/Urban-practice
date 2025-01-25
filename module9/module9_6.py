def all_variants(text):
    cnt = len(text)

    for i in range(cnt):
        for j in range(cnt):
            yield text[j: i + j + 1]

        cnt -= 1

a = all_variants("abc")
for i in a:
    print(i)