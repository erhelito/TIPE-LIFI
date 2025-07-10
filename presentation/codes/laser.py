import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from scipy.optimize import curve_fit
import seaborn as sns

def gauss(x, A, B): 
	y = A*np.exp(-2*x**2/(B**2))
	return y	

def div(x,A,B):
	y = A*np.sqrt(1+(x/B)**2)
	return y

def get_r_v(z):
    global cur
    cur.execute(f'SELECT data.Radius, data.Voltage FROM data WHERE data.distance = {z} AND data.radius >= {0} ORDER BY data.Radius')
    rows = cur.fetchall()
    r = np.array([row[0] for row in rows])
    v = np.array([row[1] for row in rows])
    return np.array(r),np.array(v)

conn = sqlite3.connect('V2/data2.db')
cur = conn.cursor()

z_list = cur.execute('SELECT DISTINCT data.distance FROM data ORDER BY data.distance').fetchall()
z_list = [z[0] for z in z_list]
W_list = []

for z in z_list:
    R,V = get_r_v(z)
    parameters,covariance = curve_fit(gauss, R, V)
    fit_A = parameters[0]
    fit_B = parameters[1]

    W_list.append(fit_B)

    fit_r = np.linspace(min(R), max(R), 100)
    fit_v = gauss(fit_r, fit_A, fit_B)

    plt.figure(f'Matrice de covariance gaussienne z={z}m')
    plt.title(f'Matrice de covariance gaussienne z={z}m')
    sns.heatmap(covariance, annot=True, xticklabels=['Amplitude (V)', 'w(z) (mm)'], yticklabels=['Amplitude (V)', 'w(z) (mm)'], cmap='viridis')
    plt.figure(f'Tension au fil du rayon (z={z})')
    plt.plot(R,V, marker='+', linestyle='dotted', markersize=10, label='Mesures')
    plt.plot(fit_r, fit_v, color='orange', label='Régression')
    plt.grid()
    plt.xlabel('Rayon (mm)')
    plt.ylabel('Tension (V)')
    plt.title(f'Évolution de la tension au fil du rayon, z={z}m')
    plt.tight_layout()
    plt.legend()

z_list, W_list = np.array(z_list),np.array(W_list)

parameters,covariance = curve_fit(div, z_list, W_list)
fit_A = parameters[0]
fit_B = parameters[1]

plt.figure('Matrice de covariance rayon caractéristique')
plt.title('Matrice de covariance rayon caractéristique')
sns.heatmap(covariance, annot=True, xticklabels=[r'${W_0}$ (mm)', r'${z_r}$ (m)'], yticklabels=[r'${W_0}$ (mm)', r'${z_r}$ (m)'], cmap='viridis')

print(f'W0 = {fit_A}, zr = {fit_B}')

fit_z = np.linspace(min(z_list), max(z_list), 100)
fit_w = div(fit_z, fit_A, fit_B)

plt.figure('Rayon caractéristique distance')
plt.plot(z_list, W_list, marker='+', linestyle='dotted', markersize=10, label='Mesures')
plt.plot(fit_z, fit_w, color='orange', label='Régression')
plt.xlabel('Distance laser/réception (m)')
plt.ylabel('Rayon caractéristique (mm)')
plt.title('Rayon caractéristique au fil de la distance')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

