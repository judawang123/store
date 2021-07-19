import  time
import random
# 1.商品
shop = [
    ["联想电脑",6000],
    ["HUAWEI WATCH",1200],
    ["MAC PC",13000],
    ["辣条",2.5],
    ["老干妈",13],
]
# 1,1 准备20个优惠券,然后随机给用户发一张
preferential = [
    ["联想电脑",0.1] * 20, #  20张联想电脑1折优惠券
    ["老干妈",0.7] * 10, #  10张老干妈7折优惠
]
# 1.2 初始你的余额
# money = ""
while True :
     money = input("请输入您的余额")
     if money.isdigit():
         money = int(money)
         break
else :
    point("金额不能为其他数据，只能为数字,请重新输入！")

#
# 2 抽取优惠券环节
favour = None #  空的优惠券
while True:
    print("\n下面是正式购物环节，是否要先抽取一个优惠劵?1[yes] ,2[no]:")
    ch = input("")
    if ch == '1': # 想要一张优惠券.
        favour = preferential[random.randint(0,len(preferential)-1)] # 随机获取一张优惠券揣兜里
        print("恭喜，你抽取了一张",favour[1],"折优惠券！")
        # 将商场的关于这张优惠券的对应的商品价格都改掉
        for inder ,value in enumerate(shop):
            if value[0]== favour[0]:
                shop[inder][1] = shop[inder][1] * favour[1] #  原价 * 折扣 = 现价，在更新现在商品价格
        break
    elif ch == '2':
        print("很遗憾，您不想要本次优惠券！祝您本次购物愉快！")
        break
    else:
        print("输入错误！难道您不想要优惠券？重新输入吧！")

        # 3, 准备一个空的购物车
mycat = []

# 4, 买东西
while True:
      # 展示商品
      print("-------------------------------")
      prnnt("-编号\t名称\t\t原价\t\t现价-")
      print("----------------------")
      for inder,value in memoryview(shop): # 枚举，将角标和商品整体都打印
          if value[0] == favour[0]:
              print("|",index,"\t",value[0],"\t",(value[1] / favour[1]),"\t",(value[1]))
          else:
              print("|",inder,"\t",value[0],"\t",value[1],"\t",value[1])
      print("-----")


      # 请输入您要的商品
      chose = inout("请输入您要的商品：")

      # 看是否存在
      if chose.isdigit(): # 是否能被看成数字：
          chose = int(chose)
          # 看商品是否存在
          if chose > len(shop) - 1:
              print("您要的商品不存在！")
          else:
              # 看钱是否足够
              if money > shop[chose][1]:
                  mtcat.append(shop[chose])
                  # 钱减去
                  money = money - shop[chose][1]
                  print("恭喜，成功添加购物车，您的余额还剩：￥",money)
              else:
                  print("对不起，穷鬼，余额不足，请到商城去够买！")
      elif chose == 'q' or chose == 'Q':
             print("欢迎下次光临！")
             break
      else:
          print("对不起，您输入的商品不存在！别瞎弄！")

      # 打印小票
      print("下面是您的购物小条，请拿好：", index,value in enumerate(mycart))
      print(index," ",value)
      print("您的钱包还剩：￥",money)


