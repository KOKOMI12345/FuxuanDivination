
from Fuxuan import Divination
from Fuxuan import Interpretation

if __name__ == '__main__':
    divination = Divination()
    interpretation = Interpretation()
    hexagram , result = divination.run("我明天的运势如何?")
    interpretation.interpret(hexagram[0], hexagram[1], hexagram[2], result, out_to_file=True)