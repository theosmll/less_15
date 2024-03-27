from fractions import Fraction

def operate_fractions(frac1, frac2):
    try:
        numerator1, denominator1 = map(int, frac1.split('/'))
        numerator2, denominator2 = map(int, frac2.split('/'))

        fraction1 = Fraction(numerator1, denominator1)
        fraction2 = Fraction(numerator2, denominator2)

        # Сумма дробей
        sum_fraction = fraction1 + fraction2

        # Произведение дробей
        product_fraction = fraction1 * fraction2

        return sum_fraction, product_fraction

    except ZeroDivisionError as e:
        print("Ошибка: деление на ноль.")
        return None, None
    except ValueError as e:
        print("Ошибка: неверный формат дроби.")
        return None, None
    except Exception as e:
        print("Произошла ошибка:", e)
        return None, None

if __name__ == "__main__":
    frac1 = input("Введите первую дробь в формате числитель/знаменатель: ")
    frac2 = input("Введите вторую дробь в формате числитель/знаменатель: ")

    sum_fraction, product_fraction = operate_fractions(frac1, frac2)

    if sum_fraction is not None and product_fraction is not None:
        print("Сумма дробей:", sum_fraction)
        print("Произведение дробей:", product_fraction)
