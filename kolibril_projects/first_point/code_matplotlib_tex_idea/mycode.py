import matplotlib.pyplot as plt

def f(x):
    return x**2
fig, ax = plt.subplots()
x= np.arange(0,100,1)
ax.plot(x, f(x))
