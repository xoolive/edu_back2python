fig, ax = plt.subplots(figsize=(10,10))
t = np.arange(0., 5., .2)
ax.plot(t, np.exp(-t)*np.cos(2*np.pi*t))