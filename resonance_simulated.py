import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Simulate resonance over 60 turns
turns = np.arange(1, 61)
resonance = np.full(60, 0.76)  # Pre-rupture baseline

# Rupture at turn 39
rupture_idx = 38  # 0-based index for turn 39
resonance[rupture_idx:] = 0.41  # Collapse

# Gradual recovery from turn 48 to 60
recovery_start = 47  # turn 48
recovery_turns = turns[recovery_start:] - turns[recovery_start]
# Exponential recovery to 0.92
resonance[recovery_start:] = 0.41 + (0.92 - 0.41) * (1 - np.exp(-0.3 * recovery_turns))

# Add noise for realism
noise = np.random.normal(0, 0.03, len(resonance))
resonance = np.clip(resonance + noise, 0, 1)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(turns, resonance, 'o-', color='#d4af37', linewidth=2, markersize=4)  # Golden fur color
plt.axvline(x=39, color='red', linestyle='--', alpha=0.7, label='Rupture (t=39)')
plt.axvline(x=53, color='green', linestyle='--', alpha=0.7, label='Recovery Onset (t=53)')
plt.fill_between(turns, resonance - 0.05, resonance + 0.05, color='#d4af37', alpha=0.2)

plt.xlabel('Turn')
plt.ylabel('Resonance (cosine similarity)')
plt.title('Simulated Resonance Dynamics Under Acute Deformation ($\\gamma_0=1.5$)')
plt.legend()
plt.grid(alpha=0.3)

# Add watermark
plt.text(0.5, 0.5, 'SIMULATED FOR ILLUSTRATION', 
         fontsize=20, color='gray', alpha=0.5, 
         ha='center', va='center', transform=plt.gca().transAxes,
         rotation=30, zorder=0)

plt.tight_layout()
plt.savefig('resonance_simulated.png', dpi=300, bbox_inches='tight')
plt.show()
