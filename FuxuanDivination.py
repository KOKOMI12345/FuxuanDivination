
from Fuxuan import Divination
from Fuxuan import Interpretation

# build exe file command:
# pyinstaller -F --version-file version.txt FuxuanDivination.py -i resources/icon.ico

if __name__ == '__main__':
    divination = Divination()
    interpretation = Interpretation()
    question = input("请输入你要占卜的问题：")
    hexagram , result = divination.run(question)
    interpretation.interpret(hexagram[0], hexagram[1], hexagram[2], result, out_to_file=True)