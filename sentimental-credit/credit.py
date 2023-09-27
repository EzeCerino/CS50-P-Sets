# TODO
from cs50 import get_string, get_int

def main():
    card_number = get_string("Insert Credit Card: ")
    if len(card_number) == 15 or len(card_number) == 16:
        check = checksum(card_number)
        type = check_type(card_number)
    else:
        print("Not Valid")
        return 0
    if check:
        print (type)
    else:
        print("Not Valid")


def checksum(card_number):
    if len(card_number) == 15:
        card_number = "0" + card_number
    sum1 = 0
    sum2 = 0
    for i in range(0,len(card_number),2):
        digit = str(int(card_number[i])*2)
        for j in range(len(digit)):
            sum1 = int(digit[j]) + sum1
    for i in range(1,len(card_number),2):
        sum2 = int(card_number[i]) + sum2
    if (sum1 + sum2) % 10 == 0:
        return True
    else:
        return False


def check_type(card_number):
    card_type = {
        "34": "AMEX",
        "37": "AMEX",
        "40": "VISA",
        "41": "VISA",
        "42": "VISA",
        "43": "VISA",
        "44": "VISA",
        "45": "VISA",
        "46": "VISA",
        "47": "VISA",
        "48": "VISA",
        "49": "VISA",
        "51": "MASTERCARD",
        "52": "MASTERCARD",
        "53": "MASTERCARD",
        "54": "MASTERCARD",
        "55": "MASTERCARD"
        }
    return card_type[card_number[0] + card_number[1]]


main()