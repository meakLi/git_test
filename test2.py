# # 计算 30 以内可以被 3 整除的整数
# lis = []
# for i in range(30):
#     # print(i)
#     lis.append(i)
# print(lis)
# new_lis = [num for num in lis if num % 3 == 0]
# print(new_lis)

new_lis = [num for num in range(30) if num % 3 == 0]
print(new_lis)

# listdemo = ['Google','Runoob', 'Taobao']  将列表中各字符串值为键，各字符串的长度为值，组成键值对
listdemo = ['Google', 'Runoob', 'Taobao']
newdict = {str: len(str) for str in listdemo}
print(newdict)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
lis = [2, 6, 4]
newdict1 = {num: num ** 2 for num in lis}
print(newdict1)



# list1 = ['python', 'test1', 'test2']
# list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
# print(list2)

list1 = ['python', 'test1', 'test2']
# for word in list1:
#     print(word.title())  # 标题化，以大写字母开始
#     print(word.startswith('p'))  # 判断首字母是不是p
#     print(word.upper())  # 全部字母大写
# p开头的str首字母大写，不是p开头的str全部字母大写
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)