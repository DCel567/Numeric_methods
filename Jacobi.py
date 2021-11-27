import numpy


def jacobi(ai: numpy.ndarray, fi: numpy.ndarray, gi: numpy.ndarray, n: int, h: float, eps: float):
	y_pred = [] * n
	r = 1
	num_iter = 0

	y = [i for i in range(n)]
	print(f'y = {y}')

	while (r > eps):

		y_pred = y.copy()
		#  для вычисления yk
		for i in range(1, n - 1):
			#  вычисление yki
			y[i] = (fi[i] * h ** 2 + ai[i + 1] * y_pred[i + 1] + ai[i] * y_pred[i - 1]) / (
						ai[i] + ai[i + 1] + gi[i] * h * h)
		num_iter += 1
		print(f'yk = {y}')

		for i in range(1, n-1):
			r_curr = abs(-ai[i + 1] * y[i + 1] + (ai[i + 1] + ai[i] + gi[i] * h * h) * y[i] - ai[i] * y[i - 1] - fi[i])
			if r_curr > r:
				r = r_curr
		print(f'r = {r}')

	return (y, num_iter)

