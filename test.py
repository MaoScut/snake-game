import random

# 测试重新设置食物位置的函数
# class Rect:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# def resetFood(arr):
#     flag = True
#     while flag:
#         rand = [random.randrange(0, 30),
#                 random.randrange(0, 30)]
#         repeated = False
#         for rect in arr:
#             if (rect.x == rand[0] and rect.y == rand[1]):
#                 repeated = True
#                 break
#         if (repeated):
#             continue
#         flag = False
#     return rand

# testCount = 2000
# errorCount = 0
# myArr = [Rect(2,4), Rect(7,15), Rect(5,26), Rect(11, 29), Rect(21, 2), Rect(18, 11)]
# while testCount > 0:
#     r = resetFood(myArr)
#     for rect in myArr:
#         if (rect.x == r[0] and rect.y == r[1]):
#             print('false')
#             errorCount += 1
#     testCount -= 1
# print('错误次数' + str(errorCount))
