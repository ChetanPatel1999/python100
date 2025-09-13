#here we use calculator module

# import calculator
# print(calculator.add(12,5))
# print(calculator.sub(12,5))
# print(calculator.mul(5,4))

# from calculator import*   # its import all function from calculator

# print(add(4,7))
# print(sub(4,8))
# print(div(5,2))


# from calculator import add,sub

# print(add(12,8))
# print(sub(12,8))
# print(mul(12,8))   show error because we import only add, sub from calculator

import calculator as myclc

print(myclc.add(4,7))
print(myclc.add(56,7))
print(myclc.mul(5,8))