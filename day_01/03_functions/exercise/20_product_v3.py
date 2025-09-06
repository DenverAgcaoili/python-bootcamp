def product(num1:int,num2:int,num3:int=1):
    """ TODO: Takes three inputs (or two) and return"""
    result = (num1 * num2 * num3)
    return result


# TODO: product(1, 1, 1)	# 1
# TODO: product(1, 2, 3)	# 6
# TODO: product(2, 5, 10)	# 100
# TODO: product(3, 3)	    # 9
# TODO: product(2, 5)	    # 12

computed_result = product(1,1,1)
print(computed_result)

computed_result = product(1,2,3)
print(computed_result)

computed_result = product(2,5,10)
print(computed_result)

computed_result = product(3,3)
print(computed_result)

computed_result = product(2,5)
print(computed_result)