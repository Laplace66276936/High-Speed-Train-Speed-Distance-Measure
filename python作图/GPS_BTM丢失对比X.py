import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

import numpy as np
from scipy.signal import butter, filtfilt


def butter_lowpass_filter(y, fs, fc):
    """
    二阶巴特沃斯低通滤波器 (零相位)

    参数:
        y  : 原始信号 (numpy array)
        fs : 采样频率 (Hz 或者 每单位x的采样点数)
        fc : 截止频率 (Hz)

    返回:
        y_filt : 滤波后的信号
    """
    order = 2
    b, a = butter(order, fc / (fs / 2), btype='low')
    y_filt = filtfilt(b, a, y)  # 零相位滤波，避免相位延迟
    return y_filt


# 读取 mat 文件
data = sio.loadmat('../matlab/gps_btm_lost.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()

x_max = max(data['distance'])
dist_org = data['distance']

no_lost_speed = butter_lowpass_filter(data['no_lost_speed_err'], 4000, 0.2)
btm_gps_lost_speed = butter_lowpass_filter(data['btm_gps_lost_speed_err'], 4000, 0.2)
no_lost_dist = butter_lowpass_filter(data['no_lost_dist_err'], 4000, 0.2)
btm_gps_lost_dist = butter_lowpass_filter(data['btm_gps_lost_dist_err'], 4000, 0.2)

# ---------- 下采样，避免曲线太粗 ----------
step = 400   # 每隔多少点取一个（可以调大，比如20、50）
dist = data['distance'][::step]
no_lost_speed = no_lost_speed[::step]
btm_gps_lost_speed =  btm_gps_lost_speed[::step]
no_lost_dist = no_lost_dist[::step]
btm_gps_lost_dist =  btm_gps_lost_dist[::step]


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10,4))
line1, = ax1.plot(dist, no_lost_speed,   '--', linewidth=0.8, label='正常情况', markevery=(100, 400), markersize=5)
line2, = ax1.plot(dist, btm_gps_lost_speed, '-', linewidth=0.8, label='GPS BTM同时失效', markevery=(0, 400), markersize=5)

line3, = ax2.plot(dist, no_lost_dist,   '--', linewidth=0.8, label='正常情况', markevery=(100, 400), markersize=5)
line4, = ax2.plot(dist, btm_gps_lost_dist, '-', linewidth=0.8, label='GPS BTM同时失效', markevery=(0, 400), markersize=5)


ax1.set_xlim(5, x_max)
ax1.set_ylim(-1.1, 1.2)
ax1.set_ylabel('测速误差 (m/s)', color='k')
ax1.legend(
    loc='upper right',        # 图例放在图上方居中
    ncol=3,                    # 每行 3 个 → 两行
    fontsize=10
)

ax2.set_xlim(5, x_max)
ax2.set_ylim(-3, 3)
ax2.set_xlabel('运行里程 (m)')
ax2.set_ylabel('测距误差 (m)', color='k')
ax2.legend(
    loc='upper right',        # 图例放在图上方居中
    ncol=3,                    # 每行 3 个 → 两行
    fontsize=10
)

plt.subplots_adjust(hspace=0.05)
fig.suptitle("BTM GPS同时失效时测速测距误差(经二阶巴特沃斯滤波显示)", fontsize=12, y=0.95)
plt.savefig("btm_gps_lost_x.svg", bbox_inches="tight")
plt.show()