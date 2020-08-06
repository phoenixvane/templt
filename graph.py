import pandas as pd
from matplotlib import pyplot as plt

# ログ読み込み
log = pd.read_csv("log.csv", index_col=0)

# 温度と明るさ毎にグラフ関連付け
s = log.index
fig, ax1 = plt.subplots()
ax1.plot(s, log['temp'], color="r", label="temp")
ax2 = ax1.twinx()
ax2.plot(s, log["lt"], color="b", label="lt")

# タイトルや軸ラベル
ax1.set_title("temp/lt")
ax1.set_ylabel("temp")
ax2.set_ylabel("lt")

# 凡例
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# 表示
plt.show()
