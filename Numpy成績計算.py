# 假設我們有一個包含學生考試成績的數據集，我們希望使用 NumPy 來進行以下操作：

# 1.計算每個學生的總分和平均分。
# 2.找出每個考試科目的最高分和最低分。
# 3.找出每個學生的排名。

# [
#     [85, 92, 88, 96],
#     [78, 85, 82, 90],
#     [91, 89, 95, 94],
#     [76, 80, 83, 87],
#     [88, 92, 91, 85]
# ]

# solution
import numpy as np


scores = np.array([
    [85, 92, 88, 96],
    [78, 85, 82, 90],
    [91, 89, 95, 94],
    [76, 80, 83, 87],
    [88, 92, 91, 85]
])

total_scores = np.sum(scores, axis=1)
average_scores = np.mean(scores, axis=1)

max_scores = np.max(scores, axis=0)
min_scores = np.min(scores, axis=0)

ranking = np.argsort(-total_scores) + 1

print("學生考試成績數據集:")
print(scores)

print("\n每個學生的總分:")
print(total_scores)

print("\n每個學生的平均分:")
print(average_scores)

print("\n每個考試科目的最高分:")
print(max_scores)

print("\n每個考試科目的最低分:")
print(min_scores)

print("\n每個學生的排名:")
print(ranking)