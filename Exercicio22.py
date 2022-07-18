def pattern(number, array=[]):
    array.append(number)
    if number <= 0:
        for n in [*array, *array[-2::-1]]:
            print(n)
        array.clear()
        return number
    else:
        return pattern(number-5)