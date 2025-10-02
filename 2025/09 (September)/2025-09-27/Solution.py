import re

def is_spam(number):
    number_no_symbols = re.sub(r"[\+\(\)\-]", "", number)
    country_code, area_code, local_number = number_no_symbols.split(" ")

    if len(country_code) > 2 or not country_code.startswith('0'):
        return True
        
    if not 900 >= int(area_code) >= 200:
        return True
    
    sum_first_three = sum([int(n) for n in local_number[:3]])
    if str(sum_first_three) in local_number[-4:]:
        return True
    
    combined_number = country_code + area_code + local_number
    if re.search(r"(.)\1{3}", combined_number):
        return True

    return False