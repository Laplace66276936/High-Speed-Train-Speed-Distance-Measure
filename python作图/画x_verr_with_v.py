import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取 mat 文件
data = sio.loadmat('../matlab/EKF_trad.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()

x_max = max(data['distance'])

fig, ax1 = plt.subplots(figsize=(10,4))

# ---------- 下采样，避免曲线太粗 ----------
step = 100   # 每隔多少点取一个（可以调大，比如20、50）
dist = data['distance'][::step]
trad_err = data['trad_speed_err'][::step]
ekf_err  = data['EKF_speed_err'][::step]
speed    = data['speed'][::step]

# ---------- 左 y 轴：速度误差 ----------
line1, = ax1.plot(dist, trad_err, 'r', linewidth=0.6, alpha=0.7, label='传统方法测速误差')
line2, = ax1.plot(dist, ekf_err, 'b', linewidth=0.6, alpha=0.7, label='EKF测速误差')

ax1.set_xlim(0, x_max)
ax1.set_ylim(-1, 4)
ax1.set_xlabel('运行里程 (m)')
ax1.set_ylabel('速度误差 (m/s)', color='k')

# ---------- 右 y 轴：运行速度 ----------
ax2 = ax1.twinx()  # 共用 x 轴
line3, = ax2.plot(dist, speed, 'g', linewidth=1.5, label='实际运行速度(右纵轴)')
ax2.set_ylabel('运行速度 (m/s)', color='k')
ax2.set_ylim(0, 140)

# ---------- 图例 ----------
lines = [line1, line2, line3]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right')

# ---------- 标题 ----------
fig.suptitle("测速误差对比(轮径偏小20mm)", fontsize=12, y=0.95)

plt.savefig("speed_err_with_speed.svg", bbox_inches="tight")
plt.show()

