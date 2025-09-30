import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

def plot_btm_stem(ax, t, y, color='g', size=5, label=None):
    """
    在子图 ax 上绘制 BTM 矫正点的小棍子效果：
    只画五角星，不重复加 legend
    """
    # 真正画五角星
    ax.plot(t, y, linestyle='None', marker='*', color=color,
            markersize=size, label=label)

# 读取 mat 文件
data = sio.loadmat('../matlab/EKF_trad.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()

x_max = max(data['distance'])

# ---------- 创建子图 ----------
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10,4))

# 传统方法（不加 legend）
ax1.plot(data['distance'], data['trad_dist_err'], 'r',linewidth=0.8, alpha=0.9)
ax1.set_ylabel('传统方法误差 (m)')
ax1.set_xlim(0, x_max)
ax1.set_ylim(-10, 60)

# EKF 方法（不加 legend）
ax2.plot(data['distance'], data['EKF_dist_err'], 'b', linewidth=0.6, alpha=0.7)
ax2.set_ylabel('EKF误差 (m)')
ax2.set_xlabel('运行里程 (m)')
ax2.set_xlim(0, x_max)
ax2.set_ylim(-1.2, 1)

# ---------- BTM 矫正点 ----------
btm_idx = data['btm'] > 0
t_btm   = data['distance'][btm_idx]

# 上图：五角星 + legend
plot_btm_stem(ax1, t_btm, data['trad_dist_err'][btm_idx],
              color='b', size=5, label='BTM矫正点')
ax1.legend(loc='upper right')

# 下图：五角星 + legend
plot_btm_stem(ax2, t_btm, data['EKF_dist_err'][btm_idx],
              color='r', size=5, label='BTM矫正点')
ax2.legend(loc='upper right')


# ---------- 版面调整 ----------
plt.subplots_adjust(hspace=0.05)
fig.suptitle("测距误差对比(轮径偏小20mm)", fontsize=12, y=0.95)
plt.savefig("x_xerr.svg", bbox_inches="tight")

plt.show()



