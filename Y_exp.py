def raise_to_power(base_num,pow_num):
    result = 1
    for num_series in range(pow_num):
        result = result * base_num 
    return result


print(raise_to_power(3,6))