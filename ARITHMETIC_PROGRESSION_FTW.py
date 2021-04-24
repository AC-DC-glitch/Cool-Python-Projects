import math


def ap_func():
    term_a = input("Enter the first term. If you don't know it, simply press ENTER: ")
    if term_a == "":
        pass
    else:
        term_a = float(term_a)

    nterm = input("Input the number of terms. If you don't know it, simply press ENTER: ")
    if nterm == "":
        pass
    else:
        nterm = float(nterm)

    cd = input("Enter the common difference. If you don't know it, simply press ENTER: ")
    if cd == "":
        pass
    else:
        cd = float(cd)

    nth_term = input("Enter the nth term. If you don't know it, simply press ENTER: ")
    if nth_term == "":
        pass
    else:
        nth_term = float(nth_term)

    nsum = input("Enter the sum of terms. If you don't know it, simply press ENTER: ")
    if nsum == "":
        pass
    else:
        nsum = float(nsum)

    if term_a == "" and nterm == "":
        term_a = (cd + math.sqrt(math.pow(cd, 2)+4*(math.pow(nth_term, 2)-(2*cd*nsum)+(cd*nth_term))))/2
        nterm = ((nth_term - term_a) / cd) + 1
        print("The 1st term is", term_a, "and the number of terms is", nterm)

    if term_a == "" and cd == "":
        term_a = ((2 * nsum) - (nterm * nth_term)) / nterm
        cd = (nth_term - term_a) / (nterm - 1)
        print("The 1st term is ", term_a, " and the common difference is ", cd)

    if term_a == "" and nth_term == "":
        term_a = ((2 * nsum) - (nterm * (nterm - 1) * cd)) / (2 * nterm)
        nth_term = ((2 * nsum) - (term_a * nterm)) / nterm
        print("The 1st term is ", term_a, " and the nth term is ", nth_term)

    if term_a == "" and nsum == "":
        term_a = nth_term - ((nterm - 1) * cd)
        nsum = (nterm / 2) * (nth_term + term_a)
        print("The first term is ", term_a, " and the sum of all terms is ", nsum)

    if nterm == "" and cd == "":
        nterm = 2 * nsum / (term_a + nth_term)
        cd = (nth_term - term_a) / (nterm - 1)
        print("The number of terms is ", nterm, " and the common difference is ", cd)

    if nterm == "" and nth_term == "":
        nth_term = (-cd + math.sqrt(math.pow(cd, 2) + 4*(term_a - term_a*cd + 2*nsum*cd)))/2
        nterm = ((nth_term - term_a) / cd) + 1
        print("The number of terms is", nterm, "and the nth term is", nth_term)

    if nterm == "" and nsum == "":
        nterm = ((nth_term - term_a) / cd) + 1
        nsum = (nterm / 2) * (2 * term_a + (nterm - 1) * cd)
        print("The number of terms is ", nterm, " and the sum of 'n' terms is ", nsum)

    if cd == "" and nth_term == "":
        cd = ((2 * nsum) - (2 * term_a * nterm)) / (nterm * (nterm - 1))
        nth_term = ((2 * nsum) - (term_a * nterm)) / nterm
        print("The common difference is ", cd, " and the nth term is ", nth_term)

    if cd == "" and nsum == "":
        cd = (nth_term - term_a) / (nterm - 1)
        nsum = (nterm / 2) * (term_a + nth_term)
        print("The common difference is ", cd)
        print("The sum of the first n terms is ", nsum)

    if nth_term == "" and nsum == "":
        nth_term = (term_a + ((nterm - 1) * cd))
        nsum = (nterm / 2) * (2 * term_a + (nterm - 1) * cd)
        print("The nth term is ", nth_term)
        print("The sum of the 1st n terms of the AP is ", nsum)


ap_func()
