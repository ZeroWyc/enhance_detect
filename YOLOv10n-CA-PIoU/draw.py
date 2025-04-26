
import pandas as pd
import matplotlib.pyplot as plt


# 训练结果列表
results_files = [
    'runs/train/exp27/results.csv',
    'runs/train/exp26/results.csv',
    'runs/train/exp24/results.csv',
]

# 与results_files顺序对应
custom_labels = [
    'yolov10n-CA-PIoU',
    'yolov10n',
    'yolov8n',

]

#
def plot_comparison(metrics, labels, custom_labels, layout=(2, 2), save_path=None):
    # 1. 增大画布尺寸（根据子图数量动态调整）
    fig_width = 18 if layout[1] >= 2 else 12  # 横向更多子图时更宽
    fig, axes = plt.subplots(layout[0], layout[1], figsize=(fig_width, 10))
    axes = axes.flatten()

    for i, (metric_key, metric_label) in enumerate(zip(metrics, labels)):
        for file_path, custom_label in zip(results_files, custom_labels):
            df = pd.read_csv(file_path)
            print(f"\n=== 文件: {file_path} ===")
            print("列名:", df.columns.tolist())
            df.columns = df.columns.str.strip()

            if 'epoch' not in df.columns or metric_key not in df.columns:
                continue

            #df = df.head(100)  # 只保留前100个epoch

            # 2. 加粗线条 + 添加标记（每隔N个点显示一个标记）
            axes[i].plot(
                df['epoch'].to_numpy(),
                df[metric_key].to_numpy(),
                label=f'{custom_label}',
                linewidth=3,          # 加粗线条（原为1-2）
                marker='o',           # 添加圆形标记
                markersize=4,         # 标记大小
                markevery=10,         # 每隔10个点显示一个标记
                alpha=0.8,
            )

        # 3. 增大标题、标签、刻度的字体
        axes[i].set_title(f'{metric_label}', fontsize=14, pad=15)  # pad增加标题间距
        axes[i].set_xlabel('Epoch', fontsize=12)
        axes[i].set_ylabel(metric_label, fontsize=12)
        axes[i].tick_params(axis='both', labelsize=10)  # 刻度字体
        axes[i].legend(fontsize=10, framealpha=0.5)     # 图例字体+半透明背景
        axes[i].grid(True, linestyle='--', alpha=0.3)

    # 4. 调整子图间距并保存高清图
    plt.tight_layout(pad=3.0)  # 增加子图间距
    if save_path:
        plt.savefig(
            save_path,
            dpi=600,                   # 超高分辨率（Word推荐300-600）
            bbox_inches='tight',       # 避免边缘被裁剪
            facecolor='white',         # 背景设为白色（避免Word中透明）
        )
    plt.show()


if __name__ == '__main__':


    # 精度指标
    metrics = [
        'metrics/precision(B)', 'metrics/recall(B)', 'metrics/mAP50(B)', 'metrics/mAP50-95(B)'
    ]

    labels = [
        'Precision', 'Recall', 'mAP@50', 'mAP@50-95'
    ]

    # 调用通用函数绘制精度对比图，并保存
    plot_comparison(metrics, labels, custom_labels, layout=(2, 2), save_path='./accuracy_comparison.png')

    # 损失指标
    loss_metrics = [
        'train/box_loss', 'train/cls_loss', 'train/dfl_loss', 'val/box_loss', 'val/cls_loss', 'val/dfl_loss'
    ]

    loss_labels = [
        'Train Box Loss', 'Train Class Loss', 'Train DFL Loss', 'Val Box Loss', 'Val Class Loss', 'Val DFL Loss'
    ]
    save_path = './comparison_plot.png'
    # 调用通用函数绘制损失对比图
    plot_comparison(loss_metrics, loss_labels, custom_labels, layout=(2, 3),save_path=save_path)

