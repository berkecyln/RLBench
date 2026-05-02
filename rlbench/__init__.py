__version__ = '1.2.0'

# pyrep/CoppeliaSim not required for data conversion (prepare_data_for_peract.py).
# Simulation-dependent imports are guarded so the package can be used headlessly.
try:
    import numpy as np
    import pyrep

    pr_v = np.array(pyrep.__version__.split('.'), dtype=int)
    if pr_v.size < 4 or np.any(pr_v < np.array([4, 1, 0, 2])):
        raise ImportError(
            'PyRep version must be greater than 4.1.0.2. Please update PyRep.')

    from rlbench.environment import Environment
    from rlbench.action_modes.action_mode import ActionMode, ArmActionMode, GripperActionMode
    from rlbench.sim2real.domain_randomization import RandomizeEvery
    from rlbench.sim2real.domain_randomization import VisualRandomizationConfig
except ModuleNotFoundError:
    pass

# These don't need pyrep — always export them
from rlbench.observation_config import ObservationConfig
from rlbench.observation_config import CameraConfig
