# Calculating the Value of a Polynomial


def calc_poly(const_seq, var_poly):
    return round(sum([const_seq[i] * var_poly**i for i in range(len(const_seq))]), 2)


# test cases
def test_cases():
    print(calc_poly([0, -2.34, 0, 1.2], 2))
    print(calc_poly([1, 0.2, -342, 4.37], 6))
    print(calc_poly([0], 2))


test_cases()
