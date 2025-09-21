n = int(input())
words = {}
order = []
for _ in range(n):
    word = input().strip()
    if word not in words:
        words[word] = 0
        order.append(word)
    words[word] += 1
print(len(order)) 
print(" ".join(str(words[word]) for word in order))       