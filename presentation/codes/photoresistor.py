import numpy as np
import matplotlib.pyplot as plt

# res de mesure
R_mes = 215

I_global = []
U_photo_global = []
i_mes_global = []
E = np.array([0,0.49,0.98,1.47,1.96,2.45,2.94])

def store(I,U_R):
    U_photo = E - U_R
    i_mes = U_R / R_mes

    I_global.append(I)
    U_photo_global.append(U_photo)
    i_mes_global.append(i_mes)

I_global = np.array(I_global)
U_photo_global = np.array(U_photo_global)
i_mes_global = np.array(i_mes_global)

### FIRST PLOT ###
fig = plt.figure('Données brutes')
ax = fig.add_subplot(projection='3d')

for i in range(len(I_global)) :
    ax.plot(i_mes_global[i],U_photo_global[i], I_global[i], marker = '+', markersize=10)

plt.title('Lien entre intensité, tension et éclairement lumineux')
ax.set_xlabel('Intensité (A)')
ax.set_ylabel('Tension (V)')
ax.set_zlabel('Éclairement lumineux (lx)')
plt.tight_layout()
ax.grid()

### LINEAR REGRESSION ###
R = []
R_square = []

for i in range(len(I_global)) :
    vec = np.polyfit(i_mes_global[i], U_photo_global[i],1)
    R.append(vec[0])
    U_reg = i_mes_global[i]*vec[0]
    err_quadratique = np.sum((U_photo_global[i] - U_reg)**2)
    ecart_type = np.sum((U_photo_global[i] - np.mean(U_photo_global[i]))**2)
    R_square.append(1-err_quadratique/ecart_type)

R = np.array(R)

min_R_square = min(R_square)
min_R_square = round(min_R_square,3)

fig = plt.figure('Régression linéaire 1')

plt.plot(I_global,R, marker='+', linestyle='dotted', markersize=10)
plt.title(r'Lien entre éclairement lumineux et resistance, $R^2 = $' + str(min_R_square))
plt.xlabel('Éclairement lumineux (lx)')
plt.ylabel(r'Resistance ($\Omega$)')
plt.tight_layout()
plt.grid()

### LOI PHOTORESISTANCE ###
new_R = 1/R

vec = np.polyfit(I_global,new_R,1)
I_lin = np.linspace(min(I_global),max(I_global),100)
reg = vec[0]*I_lin + vec[1]

err_quadratique = np.sum((U_photo_global[i] - U_reg)**2)
ecart_type = np.sum((U_photo_global[i] - np.mean(U_photo_global[i]))**2)

R_square = (1-err_quadratique/ecart_type)
R_square = round(R_square,4)

fig = plt.figure('Régression linéaire 2')
plt.plot(I_global,new_R, marker='+', linestyle='dotted', markersize=10, label='Mesures')
plt.plot(I_lin,reg, color='orange', label='Régression')
plt.title(r'Régression linéaire, $R^2 = $' + str(R_square))
plt.xlabel('Éclairement lumineux (lx)')
plt.ylabel(r'1/R ($\Omega^{-1}$)')
plt.legend()
plt.tight_layout()
plt.grid()

R_reg = 1/reg

fig = plt.figure('Loi fonctionnement photorésistance')
plt.plot(I_global,R, marker='+', linestyle='dotted', markersize=10, label='Mesures')
plt.plot(I_lin,R_reg, color='orange', label='Régression')
plt.title('Loi de fonctionnement de la photorésistance')
plt.xlabel('Éclairement lumineux (lx)')
plt.ylabel(r'Résistance ($\Omega$)')
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()

