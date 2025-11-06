import numpy as np
import matplotlib.pyplot as plt

disc = np.load("../agent_trajectories/GPOMDP/disc_ret_GPOMDP_2.npy")

plt.figure(figsize=(5,3.5))
plt.plot(disc, linewidth=2)
plt.xlabel("Learning Step")
plt.ylabel("Discounted Return")
plt.title("GPOMDP Training Curve")
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("results_fig/fig1_left_training_curve.png", dpi=200)
print("Saved: results_fig/fig1_left_training_curve.png")
