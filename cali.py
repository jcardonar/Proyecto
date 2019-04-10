import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

c = 3*10**(8)
p = np.array([760, 776, 793, 902, 926, 1036, 1090])
teo = np.array([6301.508, 6302, 6302.499, 6305.81, 6306.565, 6309.886, 6311.504])*10**(-10)
l = 1/teo

m, b, r_value, p_value, err = stats.linregress(p,l)

def cali(x):
	return 1/(m*x + b)

def doppler(x):
	a = []
	for i in range(len(x)):
		a.append(c*(x[i] - teo[i])/teo[i])
	return a

