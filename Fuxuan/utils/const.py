from datetime import datetime

NOW = datetime.now()
"""
NOW: 这个值是代表当前时间的datetime对象, 可以通过NOW.year, NOW.month, NOW.day等属性获取年月日等信息
"""

TIANGAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
DIZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

TIANGAN_NUM = {
    "甲": 1,
    "乙": 2,
    "丙": 3,
    "丁": 4,
    "戊": 5,
    "己": 6,
    "庚": 7,
    "辛": 8,
    "壬": 9,
    "癸": 10
}

# 定义地支数等,也可以表示时辰
ZHI_NUM = {
    "子": 1,
    "丑": 2,
    "寅": 3,
    "卯": 4,
    "辰": 5,
    "巳": 6,
    "午": 7,
    "未": 8,
    "申": 9,
    "酉": 10,
    "戌": 11,
    "亥": 12
}

# 获取时辰, 一天有 12个时辰, 确定 NOW.hour 在哪个范围中的时辰
ZHI_TO_TIME = {
    "子时": (23, 1, 1),
    "丑时": (1, 3, 2),
    "寅时": (3, 5, 3),
    "卯时": (5, 7, 4),
    "辰时": (7, 9, 5),
    "巳时": (9, 11, 6),
    "午时": (11, 13, 7),
    "未时": (13, 15, 8),
    "申时": (15, 17, 9),
    "酉时": (17, 19, 10),
    "戌时": (19, 21, 11),
    "亥时": (21, 23, 12)
}
TIME_TO_ZHI = { v:k for k,v in ZHI_TO_TIME.items() }

YIN = "— —" # 阴爻
YANG = "———" # 阳爻
# 定义先天卦数
HEXGRAM_NUM: dict[str, int] = {
    "乾": 1,
    "兑": 2,
    "离": 3,
    "震": 4,
    "巽": 5,
    "坎": 6,
    "艮": 7,
    "坤": 8 # 被整除的卦数
}
NUM_TO_HEXGRAM_STR = { v:k for k,v in HEXGRAM_NUM.items() }
# 卦象的表示方法(八卦表示法)
HEXGRAM_DESCRIPTION: dict[int, tuple[str, str, str]] = {
    1: (YANG, YANG, YANG),
    2: (YIN,YANG,YANG),
    3: (YANG,YIN,YANG),
    4: (YIN, YIN, YANG),
    5: (YANG,YANG,YIN),
    6: (YIN, YANG, YIN),
    7: (YANG, YIN, YIN),
    8: (YIN, YIN, YIN)
}

HEXAGRAM_DESCRIPTION_STR: dict[str, tuple[str, str, str]] = {
    "乾": (YANG, YANG, YANG),
    "兑": (YIN, YANG, YANG),
    "离": (YANG, YIN, YANG),
    "震": (YIN, YIN, YANG),
    "巽": (YANG, YANG, YIN),
    "坎": (YIN, YANG, YIN),
    "艮": (YANG, YIN, YIN),
    "坤": (YIN, YIN, YIN)
}

DESC_HEXGRAM_TONUM = { v:k for k,v in HEXGRAM_DESCRIPTION.items() }

# 定义五行
WUXING = {
    '木': {'生': '火', '克': '土'},
    '火': {'生': '土', '克': '金'},
    '土': {'生': '金', '克': '水'},
    '金': {'生': '水', '克': '木'},
    '水': {'生': '木', '克': '火'}
}

HEXGRAM_TO_WUXING = {
    "乾": "金",  # 乾为天，天的五行属性通常与金相关
    "兑": "金",  # 兑为泽，泽的五行属性也与金相关
    "离": "火",  # 离为火，火的五行属性与火相关
    "震": "木",  # 震为雷，雷的五行属性与木相关
    "巽": "木",  # 巽为风，风的五行属性与木相关
    "坎": "水",  # 坎为水，水的五行属性与水相关
    "艮": "土",  # 艮为山，山的五行属性与土相关
    "坤": "土"   # 坤为地，地的五行属性与土相关
}

RELATION_TO_LUCK = {
    ("体", "比合", "用"): "吉",
    ("体", "生", "用"): "小凶",
    ("用", "生", "体"): "大吉",
    ("体", "克", "用"): "小吉",
    ("用", "克", "体"): "大凶"
}

# 初始化关系字典
WUXING_RELATION: dict[tuple[str, str], tuple[str, str, str]] = {}

# 动态生成关系字典
def generate_wuxing_relation():
    for hex_ti, wuxing_ti in HEXGRAM_TO_WUXING.items():
        for hex_yong, wuxing_yong in HEXGRAM_TO_WUXING.items():
            if wuxing_ti == wuxing_yong:
                WUXING_RELATION[(hex_ti, hex_yong)] = ("体", "比合", "用")
            elif WUXING[wuxing_ti]['生'] == wuxing_yong:
                WUXING_RELATION[(hex_ti, hex_yong)] = ("体", "生", "用")
            elif WUXING[wuxing_yong]['生'] == wuxing_ti:
                WUXING_RELATION[(hex_ti, hex_yong)] = ("用", "生", "体")
            elif WUXING[wuxing_ti]['克'] == wuxing_yong:
                WUXING_RELATION[(hex_ti, hex_yong)] = ("体", "克", "用")
            elif WUXING[wuxing_yong]['克'] == wuxing_ti:
                WUXING_RELATION[(hex_ti, hex_yong)] = ("用", "克", "体")