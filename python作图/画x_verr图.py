import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取 mat 文件
data = sio.loadmat('../matlab/train_simu_data.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()

x_max = max(data['distance'])

fig, ax = plt.subplots(figsize=(10,4))

# ---------- 曲线 ----------
line1, = ax.plot(data['distance'], data['trad_speed_err'], 'r', label='传统方法')
line2, = ax.plot(data['distance'], data['EKF_speed_err'], 'b', label='EKF')

# ---------- BTM 矫正点 ----------
btm_idx = data['btm'] > 0
t_btm   = data['distance'][btm_idx]

# star = ax.plot(t_btm, data['EKF_speed_err'][btm_idx],
#                linestyle='None', marker='*', color='k',
#                markersize=8, label='BTM矫正点')

# ---------- 坐标轴设置 ----------
ax.set_xlim(0, x_max)
ax.set_ylim(-1, 3)
ax.set_xlabel('运行里程 (m)')
ax.set_ylabel('速度误差 (m)')

# ---------- 图例 ----------
ax.legend(loc='upper right')

# ---------- 标题 ----------
fig.suptitle("速度误差对比(轮径偏小20mm)", fontsize=12, y=0.95)

plt.savefig("speed_verr.svg", bbox_inches="tight")
plt.show()




