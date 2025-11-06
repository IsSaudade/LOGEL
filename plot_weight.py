import numpy as np
import matplotlib.pyplot as plt

# True reward weights of GridWorld (论文中固定的)
true_w = np.array([-3, -1, -5, 7, 0])

# Load LOGEL recovered weights
weights = np.load("../gridworld/results/weights_logel_2_GPODMP.npy")
est_w = weights[-1]

# Normalize both (reward is identifiable only up to scale)
true_w_n = true_w / np.max(np.abs(true_w))
est_w_n = est_w / np.max(np.abs(est_w))

# Align sign
if np.dot(true_w_n, est_w_n) < 0:
    est_w_n = -est_w_n

plt.figure(figsize=(5,3.5))
plt.plot(true_w_n, label="True Reward", marker="o", linewidth=2)
plt.plot(est_w_n, label="Estimated Reward (LOGEL)", marker="o", linewidth=2)
plt.xlabel("Region Feature Index")
plt.ylabel("Normalized Weight")
plt.title("Reward Recovery Comparison")
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("results_fig/fig1_right_reward_recovery.png", dpi=200)
print("Saved: results_fig/fig1_right_reward_recovery.png")
