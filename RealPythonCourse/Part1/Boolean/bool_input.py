var = input()
var_str = str(var)
var_str_len = len(var_str)
if var_str_len > 5:
    print('The characters in var are more than five:', var_str_len)
elif var_str_len == 5:
    print('The characters in var are exactly five')
else:
    print('The characters in var are less than five:', var_str_len)
