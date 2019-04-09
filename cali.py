import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

p = np.array([759, 777, 792, 901, 926, 1035, 1089])
l = np.array([1/6301.508, 1/6302, 1/6302.499, 1/6305.81, 1/6306.565, 1/6309.886, 1/6311.504])

m, b, r_value, p_value, err = stats.linregress(p,l)

def cali(x):
	return 1/(m*x + b)

