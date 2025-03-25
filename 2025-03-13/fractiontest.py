from fractions import Fraction

frac = Fraction(1, 2)

print(frac)
print(frac.numerator)
print(frac.denominator)
print(float(frac))
one_fourth = Fraction(1, 4)
print(f'{frac} + {one_fourth} = {frac + one_fourth}')