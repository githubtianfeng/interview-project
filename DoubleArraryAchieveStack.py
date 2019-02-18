#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Tianfeng"
#题目1: 用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。
#使用python自带的array库

class Stack(object):
    def __init__(self):
        self.array = [[], []]

#栈1
    def l_push(self, data):
        self.array[0].append(data)

    def l_pop(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            return self.array[0].pop()
#栈2
    def r_push(self, data):
        self.array[1].append(data)

    def r_pop(self):
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            return self.array[1].pop()
#显示
    def show(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            print('Stack a:', self.array[0])
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            print('Stack b:', self.array[1])

def main():
    stack = Stack()
    for i in range(1,11):
        stack.l_push(i)
        stack.r_push(i)
    stack.show()

    print("stack1 pop element:%d" % (stack.l_pop()))
    print("stack2 pop element:%d" % (stack.r_pop()))

    stack.show()
if __name__ == '__main__':
    main()