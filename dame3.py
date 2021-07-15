import random
# 1.让系统产生一个随机数

money = 2000
count = 0
data = random.randint(0, 10)  # 22
# 2,x循环的让客户去猜
i = 1
while True:
  if money < 200:
   break
  else:
      i <= 10
      count = count + 1
      money = money - 200
      num = input ("请输入您要输入的数字：")
      num = int(num)  # "22"  -->  22


      if  num > data:
          print("大了", "剩余金币：",money)
      elif num < data:
          print ("小了","剩余金币：",money)
      else :
          money = money + 5000
          print("恭喜，猜中了!,本次幸运数字为，data，奖励5000金币",money)
          san = input("是否继续游戏  1.是  2.否")
          san = int(san)
          if san == 1:
           data = random.randint(0, 10)
          else:
           break








