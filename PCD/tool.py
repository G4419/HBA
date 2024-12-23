import pcl
import numpy as np

# 加载 PCD 文件
pcd = pcl.load("/home/ryan/slam/hba_ws/src/HBA/PCD/cloud.pcd")

# 获取点云数据
points = np.asarray(pcd)

# 检查 NaN 和无穷值
if np.isnan(points).any() or np.isinf(points).any():
    print("PCD 文件中存在无效值（NaN 或无穷值）")
else:
    print("PCD 文件中没有无效值")

