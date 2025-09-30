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
data = sio.loadmat('../matlab/obe_lost.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()

x_max = max(data['distance'])
dist_org = data['distance']

vg_lost_speed = butter_lowpass_filter(data['vg_lost_speed_err'], 1000, 0.2)
vr_lost_speed = butter_lowpass_filter(data['vr_lost_speed_err'], 1000, 0.2)
gps_lost_speed = butter_lowpass_filter(data['gps_lost_speed_err'], 1000, 0.2)
btm_lost_speed = butter_lowpass_filter(data['btm_lost_speed_err'], 1000, 0.2)
imu_lost_speed  = butter_lowpass_filter(data['imu_lost_speed_err'], 1000, 0.2)

# ---------- 下采样，避免曲线太粗 ----------
step = 100   # 每隔多少点取一个（可以调大，比如20、50）
dist = data['distance'][::step]
vg_lost_speed = vg_lost_speed[::step]
vr_lost_speed =  vr_lost_speed[::step]
gps_lost_speed = gps_lost_speed[::step]
btm_lost_speed = btm_lost_speed[::step]
imu_lost_speed = imu_lost_speed[::step]


fig, ax = plt.subplots(figsize=(10, 4))
line1, = ax.plot(dist, vr_lost_speed,   '-', linewidth=1, label='雷达失效',marker='x', markevery=(100, 400), markersize=5)
line2, = ax.plot(dist, vg_lost_speed,   '--',  linewidth=1, label='速传失效')
line3, = ax.plot(dist, gps_lost_speed, '-.', linewidth=1, label='GPS失效',marker='^', markevery=(0, 400), markersize=5)
line4, = ax.plot(dist, imu_lost_speed, '-',  linewidth=1, label='IMU失效')
line5, = ax.plot(dist, btm_lost_speed, '--', linewidth=1, label='BTM失效',marker='d', markevery=(200, 400), markersize=5)
# (0,(3,1,1,1)) 是 matplotlib 的“自定义虚线样式”



ax.set_xlim(5, x_max)
ax.set_ylim(-2.4, 2.4)
ax.set_xlabel('运行里程 (m)')
ax.set_ylabel('测速误差 (m/s)', color='k')
fig.suptitle("各传感器失效时测速误差(经二阶巴特沃斯滤波显示)", fontsize=12, y=0.95)
ax.legend(
    loc='upper right',        # 图例放在图上方居中
    ncol=3,                    # 每行 3 个 → 两行
    fontsize=10
)
plt.savefig("obe_lost_v.svg", bbox_inches="tight")
plt.show()