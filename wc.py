def WCgetchar(file_name):
    f = open(file_name, "r")
    return len(f.read())
def WCgetline(file_name):
    f = open(file_name, "r")
    read = f.readlines()#以行为单位读取文本并存入列表
    return len(read)
import re
def WCgetword(file_name):
    f = open(file_name, "r")
    read = re.split(r'[^a-zA-Z]+', f.read())
    return len(read)

def main():
    str , name = input("输入命令符和文件路径（以空格分开）：\n").split()
    if str == '-c':
        print('字符数:', WCgetchar(name))
    elif str == '-w':
        print('单词数：', getword(name))
    elif str == '-l':
        print('行数：', WCgetline(name))


main()