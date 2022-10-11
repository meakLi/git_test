# # 计算 30 以内可以被 3 整除的整数
# lis = []
# for i in range(30):
#     # print(i)
#     lis.append(i)
# print(lis)
# new_lis = [num for num in lis if num % 3 == 0]
# print(new_lis)

new_lis = [num for num in range(30) if num %3 == 0]
print(new_lis)