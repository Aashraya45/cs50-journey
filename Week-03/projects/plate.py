def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(number):
    return (
        start_check(number)
        and length_check(number)
        and end_check(number)
        and first_number_check(number)
        and punctuation_check(number)
    )


def start_check(number):
    return number[:2].isalpha()


def length_check(number):
    return 2 <= len(number) <= 6


def end_check(number):
    found_digit = False

    for letter in number:
        if letter.isdigit():
            found_digit = True
        elif found_digit:
            return False

    return True


def first_number_check(number):
    for letter in number:
        if letter.isdigit():
            return letter != "0"

    return True


def punctuation_check(number):
    for letter in number:
        if not (letter.isalpha() or letter.isdigit()):
            return False

    return True


main()