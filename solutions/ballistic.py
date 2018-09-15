import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import odeint


def forces(state, t):
    m = 20.  # kilograms
    g = np.array([0, -9.8])  # metres per second

    v2 = sum(state[2:] ** 2)
    f = .5 * .5 * 1.184 * .1 * v2

    dstate = state.copy()
    dstate[:2] = state[2:]
    dstate[2:] = g - f / m * state[2:] / np.sqrt(v2)

    return dstate


# x_0, z_0, \dot{x}_0, \dot{z}_0
state0 = np.array([0., 100., 100., 100.])

t = np.arange(0.0, 30.0, 0.1)

state2 = odeint(forces, state0, t)
state2 = state2[np.where(state2[:, 1] >= 0)]

plt.plot(state[:, 0], state[:, 1])
plt.plot(state2[:, 0], state2[:, 1])

plt.xlabel("x")
plt.ylabel("z")
