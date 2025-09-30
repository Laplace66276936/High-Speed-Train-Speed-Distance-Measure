import scipy.io as sio
import numpy as np

# 读取 mat 文件
data = sio.loadmat('../matlab/EKF_trad.mat')
for key, val in data.items():
    if isinstance(val, np.ndarray):
        data[key] = val.squeeze()

print(f"(测速)本文方法"
      f"{np.mean(abs(data['EKF_speed_err'])):>.3f}, "
      f"{np.std(data['EKF_speed_err']):>.3f}, "
      f"{np.max(data['EKF_speed_err']):>.3f}")
print(f"(测速)传统方法"
      f"{np.mean(abs(data['trad_speed_err'])):>.3f}, "
      f"{np.std(data['trad_speed_err']):>.3f}, "
      f"{np.max(data['trad_speed_err']):>.3f}")

print(f"(测距)本文方法"
      f"{np.mean(abs(data['EKF_dist_err'])):>.3f}, "
      f"{np.std(data['EKF_dist_err']):>.3f}, "
      f"{np.max(data['EKF_dist_err']):>.3f}")
print(f"(测距)传统方法"
      f"{np.mean(abs(data['trad_dist_err'])):>.3f}, "
      f"{np.std(data['trad_dist_err']):>.3f}, "
      f"{np.max(data['trad_dist_err']):>.3f}")