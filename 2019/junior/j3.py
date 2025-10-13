# CCC 2019 Junior J3: Cold Compress

lines = int(input())

for _ in range(lines):
    text = input()
    if not text:
        print()
        continue

    encoded = []
    count = 1
    for idx in range(1, len(text)):
        if text[idx] == text[idx - 1]:
            count += 1
        else:
            encoded.append(f"{count} {text[idx - 1]}")
            count = 1

    encoded.append(f"{count} {text[-1]}")
    print(" ".join(encoded))
