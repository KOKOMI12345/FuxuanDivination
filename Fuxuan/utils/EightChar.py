# 获取生辰八字
from datetime import datetime
from .const import TIANGAN, DIZHI
from ..exceptions import ArgumentRequired

"""
作者提醒： 这个八字计算可能会不准确，因为要考虑立春
"""

def get_gan_zhi_from_year(year: int) -> tuple[str, str]:
    """
    根据年份获取天干地支
    :param year: 年份
    :return: 天干和地支的元组
    :rtype: tuple
    """
    if year is None:
        raise ArgumentRequired("年份不能为空")
    # 1984年是甲子年，用当前年份减去1984，然后取余数确定天干和地支
    gan_index = (year - 1984) % 10
    zhi_index = (year - 1984) % 12
    tiangan_year = TIANGAN[gan_index]
    dizhi_year = DIZHI[zhi_index]
    return (tiangan_year, dizhi_year)

def get_gan_zhi_from_month(year: int, month: int) -> tuple[str, str]:
    """
    根据年份和月份获取月干地支
    :param year: 年份
    :param month: 月份
    :return: 月干和地支的元组
    :rtype: tuple
    """
    if year is None or month is None:
        raise ArgumentRequired("年份和月份不能为空")
    # 每个月的地支是固定的，从寅月开始
    month_zhi = DIZHI[month % 12]

    # 每个月的天干需要根据当年的天干来确定
    year_gan, _ = get_gan_zhi_from_year(year)
    month_gan = TIANGAN[(year_gan.index(year_gan[0]) + month) % 10]

    return (month_gan, month_zhi)

def get_gan_zhi_from_day(year: int, month: int, day: int) -> tuple[str, str]:
    """
    根据日获取日干地支
    :param year: 年份
    :param month: 月份
    :param day: 日
    :return: 日干和日支的元组
    :rtype: tuple
    """
    if year is None or month is None or day is None:
        raise ArgumentRequired("年份、月份和日不能为空")
    # 1900年1月31日是甲辰日
    start_date = datetime(1900, 1, 31)
    start_day = (start_date - datetime(1900, 1, 1)).days
    target_date = datetime(year, month, day)
    target_day = (target_date - datetime(year, 1, 1)).days
    
    # 计算从1900年1月31日到目标日期的天数差
    delta_days = (target_day - start_day) % 60
    
    # 计算日干和日支
    gan_index = (delta_days * 2 + 5) % 10  # 甲为0，所以加5
    zhi_index = (delta_days + 4) % 12  # 辰为3，所以加4
    
    tiangan_day = TIANGAN[gan_index]
    dizhi_day = DIZHI[zhi_index]
    
    return (tiangan_day, dizhi_day)

def get_gan_zhi_from_hour(day_gan: str, hour: int) -> tuple[str, str]:
    """
    根据日干和小时获取时干地支
    :param day_gan: 日干
    :param hour: 小时（0-23）
    :return: 时干和时支的元组
    :rtype: tuple
    """
    if day_gan is None or hour is None:
        raise ArgumentRequired("小时不能为空")
    # 根据小时计算时辰的地支
    hour_zhi_index = (hour + 1) // 2 % 12
    dizhi_hour = DIZHI[hour_zhi_index]
    
    # 根据日干和时辰的地支计算时辰的天干
    hour_gan_index = (TIANGAN.index(day_gan) * 2 + (hour_zhi_index % 10)) % 10
    tiangan_hour = TIANGAN[hour_gan_index]
    
    return (tiangan_hour, dizhi_hour)

def get_eight_char_time(time: datetime) -> str:
    """
    获取生辰八字时间
    :param time: 日期时间
    :return: 生辰八字时间
    :rtype: str
    """
    year_gan, year_zhi = get_gan_zhi_from_year(time.year)
    month_gan, month_zhi = get_gan_zhi_from_month(time.year, time.month)
    day_gan, day_zhi = get_gan_zhi_from_day(time.year, time.month, time.day)
    hour_gan, hour_zhi = get_gan_zhi_from_hour(day_gan, time.hour)

    # 将天干地支组合成生辰八字时间
    eight_char_time = f"{year_gan}{year_zhi}年,{month_gan}{month_zhi}月,{day_gan}{day_zhi}日,{hour_gan}{hour_zhi}时"
    return eight_char_time

def get_eight_char(time: datetime) -> str:
    """
    获取生辰八字
    :param time: 日期时间
    :return: 生辰八字
    :rtype: str
    """
    year_gan, year_zhi = get_gan_zhi_from_year(time.year)
    month_gan, month_zhi = get_gan_zhi_from_month(time.year, time.month)
    day_gan, day_zhi = get_gan_zhi_from_day(time.year, time.month, time.day)
    hour_gan, hour_zhi = get_gan_zhi_from_hour(day_gan, time.hour)

    # 将天干地支组合成生辰八字
    eight_char = f"{year_gan}{year_zhi}{month_gan}{month_zhi}{day_gan}{day_zhi}{hour_gan}{hour_zhi}"
    return eight_char

if __name__ == '__main__':
    # 测试
    eight_char = get_eight_char(datetime(2022, 1, 1, 12))
    print(eight_char)  # 庚申年戊辰月丙寅日戊申时辰