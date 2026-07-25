# CA Reservoir with Spatial Mask

# Experimenting with Reservoir Computing.

Examining the space-time tradeoffs when using in a Cellular Automata 
as a computational reservoir with spatial masking to speed-up the computation.

## Scientific Grounding: Dimensional Translation via Spatial Masking

The strategy implemented here—using a dense spatial mask to accelerate a slow temporal process—is a computational manifestation of **Time-Multiplexed Reservoir Computing**. 

In physical systems, when a substrate is too slow to process high-frequency temporal data, we can fold the temporal dimension into the spatial dimension. By passing a slow signal through a static, high-frequency spatial mask (a "grating"), the spatial interference creates a rapid temporal beat frequency that a slow reservoir can integrate. 

**Key Literature & Precedents:**
1. **Appeltant et al. (2011), *Nature Communications*:** "Information processing using a single dynamical node through liquid state machine." This foundational paper demonstrated that a single, slow nonlinear node (like a photonic circuit) could process complex, fast temporal signals by using a fast temporal mask to unfold the signal into a high-dimensional virtual state space.
2. **Larger et al. (2013), *Optics Express*:** Demonstrated this exact space-time folding in photonic delay reservoirs, proving that the "speed" of the computation is decoupled from the physical bandwidth of the node, bounded only by the resolution of the mask.

**Systems Synthesis:**
This mirrors biological architectures like the mammalian cochlea, which uses a spatial stiffness gradient (the basilar membrane) to translate slow, broad fluid waves into high-frequency, localized temporal firing rates in the auditory nerve. In both biology and this algorithm, "speed" is not a fundamental physical absolute, but an emergent property of spatial geometry.

## Run in the Cloud (No Installation Required)
Click the badge below to launch this notebook in a free, temporary cloud environment via Binder. It will take 1-2 minutes to build the environment on first click.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ceremona/CA-as-Reservoir/HEAD?labpath=CA-Reservoir-wSpatialMask.ipynb)

## Local Execution
If you prefer to run this locally using `uv`:
```bash
uv run jupyter notebook
