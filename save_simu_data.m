save('EKF_trad.mat','t','distance','speed','btm','EKF_dist_err', 'EKF_speed_err','trad_dist_err','trad_speed_err');

%% ȫ������
no_lost_speed_err = EKF_speed_err;
no_lost_dist_err = EKF_dist_err;

%% �ٴ�ʧЧ
vg_lost_speed_err = EKF_speed_err;
vg_lost_dist_err = EKF_dist_err;

%% �״�ʧЧ
vr_lost_speed_err = EKF_speed_err;
vr_lost_dist_err = EKF_dist_err;

%% GPS��λʧЧ
gps_lost_speed_err = EKF_speed_err;
gps_lost_dist_err = EKF_dist_err;

%% BTM��λʧЧ
btm_lost_speed_err = EKF_speed_err;
btm_lost_dist_err = EKF_dist_err;

%% IMUʧЧ
imu_lost_speed_err = EKF_speed_err;
imu_lost_dist_err = EKF_dist_err;

%% ���ָ�ʧЧ����
save('obe_lost.mat','t','distance','speed','btm',...
    'no_lost_speed_err','no_lost_dist_err',...
    'vg_lost_speed_err','vg_lost_dist_err',...
    'vr_lost_speed_err','vr_lost_dist_err',...
    'gps_lost_speed_err','gps_lost_dist_err',...
    'btm_lost_speed_err','btm_lost_dist_err',...
    'imu_lost_speed_err','imu_lost_dist_err');


%% BTM GPSʧЧ���
btm_gps_lost_speed_err = EKF_speed_err;
btm_gps_lost_dist_err = EKF_dist_err;

%%
save('gps_btm_lost.mat','t','distance','speed','btm',...
    'no_lost_speed_err','no_lost_dist_err',...
 'btm_gps_lost_speed_err','btm_gps_lost_dist_err');