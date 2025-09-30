save('EKF_trad.mat','t','distance','speed','btm','EKF_dist_err', 'EKF_speed_err','trad_dist_err','trad_speed_err');

%% 全部正常
no_lost_speed_err = EKF_speed_err;
no_lost_dist_err = EKF_dist_err;

%% 速传失效
vg_lost_speed_err = EKF_speed_err;
vg_lost_dist_err = EKF_dist_err;

%% 雷达失效
vr_lost_speed_err = EKF_speed_err;
vr_lost_dist_err = EKF_dist_err;

%% GPS定位失效
gps_lost_speed_err = EKF_speed_err;
gps_lost_dist_err = EKF_dist_err;

%% BTM定位失效
btm_lost_speed_err = EKF_speed_err;
btm_lost_dist_err = EKF_dist_err;

%% IMU失效
imu_lost_speed_err = EKF_speed_err;
imu_lost_dist_err = EKF_dist_err;

%% 保持各失效数据
save('obe_lost.mat','t','distance','speed','btm',...
    'no_lost_speed_err','no_lost_dist_err',...
    'vg_lost_speed_err','vg_lost_dist_err',...
    'vr_lost_speed_err','vr_lost_dist_err',...
    'gps_lost_speed_err','gps_lost_dist_err',...
    'btm_lost_speed_err','btm_lost_dist_err',...
    'imu_lost_speed_err','imu_lost_dist_err');


%% BTM GPS失效情况
btm_gps_lost_speed_err = EKF_speed_err;
btm_gps_lost_dist_err = EKF_dist_err;

%%
save('gps_btm_lost.mat','t','distance','speed','btm',...
    'no_lost_speed_err','no_lost_dist_err',...
 'btm_gps_lost_speed_err','btm_gps_lost_dist_err');