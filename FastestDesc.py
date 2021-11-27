import math
def FastestDesc(a, f, g, n, h, eps):
	y = [0] * (n + 1)
	y0 = [0] * (n + 1)
	r = [0] * (n + 1)
	r[0] = 0
	r[n] = 0
	k_NaiskSp = 0

	while True:  # Проверить ЦИКЛЫЫЫЫЫЫЫЫ
		for i in range(n - 1):
			r[i] = -a[i + 1] * (y0[i + 1] - y0[i]) + a[i] * (y0[i] - y0[i - 1]) + g[i] * math.pow(h, 2) * y0[i] - f[i]
		chislitel_tay = 0
		for i in range(n - 1):
			chislitel_tay += r[i] * r[i]
		levChast = [0] * (n + 1)
		for i in range(n - 1):
			levChast[i] = -a[i + 1] * (r[i + 1] - r[i]) + a[i] * (r[i] - r[i - 1]) + g[i] * math.pow(h, 2) * r[i]
		znamenatel_tay = 0
		for i in range(n - 1):
			znamenatel_tay = znamenatel_tay + levChast[i] * r[i]
		tay = chislitel_tay / znamenatel_tay
		for i in range(n - 1):
			y[i] = y0[i] - tay * r[i]
		k_NaiskSp += 1
		max = -1
		for i in range(n - 1):
			if (math.abs(y[i] - y0[i]) > max):
				max = math.abs(y[i] - y0[i])
			y0[i] = y[i]

		if (max > eps):
			break
	return y