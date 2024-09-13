from ..utils import WUXING , HEXGRAM_TO_WUXING , DESC_HEXGRAM_TONUM , NUM_TO_HEXGRAM_STR

class Interpretation:
    """
    解卦类, 用于解释卦象
    """

    def __init__(self) -> None:
        pass

    def is_tian_hexagram(self, 
        original_hexagram: tuple[str, str, str],
        hexagram: tuple[str, str, str],
    ) -> str:
        """
        判断是否是体卦
        """
        return "体" if original_hexagram == hexagram else "用"


    def interpret(self, 
        original_hexagram: tuple[str, str, str, str, str, str],
        mutual_hexagram: tuple[str, str, str, str, str, str],
        changed_hexagram: tuple[str, str, str, str, str, str]
    ) -> str:
        """
        解释卦象
        """
        cache = []
        original_upper , original_lower = original_hexagram[:3], original_hexagram[3:]
        mutual_upper, mutual_lower = mutual_hexagram[:3], mutual_hexagram[3:]
        changed_upper, changed_lower = changed_hexagram[:3], changed_hexagram[3:]
        raise NotImplementedError("还没写完")
        
        