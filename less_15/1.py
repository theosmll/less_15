import argparse
import logging

def to_hex(num):
    try:
        if num == 0:
            return "0"

        hex_string = "{:X}".format(num)
        return hex_string
    except Exception as e:
        logging.error("Ошибка при конвертации числа в шестнадцатеричное представление: %s", e)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Программа для конвертации числа в шестнадцатеричное представление")
    parser.add_argument("num", nargs="?", type=int, help="Число для конвертации")
    parser.add_argument("--log", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Уровень логирования")
    args = parser.parse_args()

    if args.num is None:
        num = int(input("Введите число для конвертации в шестнадцатеричное представление: "))
    else:
        num = args.num

    if args.log:
        logging.basicConfig(level=args.log)  # Установка уровня логирования

    hex_representation = to_hex(num)
    if hex_representation is not None:
        print("Шестнадцатеричное представление числа:", hex_representation if hex_representation != "0" else "")
        print("Проверка результата:", hex(num))
