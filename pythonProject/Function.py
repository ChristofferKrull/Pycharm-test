def function1(x, y):
    print(x * y)
    print(x + y)
    print("du är kung")
    return 3 * x


a = function1(4, 7)
print(function1)

r = function1(6, 2)
print(r)

namn = "christoffer"
langd = 1.83
vikt = 81

def bmi_calc(namn, langd, vikt):
    bmi = vikt / (langd ** 2)
    return bmi
print("Ditt bmi är:")
print(bmi_calc(namn,langd, vikt))
