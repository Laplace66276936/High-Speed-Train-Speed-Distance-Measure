import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

plt.title("差值示例")  # 测试中文
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
