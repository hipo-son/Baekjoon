num1 = input()
num2 = input()

num3 = int(num2[2]) * int(num1) # num2의 일의자리
num4 = int(num2[1]) * int(num1) # num2의 십의자리
num5 = int(num2[0]) * int(num1) # num2의 백의자리
num6 = num3 + (num4 * 10) + (num5 * 100)

print(num3)
print(num4)
print(num5)
print(num6)

# num1 = int(input())
# num2 = int(input())
#
# num2_1 = int(num2 % 10) # 두번째 input값의 일의자리
# num2_10 = int((num2 % 100 - num2_1) / 10) # 두번째 input값의 십의자리
# num2_100 = int(((num2 - num2_10 * 10) - num2_1) / 100) # 두번째 input값의 백의자리
# 문자열로 풀자
