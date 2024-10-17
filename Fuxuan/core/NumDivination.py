
from ..utils import NUM_TO_HEXGRAM_STR , HEXAGRAM_DESCRIPTION_STR , YANG , YIN
from ..metadata import print_logo_and_some_infomation

class Num:
    """占卜数字类表示"""
    def __init__(self,
        first_num: int,
        second_num: int,
        third_num: int
    ) -> None:
        self.first_num = first_num
        self.second_num = second_num
        self.third_num = third_num

    def __str__(self) -> str:
        return f"first: {self.first_num}, second: {self.second_num}, third: {self.third_num}"
    
    def __repr__(self) -> str:
        return f"Num({self.first_num}, {self.second_num}, {self.third_num})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Num):
            return False
        return self.first_num == other.first_num and self.second_num == other.second_num and self.third_num == other.third_num
    
    def __hash__(self) -> int:
        return hash((self.first_num, self.second_num, self.third_num))
    
class NumDivination:
    """数字占卜类"""
    def __init__(self, num: Num, render_message: bool = True) -> None:
        self.num = num
        if render_message:
            print_logo_and_some_infomation()

    def get_upper_hexagram(self) -> tuple[str, str, str]:
        """获取上卦"""
        r_num = self.num.first_num % 8
        if r_num == 0:
            r_num = 8
        hexagram_str = NUM_TO_HEXGRAM_STR[r_num]
        hexagram = HEXAGRAM_DESCRIPTION_STR[hexagram_str]
        return hexagram
    
    def get_lower_hexagram(self) -> tuple[str, str, str]:
        """获取下卦"""
        r_num = self.num.second_num % 8
        if r_num == 0:
            r_num = 8
        hexagram_str = NUM_TO_HEXGRAM_STR[r_num]
        hexagram = HEXAGRAM_DESCRIPTION_STR[hexagram_str]
        return hexagram
    
    def change_yao(self, yao: str) -> str:
        """变爻"""
        if yao == YANG:
            return YIN
        else:
            return YANG
    
    def get_original_hexagram(self) -> tuple[tuple[str, str, str, str, str, str], int]:
        upper = self.get_upper_hexagram()
        lower = self.get_lower_hexagram()
        orig_hexagram = upper + lower
        changed = self.num.third_num % 6 # 爻以六除余
        return orig_hexagram , changed
    
    def get_mutual_hexagram(self) -> tuple[str, str, str, str, str, str]:
        """获取互卦"""
        orig_hexagram, _ = self.get_original_hexagram()
        mutual_upper = (orig_hexagram[3], orig_hexagram[2], orig_hexagram[1]) # 取本卦的 3, 4, 5 为上卦
        mutual_lower = (orig_hexagram[4], orig_hexagram[3], orig_hexagram[2]) # 取本卦的 2, 3, 4 为下卦
        mutual_hexagram = mutual_upper + mutual_lower
        return mutual_hexagram
    
    def get_changed_hexagram(self) -> tuple[str, str, str, str, str, str]:
        """获取变卦"""
        orig_hexagram, changed = self.get_original_hexagram()
        # 从下往上看, 先倒序排列
        hexagram = [hexagram for hexagram in reversed(orig_hexagram)]
        _changed = changed - 1 # 因为索引从0开始, 所以要减1
        hexagram[_changed] = self.change_yao(hexagram[_changed])
        changed_hexagram = tuple(reversed(hexagram)) # 再反转回来，并转为元组
        return changed_hexagram # type: ignore
    
    def build_hexagram(self) -> tuple[tuple[str, str, str, str, str, str], tuple[str, str, str, str, str, str], tuple[str, str, str, str, str, str]]:
        """构建卦象"""
        orig_hexagram, _ = self.get_original_hexagram()
        mutual_hexagram = self.get_mutual_hexagram()
        changed_hexagram = self.get_changed_hexagram()
        return (orig_hexagram, mutual_hexagram, changed_hexagram)
        
    
    def run(self, question: str) -> tuple[tuple[tuple[str, str, str, str, str, str], tuple[str, str, str, str, str, str], tuple[str, str, str, str, str, str]], str]:
        """运行占卜"""
        result = ""
        hexagram = self.build_hexagram()
        result +="对于你的问题,卦象情况如下:\n"
        result += f"本卦: \n{hexagram[0]}\n"
        result += f"互卦: \n{hexagram[1]}\n"
        result += f"变卦: \n{hexagram[2]}\n"
        return hexagram , result