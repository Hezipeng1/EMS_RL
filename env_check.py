# env_check.py - 修正版（匹配真实类名+初始化参数）
from Energy_District_Gym_Environment import EnergyDistrictEnvironment  # 修正类名
import yaml
import pandas as pd  # 补充依赖（原类中用到了pd，需导入）

# 初始化能源环境（注意：原类的__init__参数是config_file，不是config）
env = EnergyDistrictEnvironment(config_file="./config.yaml")  # 修正初始化参数

# 重置环境获取初始状态
obs, info = env.reset()
print("✅ 环境初始化成功，初始状态维度：", obs.shape)

# 测试单步动作执行
action = env.action_space.sample()  # 随机采样一个动作
next_obs, reward, done, truncated, info = env.step(action)
print("✅ 单步交互成功，奖励值：", reward)

env.close()
