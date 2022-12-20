﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define e = Character("桃濑日和")
define config.gl2 = True

image hiyori = Live2D("Resources/hiyori", base=.6, loop = True, seamless=True)

init python:
    import socket
    import time
    ip_port = ('127.0.0.1', 9000)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(ip_port)


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    #scene bg library

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。
    show hiyori m01

    #show eileen happy

    # 此处显示各行对话。


    python:
        token = renpy.input("让我们开始吧，请输入ChatGPT的Token")
        client.send(token.encode())
    
    e "Token已经收到，我们进入下一步吧"
    menu modelChoice:
        e "我们来选择一个角色作为语音输出"

        "綾地寧々":
            #block of code to run
            python:
                client.send(("0").encode())
            jump talk
        "在原七海":
            #block of code to run
            python:
                client.send(("1").encode())
            jump talk
        "小茸":
            #block of code to run
            python:
                client.send(("2").encode())
            jump talk
        "唐乐吟":
            #block of code to run
            python:
                client.send(("3").encode())
            jump talk
    
    # 此处为游戏结尾。

    return
    
label talk:
    show hiyori m02
    python:
        message = renpy.input("你：")
        client.send(message.encode())
        data = bytes()
    jump checkRes

label checkRes:
    
    show hiyori m03
    e "..."

    python:
        client.setblocking(0)
        try:
                data = client.recv(1024)
        except:
                data = bytes()
                client.setblocking(1)
    
    if(len(data) > 0):
        $ response = data.decode()
        jump answer
    else:
        e "......"
        jump checkRes

        

label answer:
    show hiyori talking
    #$ duration = renpy.music.get_duration(channel='sound')
    #play sound "/audio/test.mp3"
    #$ renpy.pause(delay=(duration + 1), hard=True)
    
    $ lines = ["/audio/test.mp3"]
    while lines: # 只要lines列表不为空，表达式结果等效于True
        play sound lines.pop(0) # 移除lines列表第一个元素
        e "[response]"
        pause    
    #e "[response]"

    jump talk
    