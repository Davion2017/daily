import aiml
import jieba

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


while True:
    question = " ".join(jieba.cut(input("小爱同学为你服务>>>")))
    # print("问题拆分为" + question)
    print("".join(kernel.respond(question)))