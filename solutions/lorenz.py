from scipy.integrate import odeint

σ = 10
ρ = 28
β = 8 / 3


def lorenz(state, t):
    x, y, z = state

    # fill here
    x_p = σ * (y - x)
    y_p = (ρ - z) * x - y
    z_p = x * y - β * z

    return [x_p, y_p, z_p]


state0 = [2.0, 3.0, 4.0]
t = np.arange(0.0, 30.0, 0.01)
state = odeint(lorenz, state0, t)

# do some fancy 3D plotting
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection="3d")
ax.plot(*state.T, alpha=0.4)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
