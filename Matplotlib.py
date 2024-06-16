import matplotlib.pyplot as plt
import numpy as np

# 生成資料
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 創建圖表和軸
fig, ax = plt.subplots()

# 繪製折線圖
ax.plot(x, y1, label='Sine Wave', color='blue')
ax.plot(x, y2, label='Cosine Wave', color='red')

# 添加標題和標籤
ax.set_title('Sine and Cosine Waves')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# 顯示圖例
ax.legend()

# 顯示圖表
plt.show()

# # 生成資料
# categories = ['A', 'B', 'C', 'D']
# values = [4, 7, 1, 8]

# # 創建圖表
# fig, ax = plt.subplots()

# # 繪製條形圖
# ax.bar(categories, values, color=['blue', 'green', 'red', 'purple'])

# # 添加標題和標籤
# ax.set_title('Category Values')
# ax.set_xlabel('Category')
# ax.set_ylabel('Values')

# # 顯示圖表
# plt.show()
