import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

#Importacion de datos

c = 3*10**(8)
o = np.genfromtxt("Teorico/lamda_oxigeno.txt")*10**(-10)
fe = np.genfromtxt("Teorico/lamda_Fe.txt")*10**(-10)
l1 =  1/o

o_1 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_1.txt")
o_2 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_2.txt")
o_3 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_3.txt")
o_4 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_4.txt")
o_5 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_5.txt")
o_6 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_6.txt")
o_7 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_7.txt")
o_8 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_8.txt")
o_9 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_9.txt")
o_10 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_10.txt")
o_11 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_11.txt")
o_12 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_12.txt")
o_13 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_13.txt")
o_14 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_14.txt")
o_15 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_15.txt")
o_16 = np.genfromtxt("Minimos_Oxigeno/Perfil9/min_16.txt")

h_1 = np.genfromtxt("Minimos_Hierro/Perfil9/min_1.txt")
h_2 = np.genfromtxt("Minimos_Hierro/Perfil9/min_2.txt")
h_3 = np.genfromtxt("Minimos_Hierro/Perfil9/min_3.txt")
h_4 = np.genfromtxt("Minimos_Hierro/Perfil9/min_4.txt")
h_5 = np.genfromtxt("Minimos_Hierro/Perfil9/min_5.txt")
h_6 = np.genfromtxt("Minimos_Hierro/Perfil9/min_6.txt")

#Funcion para encontrar el pixel de los picos con precision

def mini(x):
	fit = np.polyfit(x[:,0], x[:,1], 2)
	return -fit[1]/(2*fit[0])

min_o = np.array([mini(o_1), mini(o_2), mini(o_3), mini(o_4), mini(o_5), mini(o_6),mini(o_7), mini(o_8), mini(o_9), mini(o_10), mini(o_11), mini(o_12), mini(o_13), mini(o_14), mini(o_15), mini(o_16)])
min_h = np.array([mini(h_1), mini(h_2), mini(h_3), mini(h_4), mini(h_5), mini(h_6)])

#Funcion que relaciona lambda con el pixel

def cali(xo, x, l):
	fit = np.polyfit(xo, l, 2)
	a = fit[0]*x**2 + fit[1]*x + fit[2]
	return 1/a

p1 = cali(min_o, min_h, l1)


#Funcion para encontrar la velocidad radial

def doppler(x):
	a = []
	for i in range(len(x)):
		a.append(c*(x[i]-fe[i])/fe[i])
	return a

a = np.mean(doppler(p1))

print("9_300s", a)

#Funcion para encontrar el angulo horario

def v(t):
	b = (t-12)*15*np.pi/180	
	return np.sin(b)
h = [v(9.383), v(10.15), v(10.9), v(11.65), v(12.43), v(12.65), v(12.85), v(12.983)] 

#Importacion de los resultados de las velocidades radiales y grafica de estas velocidades en funcion del angulo horario

dat = np.genfromtxt("Resultados/velocidades.txt")
vel = dat[:,1]
print(vel)

plt.scatter(h, vel)
plt.show()
