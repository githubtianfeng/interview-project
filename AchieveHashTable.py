#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Tianfeng"
#题目1: 用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。

global HASHSIZE,NULLKEY
HASHSIZE = 12
NULLKEY = 0xffffffff/2

class HashTable(object):
    def __init__(self, size):
        self.array = []
        for i in range(0,size):
            self.array.append(NULLKEY)

    #哈希函数
    def Hash(self, key):
        return key % HASHSIZE; #除留取余法

    #插入关键字到哈希表
    def InsertHashTable(self, key):
        addr = self.Hash(key)
        while(self.array[addr] != NULLKEY):#不为空，则冲突了
            addr = (addr+1) % HASHSIZE; #开放定址法：线性探测
        self.array[addr] = key
    #在哈希表中查找关键字记录
    def SearchHashTable(self, key):
        addr = self.Hash(key)
        while(self.array[addr] != key):
            addr = (addr+1) % HASHSIZE #开放定址法：线性探测
            if(self.array[addr] == NULLKEY):
                return -1
        return addr
    #打印
    def show(self):
        print("hash table all element:")
        for i in self.array:
            print(i)
def main():
    hashtable = HashTable(HASHSIZE)
    list = [3, 1, 6, 3, 8, 9, 10, 23, 12, 11]
    for i in list:
        hashtable.InsertHashTable(i)
    hashtable.show()
    key = 11
    index = hashtable.SearchHashTable(key)
    print("find element:%d" %(index))

if __name__ == '__main__':
    main()