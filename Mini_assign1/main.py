from collections import Counter
class StringClass:
    def __init__(self, string):
        self.string = string
    def getstring(self):
        print(self.string)
    def stringlength(self):
        print(len(self.string))
    def tocharlist(self):
        str = []
        for x in self.string:
            str.append(x)
        print(str)


class pairpossible:
    def __init__(self, string):
        self.string = string

    def getpairs(self):
        pairs = [[x,y]for x in self.string for y in self.string]
        for i in pairs:
            print(f"({i[0]},{i[1]})", end=' ')
        print()

class commonelement:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    def common(self):
        dict1 = Counter(self.str1)
        dict2 = Counter(self.str2)
        commondict = dict1 & dict2
        commonchar = list(commondict.elements())
        print(commonchar)


print('Enter first string')
str1 = str(input())
obj = StringClass(str1)
obj.stringlength()
obj.tocharlist()
print('Enter second string')
str2 = str(input())
obj2 = pairpossible(str2)
obj2.getpairs()
obj3 = commonelement(str1,str2)
obj3.common()
