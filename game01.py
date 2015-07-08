__author__ = 'Pet'
print("----------wenlinzouGAME--------")
# for i in range(10):
#     print(i)
#     i = 5
temp = input("猜猜我心里的数字")
guess = int(temp)

# while(guess==8){
if guess == 8:
    print("你太有才了")
    print("猜对了")
else:
    print("猜的不对")
    print("游戏结束")
# }