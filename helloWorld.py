print("hello world")

print(1,2,3,4) #分隔符默认为空格 输出1 2 3 4

print(1,2,3,4,sep="->") #sep="",中间填值代替分隔符

print(1,2,3,4,end="\n")

f=open("nihao","a")
print("hello world",file=f)
f.close()#文件写入写法，普通类,没有文件也会自动创建文件

with open("nihao","a")as f:
    print("hello",file=f)#文件写入写法，with类，没有文件自动创建文件，会自动关闭文件

f=open("nihao","a")
print("www",file=f)
f.close()

with open("nihao","a")as f:
    print("aaa",file=f)

f=open("nihao","a")
print("bbb",file=f)
f.close()

with open("nihao","a")as f:
    print("ccc",file=f)

with open("nihaoma","a")as f:
    print("ddd",file=f)

with open("nihaoma","w")as f:
    print("eee",file=f)#"w"参数为覆盖文件内容



