from ..utils import WUXING , HEXGRAM_TO_WUXING , DESC_HEXGRAM_TONUM , NUM_TO_HEXGRAM_STR , HEXAGRAMS_64_TO_NAME , WUXING_RELATION , RELATION_TO_LUCK
from typing import Union, Optional

class Interpretation:
    """
    解卦类, 用于解释卦象
    """

    def __init__(self) -> None:
        pass

    def is_ti_or_yong_hexagram(self,
        original_hexagram: tuple[str, str, str, str, str, str],
        changed_hexagram: tuple[str, str, str, str, str, str]
    ) -> dict[str, tuple[str, str, str]]:
        """
        根据本卦和变卦判断体用关系
        判断方法:
        如果卦象中有变爻,那么为用,否则为体
        """
        ti_or_yong = {}
            # 判断哪个爻变了
        for i in range(6):
            if original_hexagram[i] != changed_hexagram[i]:
                # 如果找到了变爻，则开始拆分
                if i <= 3:
                    # 取上卦
                    ti_or_yong['体'] = original_hexagram[:3] # 体
                    ti_or_yong['用'] = changed_hexagram[3:] # 用
                else:
                    # 取下卦
                    ti_or_yong["体"] = original_hexagram[3:] # 体
                    ti_or_yong["用"] = changed_hexagram[:3] # 用
                break
        return ti_or_yong
    
    def get_name_of_hexagram(self, hexagram: tuple[str, str, str]) -> str:
        """
        获取卦象的名称
        """
        try:
            hexagram_num = DESC_HEXGRAM_TONUM[hexagram]
            hexagram_name = NUM_TO_HEXGRAM_STR[hexagram_num]
            return hexagram_name
        except KeyError:
            return "未知八卦中的卦象"
        
    def get_wuxing_info(self, hexagram: tuple[str, str, str],return_wuxing: bool = False) -> Union[dict[str, str], str]:
        """
        获取卦象的五行属性信息 (也是卦象相生相克的信息)
        如果 return_key 为 True, 则返回五行属性
        """
        try:
            hexagram_name = self.get_name_of_hexagram(hexagram)
            wuxing = HEXGRAM_TO_WUXING[hexagram_name]
            hexagram_wuxing_info = WUXING[wuxing]
            # 如果 return_key 为 True, 则返回五行属性的键值
            if return_wuxing:
                return wuxing
            else:
                return hexagram_wuxing_info
        except KeyError:
            return "未知五行属性或卦象"
    
    # 定义判断相生相克的函数
    def validate_defnense_wuxing_element(self, hexagram_ti: tuple[str, str, str], hexagram_yong: tuple[str, str, str]) -> tuple[str, str, str]:
        """
        判断两个卦象是否相生相克
        返回 (体/用, 生/克 , 体/用)
        """
        default = ("体", "未知", "用")
        default_reverse = ("用", "未知", "体")
        hexagram_ti_name = self.get_name_of_hexagram(hexagram_ti)
        hexagram_yong_name = self.get_name_of_hexagram(hexagram_yong)

        relation = WUXING_RELATION.get((hexagram_ti_name, hexagram_yong_name), default)
        if relation == default:
            # 未找到对应关系, 尝试反向查找
            relation = WUXING_RELATION.get((hexagram_yong_name, hexagram_ti_name), default_reverse)
        return relation
        
    def interpret_luck_for_hexagram(self, hexagram_ti: tuple[str, str, str], hexagram_yong: tuple[str, str, str]) -> str:
        """
        解释卦象的吉凶
        """
        try:
            relation = self.validate_defnense_wuxing_element(hexagram_ti, hexagram_yong)
            luck = RELATION_TO_LUCK[relation]
            return luck
        except KeyError:
            return "未知吉凶"
    
    def get_64_hexagram(self, hexagram: tuple[str, str, str, str, str, str]) -> str:
        """
        获取卦象的类型
        """
        try:
            return HEXAGRAMS_64_TO_NAME[hexagram]
        except KeyError:
            return "卦象还未被收录"

    def interpret(self, 
        original_hexagram: tuple[str, str, str, str, str, str],
        mutual_hexagram: tuple[str, str, str, str, str, str],
        changed_hexagram: tuple[str, str, str, str, str, str],
        result_string: str,
        output_to_console: bool = True, # 是否输出到控制台
        out_to_file: bool = False, # 是否输出到文件
        file_path: str = "interpretation.txt" # 文件路径
    ) -> Optional[str]:
        """
        解释卦象(解释卦象的主函数)
        """
        answer = "卦象解释如下：\n" # 解释卦象的结果
        answer += result_string
        original_hexagram_name = self.get_64_hexagram(original_hexagram)
        mutual_hexagram_name = self.get_64_hexagram(mutual_hexagram)
        changed_hexagram_name = self.get_64_hexagram(changed_hexagram)
        orig_upper , orig_lower = original_hexagram[:3] , original_hexagram[3:]
        mut_upper , mut_lower = mutual_hexagram[:3] , mutual_hexagram[3:]
        chg_upper , chg_lower = changed_hexagram[:3] , changed_hexagram[3:]
        answer += f"本卦: {self.get_name_of_hexagram(orig_upper)}上{self.get_name_of_hexagram(orig_lower)}下\n"
        answer += f"互卦: {self.get_name_of_hexagram(mut_upper)}上{self.get_name_of_hexagram(mut_lower)}下\n"
        answer += f"变卦: {self.get_name_of_hexagram(chg_upper)}上{self.get_name_of_hexagram(chg_lower)}下\n"
        answer += f"本卦为: {original_hexagram_name}\n"
        answer += f"互卦为: {mutual_hexagram_name}\n"
        answer += f"变卦为: {changed_hexagram_name}\n"
        hexagram_ti = self.is_ti_or_yong_hexagram(original_hexagram, changed_hexagram)['体']
        hexagram_yong = self.is_ti_or_yong_hexagram(original_hexagram, changed_hexagram)['用']
        orig_result = self.interpret_luck_for_hexagram(hexagram_ti, hexagram_yong)
        answer += f"本卦为: {orig_result}卦\n"
        chg_ti = self.is_ti_or_yong_hexagram(changed_hexagram, original_hexagram)['体']
        chg_yong = self.is_ti_or_yong_hexagram(changed_hexagram, original_hexagram)['用']
        chg_result = self.interpret_luck_for_hexagram(chg_ti, chg_yong)
        answer += f"变卦为: {chg_result}卦\n"
        if orig_result == chg_result:
            answer += f"所以,这件事或运气从开始到结束都是: {orig_result} 的\n"
        else:
           answer += f"所以,这件事从开始到结束的变化为: {orig_result} -> {chg_result}\n"
        if output_to_console:
            print(answer)
        if out_to_file:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(answer)
        return answer