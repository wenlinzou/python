#coding=utf8
num = 49
tens = num // 10
ones = num % 10
print tens, ones
print 10 * tens + ones


hour = 20
shift = 8
print (hour + shift) % 24

width = 800
position = 797
move = 5
position = (position + move) % width
print position

hour = 3
ones = hour % 10
tens = hour // 10
print tens, ones, ":00"
print str(tens), str(ones), ":00"
print str(tens) + str(ones) + ":00"


# import simplegui
import math
import random

print math.pi