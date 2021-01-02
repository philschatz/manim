import matplotlib.pyplot as plt

def f2(x):
    return np.sin(x)
fig, ax = plt.subplots()
x= np.arange(0,20,0.1)
ax.plot(x, f2(x))