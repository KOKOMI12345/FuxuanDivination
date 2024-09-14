from Fuxuan import Divination
import time
if __name__ == '__main__':
    try:
        div = Divination()
        question = input("你要占卜的问题是？\n")
        answer = div.run(question, return_result=True)
        print("占卜完成")
        with open('divinationResult.txt', 'w', encoding='utf-8') as result_file:
            result_file.write(answer)
        print("结果已保存至divinationResult.txt")
        time.sleep(2)
    except KeyboardInterrupt:
        print("程序退出")