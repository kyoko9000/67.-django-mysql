from collections import Counter

L = [10, 2, 3, 2, 5, 10, 8, 9, 9, 8, 9]
counts = Counter(L)
print(counts)
R = {}
for i, n in enumerate(L):
    # if counts[n]>1:
    R.setdefault(n, []).append(i)
print(R)
# print(list(enumerate(L)))

# from collections import defaultdict

# l = [1, 2, 3, 4, 1, 3]
# _indices = defaultdict(list)
#
# for index, item in enumerate(l):
#     _indices[item].append(index)
#
# m = []
# for key, value in _indices.items():
#     # if len(value) > 1:
#         # Do something when them
#         m.append([key, value])
# print(m)
