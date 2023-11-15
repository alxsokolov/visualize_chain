import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits import mplot3d
import pdb


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig=plt.figure()
ax=plt.axes(projection='3d')

dir_name = 'RectangularDataEquil'
path= os.path.join('data', dir_name)
data=os.listdir(path)

plot_every_n_steps = 5 

def sort_key(value):
    return int(value.split(".")[0])

data = sorted(data, key=sort_key)[::plot_every_n_steps]

n_particles = np.loadtxt(os.path.join(path, '0.dat')).shape[0] 
n=np.arange(-int((n_particles-1)/2), int((n_particles-1)/2) + 1)
u=np.zeros(n_particles)

for item in data:
    if 'dat' in item:
        u=np.loadtxt(os.path.join(path, item))
        t=np.ones(n_particles)*int(item.strip('.dat'))*2*np.pi*1e-2
        ax.plot(t, n, u[:,2], 'k')
        ax.set_ylabel(r'$n$')
        ax.set_xlabel(r'$t\omega_0$')
        ax.set_zlabel(r'$u$')

ax.azim = 50 
ax.elev = 40
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)
plt.savefig(dir_name+".pdf", format="pdf", bbox_inches="tight")
plt.show()
