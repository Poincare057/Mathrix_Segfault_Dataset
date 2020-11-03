y = []  # file for storing data


def x_age_y_respiratory():
    s = 0
    for a in range(94):  # population of 75000 people
        y1 = (((-0.000689416)*(a**4))+(0.114414*(a**3)) +
              ((-5.60248)*(a**2))+(82.0383*(a))+(452.791))/75000  # 4 degree polynomial
        if y1 >= 0:
            s += y1
            y.append(y1)
            print(a, ' : ', y1)

    print(s)


x_age_y_respiratory()
