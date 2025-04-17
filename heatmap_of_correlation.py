import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('processed_data.csv')

# 计算相关系数矩阵
corr_matrix = df.corr()
# 画热力图
plt.figure(figsize=(10, 8))  # 画布大小，可以不填
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
'''用于美化热力图的参数
annot=True  显示方块内的具体数字
cmap="coolwarm"  方块颜色调整
fmt=".2f"  方块数字两位小数
linewidths=0.5  方块与方块之间的距离
'''
plt.title("Heatmap of Correlations:Input and Output Variables")
plt.show()