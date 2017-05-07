# -*- coding: utf-8 -*-
"""
Created on Sun May 07 14:24:56 2017

@author: zack zhang
"""

x = [1,2,3,4,5,6]
print x[::2]#第一个：代表start，第二个：代表end，2代表step
print x[1::2]#1代表start的index，两个：代表到end，2代表step


前段时间Jeff Atwood 推广了一个简单的编程练习叫FizzBuzz，问题引用如下：
写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。
这里就是一个简短的，有意思的方法解决这个问题：

for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x #当x可以被3整除时，"fizz"[x%3*4::]变成"fizz"[0::]="fizz"
