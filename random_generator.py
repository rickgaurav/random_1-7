from random import randint


def rand1to5():
    return randint(1, 5)


def rand1to7():
    """
    Logic:
    1. The logic somehow generate the integers from 1 to a multiple of 7 (7, 14, 21 ..) with equal probability. Lets call it "number".
    2. Then we use (number % 7) + 1 to generate a number in range of 1 to 7 with equal probability.
    :return: an integer in range of 1-5.
    """

    # This will generate numbers in range of [1,25]
    number = 5*rand1to5() + rand1to5() - 5

    if number < 22:
        return (number % 7) + 1
    return rand1to7()

if __name__ == '__main__':

    print "Random number generated is {}".format(rand1to7())

    n = 1000000

    print "Running a test on function for a range of 1 to {}".format(n)

    count_1 = count_2 = count_3 = count_4 = count_5 = count_6 = count_7 = 0

    for num in range(0, n):
        num = rand1to7()

        if num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1
        elif num == 3:
            count_3 += 1
        elif num == 4:
            count_4 += 1
        elif num == 5:
            count_5 += 1
        elif num == 6:
            count_6 += 1
        elif num == 7:
            count_7 += 1

    print "1 occurred {}% times".format((float(count_1*100))/n)
    print "2 occurred {}% times".format((float(count_2*100))/n)
    print "3 occurred {}% times".format((float(count_3*100))/n)
    print "4 occurred {}% times".format((float(count_4*100))/n)
    print "5 occurred {}% times".format((float(count_5*100))/n)
    print "6 occurred {}% times".format((float(count_6*100))/n)
    print "7 occurred {}% times".format((float(count_7*100))/n)

