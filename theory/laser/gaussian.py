import numpy as np
import matplotlib.pyplot as plt

z_max = 3
r_max = 5
z_r = 1
w_0 = 1
I_0 = 1

z_list = np.linspace(0, z_max, 300)
r_list = np.linspace(-r_max, r_max, 300)
Z, R = np.meshgrid(z_list, r_list)

def div(z, A, B):
    return A * np.sqrt(1 + (z / B) ** 2)

def gaussian(r, A, B):
    return A * np.exp(-2 * r**2 / B**2)

def radiance(z, r):
    w = div(z, w_0, z_r)
    return gaussian(r, I_0 * (w_0 / w)**2, w)

I = radiance(Z, R)

plt.figure('Irradiance faisceau laser gaussien')
extent = [z_list.min(), z_list.max(), r_list.min(), r_list.max()]
plt.imshow(I, extent=extent, aspect='auto', cmap='inferno')
plt.xlabel('Distance laser/réception (m)')
plt.ylabel('Rayon (mm)')
plt.title('Irradiance du faisceau laser gaussien (valeurs arbitraires)')
plt.colorbar(label=r'Irradiance ($W \cdot m^{-2}$)')
plt.tight_layout()
plt.show()