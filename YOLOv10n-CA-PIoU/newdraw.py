import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建绘图
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制深度卷积部分
depthwise_rects = [
    patches.Rectangle((-1, 2), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue', label='1x1 Conv'),
    patches.Rectangle((-1, 0), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue', label='1x1 Conv'),
    patches.Rectangle((0, 2), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue'),
    patches.Rectangle((0, 0), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue'),
    patches.Rectangle((1, 2), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue'),
    patches.Rectangle((1, 0), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue'),
    patches.Rectangle((2, 2), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue'),
    patches.Rectangle((2, 0), 1, 1, linewidth=2, edgecolor='blue', facecolor='lightblue')
]

# 绘制点卷积部分
pointwise_rect = patches.Rectangle((4, 1), 1, 3, linewidth=2, edgecolor='orange', facecolor='orange', label='1x1 Conv')

# 添加深度卷积矩形
for rect in depthwise_rects:
    ax.add_patch(rect)

# 添加点卷积矩形
ax.add_patch(pointwise_rect)

# 添加箭头连接
ax.annotate('', xy=(1, 2.5), xytext=(2, 2.5), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(1, 0.5), xytext=(2, 0.5), arrowprops=dict(arrowstyle='->', lw=1.5))

ax.annotate('', xy=(3, 2), xytext=(4, 2), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.annotate('', xy=(3, 0), xytext=(4, 0), arrowprops=dict(arrowstyle='->', lw=1.5))

# 添加文字标签
ax.text(-1.2, 2.5, 'Depthwise Convolution', fontsize=12, color='blue')
ax.text(4.2, 2.5, 'Pointwise Convolution', fontsize=12, color='orange')

# 设置坐标轴
ax.set_xlim(-2, 6)
ax.set_ylim(-1, 4)

# 移除坐标轴
ax.axis('off')

# 显示图形
plt.show()
