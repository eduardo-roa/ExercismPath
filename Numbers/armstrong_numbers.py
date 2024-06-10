def is_armstrong_number(number):
    number=str(number)
    exp = len(number)
    sum = 0
    for i in number:
        sum = sum + (int(i)**exp)

    return sum == int(number)
    