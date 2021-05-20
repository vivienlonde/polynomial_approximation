# polynomial_approximation

Two methods to approximate a function of the real variable by a polynomial:
- Chebyshev interpolation of the first kind.
- Polynomial fit (least squares).

Smooth functions like x -> log(x) can be approximated by low degree polynomials (say, degree 2 or 3).
Non differentiable functions like x -> max(x,0) require a higher degree polynomial approximation (say, degree 10).

It looks like x -> max(x,0) is better approximated by a polynomial fit than by Chebyshev interpolation.


