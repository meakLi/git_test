# 将两个列表合成一个列表，重复的部分只保留一个
class UniqueNames:
    # 基本属性，调用类属性用到
    name = 'meak'
    age = 18

    # 构造方法，构造实例对象之后，首先调用实例方法
    def __init__(self):
        # 类属性
        self.names1 = ["Ava", "emma", "olivia"]
        self.names2 = ["olivia", "sophia", "emma"]

    def solution(self):
        for item in self.names2:
            if item not in self.names1:
                self.names1.append(item)
        print(self.names1)
        return self.names1


P1 = UniqueNames()
lis = P1.solution()
print(lis)