# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "pillow",
# ]
# ///

import numpy as np
import matplotlib
matplotlib.use('Agg') #Decouples computation from display; allows headless execution.
import matplotlib.pyplot as plt
plt.style.use('dark_background')

from matplotlib.animation import FuncAnimation, PillowWriter

# --- 1. Setup the CA Topology (Rule 90) ---
N = 500       # Spatial cells: The spatial resolution (degrees of freedom).
T = 300       # Time steps: The temporal observation window.
lr = 0.3      # Leak rate: Controls thermodynamic dissipation (memory decay).
sr = 0.9      # Spectral radius: Controls the edge of chaos (nonlinear amplification).

# Nearest-neighbor coupling defines the "speed of light" 
# in this discrete universe. Information can only propagate 1 cell per time step.
W = np.zeros((N, N))
for i in range(N):
    W[i, (i-1)%N] = 1.0  # Left neighbor coupling
    W[i, (i+1)%N] = 1.0  # Right neighbor coupling

# --- 2. Generate the Spatial Mask (PRBS) ---
# Maximum Entropy Grating: A Pseudo-Random Binary Sequence 
# ensures the spatial mask has the highest possible linear independence, 
# preventing the reservoir states from collapsing into a low-dimensional subspace.
np.random.seed(42)
mask = (np.random.rand(N) > 0.5).astype(float)

# --- 3. Pre-compute Space-Time States ---
raw_states = np.zeros((T, N))
masked_states = np.zeros((T, N))

x = np.zeros(N)
x[N//2] = 1.0 # Initial perturbation: The "seed" of information.

for t in range(T):
    # [PHYSICS] Leaky Integration & Nonlinearity: 
    # The tanh function provides the nonlinear mixing required for computation.
    # The leak rate (lr) guarantees a negative Lyapunov exponent, ensuring the 
    # system possesses "fading memory" and won't trap itself in infinite echoes.
    x_next = (1 - lr) * x + lr * np.tanh(sr * (W @ x))
    x = x_next
    
    raw_states[t] = x
    
    # Dimensional Translation: 
    # Multiplying the slow, broad spatial wave by the dense static mask 
    # forces the spatial gradients to alias into high-frequency temporal noise.
    # "space" => "time".
    masked_states[t] = x * mask

# --- 4. Setup Animation Figure ---
# Mapping the high-dimensional, abstract state space 
# back into a human-perceptible 2D geometric plane.
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Evolution of Space-Time Tradeoff", fontsize=16, color='white')

x_axis = np.arange(N)

# Brighter colors for dark background visibility (High contrast signal extraction)
line1, = ax1.plot([], [], color='#ff4d4d', lw=1.5, label='Raw CA State')
line2, = ax2.plot([], [], color='#00ffff', lw=1.5, label='Masked CA State (Simulated Fast Signal)')

# Format axes
for ax in (ax1, ax2):
    ax.set_xlim(0, N)
    ax.set_ylim(-1.1, 1.1)
    ax.set_ylabel("State Amplitude", color='white')
    ax.tick_params(colors='white')
    ax.legend(loc='upper right', facecolor='#222222', edgecolor='white', labelcolor='white')

ax2.set_xlabel(f"Spatial Cells (N={N})", color='white')

# Adjusted text box for dark mode
time_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes, fontsize=12,
                     verticalalignment='top', color='white',
                     bbox=dict(boxstyle='round', facecolor='#333333', edgecolor='white', alpha=0.8))

# --- 5. Animation Update Function ---
# The readout mechanism stepping through the 
# pre-computed high-dimensional states 
def update(frame):
    line1.set_data(x_axis, raw_states[frame])
    line2.set_data(x_axis, masked_states[frame])
    time_text.set_text(f"Time Step (Slow Clock): {frame}")
    return line1, line2, time_text

# --- 6. Generate and Save GIF ---
print("Generating animation...")
ani = FuncAnimation(fig, update, frames=T, interval=50, blit=True)

writer = PillowWriter(fps=20)
ani.save("ca_evolution.gif", writer=writer)

print("Animation complete. Saved to ca_evolution.gif")
