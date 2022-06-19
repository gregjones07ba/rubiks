from math import isclose

def vectors_equal(v1, v2, abs_tol=1e-09):
    return all(isclose(c1, c2, abs_tol=abs_tol)
               for c1, c2 in
               zip(v1, v2))
