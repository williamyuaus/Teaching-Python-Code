from collections import Counter
pharse = 'Statue of Liberty'
pharse_sorted = sorted(pharse.lower().strip())
count = Counter(pharse_sorted)
print(count)