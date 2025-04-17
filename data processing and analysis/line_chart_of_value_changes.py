import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('processed_data.csv')

# 自定义下面这些部分，手动更改就可以了
selected_columns = ['IN1', 'IN2']  # 要画哪些变量的图
data_range = (200, 1000)  # 要画第多少行到第多少行的数据，这里是200到1000
colors = {
    'IN2': 'blue',
    'IN1': 'green',
}      # 每个变量对应的颜色

plt.figure(figsize=(14, 8))   # 画布尺寸

df_subset = df.loc[data_range[0]:data_range[1], selected_columns]
for col in selected_columns:
    plt.plot(df_subset.index, df_subset[col], label=col, color=colors.get(col, None), linewidth=2)

plt.xlabel("Index value")
plt.ylabel("Value")
plt.title("Line chart of value changes")

plt.legend()   # 添加图例
plt.grid(True)  # 网格线
plt.tight_layout()  # 使布局更美观，不会出现字体重叠或是图线超出边框的情况
plt.show()