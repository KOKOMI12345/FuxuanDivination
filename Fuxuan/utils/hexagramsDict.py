
from .const import YIN ,YANG

NAME_TO_HEXAGRAMS_64 = {
    "乾为天": (YANG, YANG, YANG, YANG, YANG, YANG),
    "坤为地": (YIN, YIN, YIN, YIN, YIN, YIN),
    "水雷屯": (YIN, YANG, YANG, YANG, YIN, YIN),
    "山水蒙": (YIN, YIN, YANG, YANG, YIN, YIN),
    "水天需": (YIN, YIN, YIN, YANG, YANG, YANG),
    "天水讼": (YANG, YIN, YIN, YIN, YANG, YANG),
    "地水师": (YIN, YIN, YIN, YIN, YANG, YANG),
    "水地比": (YIN, YIN, YIN, YANG, YIN, YIN),
    "风天小畜": (YIN, YIN, YANG, YANG, YANG, YANG),
    "天泽履": (YANG, YANG, YIN, YIN, YIN, YIN),
    "天地否": (YANG, YANG, YANG, YIN, YIN, YIN),
    "地天泰": (YIN, YIN, YIN, YANG, YANG, YANG),
    "火水未济": (YANG, YIN, YANG, YIN, YANG, YIN),
    "火风鼎": (YANG, YIN, YANG, YANG, YIN, YIN),
}

HEXAGRAMS_64_TO_NAME = {hexagrams : name for name, hexagrams in NAME_TO_HEXAGRAMS_64.items()}