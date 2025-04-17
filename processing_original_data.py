import pandas as pd
from sklearn.preprocessing import MinMaxScaler

path = r"C:\Users\ASUS\Desktop\original_data.csv"  # 改为本地的路径
data = pd.read_csv(path)

#  异常值处理（四分位数间距法即IQR 方法）
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
outlier_mask = (data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))
df = data.mask(outlier_mask, data.median(), axis=1) # 中位数填充异常值
# df = data.mask(outlier_mask, data.mean(), axis=1) # 均值填充，axis = 1表示使用该列的均值

#  归一化数据（Min-Max 归一化）
scaler = MinMaxScaler()
data = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

data.to_csv('processed_data.csv', index=False)