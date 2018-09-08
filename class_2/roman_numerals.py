def int_to_roman(int_):
    result = int_ // 1000 * "M"
    result += calculate(int_ % 1000 // 100, "C", "D", "M")
    result += calculate(int_ % 100 // 10, "X", "L", "C")
    result += calculate(int_ % 10, "I", "V", "X")
    return result


def calculate(num, ones, fives, tens):
    romans = {
            0:  '',
            1: num * ones,
            2: num * ones,
            3: num * ones,
            4: ones + fives,
            5: fives,
            6: fives + ones,
            7: fives + 2 * ones,
            8: ones * 2 + tens,
            9: ones + tens,
            10: tens,
            }

    return romans[num]

print("Roman numeral of {} is {}".format(9, int_to_roman(9)))
print("Roman numeral of {} is {}".format(947, int_to_roman(947)))
print("Roman numeral of {} is {}".format(1215, int_to_roman(1215)))
print("Roman numeral of {} is {}".format(490, int_to_roman(490)))

