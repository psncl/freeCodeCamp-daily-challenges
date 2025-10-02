def to_binary(decimal):
    binary = ""
    quotient = None
    remainder = None

    while True:
        remainder = decimal % 2        
        quotient = decimal // 2

        binary = str(remainder) + binary
        
        if quotient == 0:
            break

        decimal = quotient

    return binary