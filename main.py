import math
import numpy
import Jacobi


def main():
	n = 40
	h = 1/n
	eps = pow(h, 3)

	alpha = 2
	beta = 3
	gamma = 2

	g = lambda x: 1 + x
	p = lambda x: 1 + pow(x, gamma)
	u = lambda x: pow(x, alpha)*pow((1-x), beta)
	#  u(x) = x^2*(1-x)^3
	#  u'(x) = -3*x^2*(1-x)^2 + 2*x*(1-x)^3
	d_u = lambda x: -beta*pow(x, alpha)*pow((1-x), beta-1) + alpha*pow(x, alpha-1)*pow((1-x), beta)


	ai = numpy.array([p(i*h) for i in range(n)])

	ui = numpy.array([u(i*h) for i in range(n)])
	qi = numpy.array([g(i*h) for i in range(n)])

	# ((1+x^gamma)*(-3*x^2*(1-x)^2 + 2*x*(1-x)^3))'
	# (-3*x^2*(1-x)^2 + 2*x*(1-x)^3)+x^gamma*((-3*x^2*(1-x)^2 + 2*x*(1-x)^3))'



	left_f = lambda x: (
							- beta*alpha*pow(x, alpha-1)*pow((1-x), beta-1) +
							beta*pow(x, alpha)*(beta-1)*pow(1-x, beta-2) +
							alpha*(alpha-1)*pow(x, alpha-2)*pow(1-x, beta) -
							alpha*pow(x, alpha-1)*beta*pow(1-x, beta-1) -
							beta*(alpha+gamma)*pow(x, alpha+gamma-1)*pow((1-x), beta-1) +
							beta*pow(x, alpha+gamma)*(beta-1)*pow(1-x, beta-2) +
							alpha*(alpha+gamma-1)*pow(x, alpha+gamma-2)*pow(1-x, beta) -
							alpha*pow(x, gamma+alpha-1)*beta*pow(1-x, beta-1)
						)
	left_fi = numpy.array([left_f(i*h) for i in range(n)])

	fi = ui*qi - left_fi

	y, num_iter_jacobi = Jacobi.jacobi(ai, fi, qi, n, h, eps)

	print(num_iter_jacobi)



if __name__ == "__main__":
	main()


