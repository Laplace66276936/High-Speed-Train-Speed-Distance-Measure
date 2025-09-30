import scipy.io as sio
import numpy as np

# 读取 mat 文件
data = sio.loadmat('../matlab/obe_lost.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()


speed_key = ['imu_lost_speed_err', 'vg_lost_speed_err', 'vr_lost_speed_err',
             'gps_lost_speed_err', 'btm_lost_speed_err', ]
dist_key = ['imu_lost_dist_err', 'vg_lost_dist_err', 'vr_lost_dist_err',
             'gps_lost_dist_err', 'btm_lost_dist_err', ]

for k in speed_key:
      print(f"{k.split('_')[0]}: "
            f"{np.mean(abs(data[k])):>.3f}, "
            f"{np.std(data[k]):>.3f}, "
            f"{np.max(data[k]):>.3f}")

print('')
for k in dist_key:
      print(f"{k.split('_')[0]}: "
            f"{np.mean(abs(data[k])):>.3f}, "
            f"{np.std(data[k]):>.3f}, "
            f"{np.max(data[k]):>.3f}")

