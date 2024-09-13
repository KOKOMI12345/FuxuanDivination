
from ..metadata import print_logo_and_some_infomation
from ..utils import NOW, ZHI_TO_TIME, ZHI_NUM, HEXGRAM_DESCRIPTION, YANG, YIN , get_gan_zhi_from_year

try:
    from ..requires import LunarDate
    import sys
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r', 'requirements.txt'])
    from ..requires import LunarDate

class Divination:
    """
    易经占卜程序主要实现类,用于占卜问题的吉凶、卦象、变卦等信息。
    本人符玄厨QwQ~
    """

    def __init__(self):
        print_logo_and_some_infomation()

    def get_lunar_day_and_month(self) -> tuple[int, int]:
        """
        获取当前农历日期
        """
        ld = LunarDate.today()
        return ld.month, ld.day

    def get_year_zhi(self) -> str:
        """
        根据公历年份获取对应的地支
        """
        zhi = [
            "子", "丑", "寅", "卯", "辰", "巳",
            "午", "未", "申", "酉", "戌", "亥"
        ]
        # 1984年是甲子年，用当前年份减去1984，然后取余数确定地支
        year = NOW.year
        index = (year - 1984) % 12
        return zhi[index]
    
    def get_current_zhi_and_num(self) -> tuple[str, int]:
        current_hour = NOW.hour
        for zhi, (start, end, day_zhi_num) in ZHI_TO_TIME.items():
            if start <= current_hour < end:
                return zhi , day_zhi_num
            # 处理子时（23:00 - 01:00）和跨越日期分界的情况
            if zhi == "子时" and (current_hour >= 23 or current_hour < 1):
                return zhi , day_zhi_num
        return "未知时辰"
    
    def get_current_zhi_and_num_by_lunar(self) -> tuple[str, int]:
        """
        获取当前农历日期的地支
        """
        year_zhi = self.get_year_zhi()
        # 农历日期转阳历日期
        return year_zhi, ZHI_NUM[year_zhi]
    

    def get_upper_hexgram(self) -> tuple[str, str, str]:
        """
        获取上卦
        """
        year_zhi = self.get_year_zhi()
        zhi_num = ZHI_NUM[year_zhi]
        upper_hexgram = HEXGRAM_DESCRIPTION[zhi_num]
        return upper_hexgram

    def get_lower_hexagram(self) -> tuple[str, str, str]:
        """
        获取下卦
        方法是 (年 + 农月 + 农日 + 时辰) % 8 ... 取余数确定卦象
        """
        _ , year_num = self.get_current_zhi_and_num_by_lunar()
        ld_date = self.get_lunar_day_and_month()
        now_zhi = self.get_current_zhi_and_num()
        # 获取余数
        remainder = (year_num + ld_date[0] + ld_date[1] + now_zhi[1]) % 8
        if remainder == 0: # 坤卦
            return HEXGRAM_DESCRIPTION[8]
        else:
           return HEXGRAM_DESCRIPTION[remainder]
    
    def get_changed_yao(self, yao: str) -> str:
        """
        根据当前爻的状态，返回反转后的爻
        """
        if yao == YANG:
            return YIN
        elif yao == YIN:
            return YANG
        return yao  # 如果传入的 yao 不是 YANG 或 YIN，就返回原样

    def get_changed_hexagram(self, hexagram: tuple[str, str, str, str, str, str]) -> tuple[str, str, str, str, str, str]:
        """
        根据当前的卦象，返回变卦后的卦象
        算法步骤:
        (年 + 农月 + 农日 + 时) / 6 = result ... 余数确定变卦象(爻以六除)
        """
        year_zhi, year_num = self.get_current_zhi_and_num_by_lunar()
        ld_date = self.get_lunar_day_and_month()
        now_zhi = self.get_current_zhi_and_num()
        # 获取余数
        remainder = (year_num + ld_date[0] + ld_date[1] + now_zhi[1]) % 6
        changed_hexagram = list(hexagram)  # 将元组转换为列表以便修改

        # 根据余数确定变卦的爻，从下往上数
        if remainder != 0:
            # remainder 应该不能为6, 因为python的索引从 0 开始, 为 6就会 IndexError
            changed_hexagram[remainder - 1] = self.get_changed_yao(changed_hexagram[remainder - 1])
        else:
            changed_hexagram[5] = self.get_changed_yao(changed_hexagram[5])

        return tuple(changed_hexagram)  # 将列表转换回元组
        

    def build_hexagram(self) -> tuple:
        """
        构建卦象，包括本卦、互卦和变卦
        """
        # 本卦
        upper_hexagram = self.get_upper_hexgram()
        lower_hexagram = self.get_lower_hexagram()
        original_hexagram = upper_hexagram + lower_hexagram

        # 互卦 (取本卦的 345 做上卦, 234 做下卦)
        mutual_upper = (original_hexagram[3], original_hexagram[2], original_hexagram[1])
        mutual_lower = (original_hexagram[4], original_hexagram[3], original_hexagram[2])
        mutual_hexagram = mutual_upper + mutual_lower

        # 变卦
        changed_hexagram = self.get_changed_hexagram(original_hexagram)

        # 接下来用字符串表示卦象
        original_hexagram_str = "\n".join(original_hexagram)
        mutual_hexagram_str = "\n".join(mutual_hexagram)
        changed_hexagram_str = "\n".join(changed_hexagram)

        return original_hexagram_str, mutual_hexagram_str, changed_hexagram_str
    
    def run(self, question: str) -> None:
        """
        主程序入口
        """
        print(f"您的问题：{question}")
        hexagram = self.build_hexagram()
        year_gan , year_zhi = get_gan_zhi_from_year(NOW.year)
        print(f"占卜时间: {NOW.strftime('%Y-%m-%d %H:%M:%S')}({year_gan}{year_zhi}年)({self.get_current_zhi_and_num()[0]})")
        print("对于你的问题,卦象情况如下:\n")
        print(f"本卦: \n{hexagram[0]}")
        print(f"互卦: \n{hexagram[1]}")
        print(f"变卦: \n{hexagram[2]}")

if __name__ == '__main__':
    pass