import numpy as np
import matplotlib.pyplot as plt

#Funcion para encontrar el angulo horario

def v(t):
	b = (t-12)*15*np.pi/180	
	return np.sin(b)
h = np.array([v(9.383), v(10.15), v(10.9), v(11.65), v(12.43), v(12.65), v(12.85), v(12.983)])

#Importacion de los resultados de las velocidades y sus errores

dat = np.genfromtxt("Resultados/velocidades.txt")
vel = np.array(dat[:,1])
yerr = np.genfromtxt("Resultados/errores.txt")

#Definiendo los pesos estadisticos

w0 = 1/(yerr)**2

#Funciones para la regresion ponderada

def delta(x,w):
	return np.sum(w)*np.sum(w*x**2) - (np.sum(w*x))**2

#Intercepto y su error
def a0(x, y, w):
	n = np.sum(w*x**2)*np.sum(y*w) - np.sum(x*w)*np.sum(x*y*w)
	return n/delta(x, w)

def err_a0(x,w):
	n = np.sum(w*x**2)
	return np.sqrt(n/delta(x,w))

#Pendiente y su error
def a1(x, y, w):
	n = np.sum(w)*np.sum(x*y*w) - np.sum(x*w)*np.sum(y*w)
	return n/delta(x, w)

def err_a1(x,w):
	n = np.sum(w)
	return np.sqrt(n/delta(x,w))

a_0 = a0(h, vel, w0)
e_a0 = err_a0(h, w0)
a_1 = a1(h, vel, w0)
e_a1 = err_a1(h, w0)

#Funcion para encontrar el radio de la Tierra

def radio(v, t):
	return (v*t)/(2*np.pi)

#Definicion de un dia sideral en segundos y determinacion del volumen de la Tierra
T = 86164.1
R = radio(a_1, T)
V = (4/3)*np.pi*R**3

########################ERRORES######################################

##Error angulo horario##

def err_v(t):
	b=15*np.pi/180*(1/60)
	return b

h_erro=np.array([err_v(9.383), err_v(10.15), err_v(10.9), err_v(11.65), err_v(12.43), err_v(12.65), err_v(12.85), err_v(12.983)])


##Error radio tierra###

def error_radio(v,t,err_v):
	return (t/(2*np.pi))*(err_v)

R_err=error_radio(a_1, T, e_a1)

##Error volumen tierra###

V_err=4*np.pi*(R**2)*R_err 


print("Velocidad de la Tierra:", a_1, u"\u00B1", e_a1)
print("Radio de la Tierra:", R, u"\u00B1", R_err)
print("Volumen de la Tierra:", V, u"\u00B1", V_err)




