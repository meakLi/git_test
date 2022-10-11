# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(names) > 3]
print(new_names)