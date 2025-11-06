# LOGEL – Inverse Reinforcement Learning from a Gradient-Based Learner

本项目复现论文 **Inverse Reinforcement Learning from a Gradient-Based Learner (NeurIPS 2021)**，并在 GridWorld 环境中展示：
1) GPOMDP 学习器训练策略的过程
2) LOGEL 算法从策略梯度更新中反推出奖励函数的能力

本指南保证在 **Linux / HPC / SSH** 环境可复现，无需图形界面。

---

## 环境准备

### 1) 克隆仓库
git clone https://github.com/IsSaudade/LOGEL.git

cd LOGEL/gridworld


### 2) 创建 Conda 环境
conda create -n logel python=3.10 -y
conda activate logel


### 3) 安装依赖（注意：必须使用 gym 0.21）
pip install numpy==1.23.5
pip install "gym==0.21.0" --no-build-isolation
pip install pyglet==1.5.21
pip install torch matplotlib


### 4) （可选，仅服务器无图形界面时）
export DISPLAY=:99
Xvfb :99 -screen 0 1024x768x24 >/dev/null 2>&1 &

---

## 运行实验

### Step 1: 使用 GPOMDP 生成策略学习轨迹
python -m learners.learner_gpomdp --expe 1



运行后会生成：
LOGEL/agent_trajectories/GPOMDP/
├─ traj_GPOMDP_1.npy
├─ feat_GPOMDP_1.npy
├─ params_GPOMDP_1.npy
└─ disc_ret_GPOMDP_1.npy


### Step 2: 使用 LOGEL 从轨迹中反推出奖励
python logel.py --expe 1


生成：
LOGEL/gridworld/results/
├─ weights_logel_1_GPODMP.npy
└─ value_logel_1_GPODMP.npy

## 可视化结果

### 学习曲线（折扣回报随训练步变化）
### 奖励恢复对比（LOGEL vs 真实奖励）
参考论文，我粗略画了个，在results_fig