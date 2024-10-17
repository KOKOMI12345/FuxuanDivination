from datetime import datetime
from .const import TIANGAN , DIZHI
from lunarcalendar import Converter, Solar, Lunar

class EightChar:
    """
    生辰八字表示类
    """
    def __init__(self,
        year: str,
        month: str,
        day: str,
        hour: str
    ) -> None:
        self.year = year
        self.month = month
        self.day = day  
        self.hour = hour

    def time_show(self) -> str:
        """
        输出生辰八字
        """
        return f"{self.year}年-{self.month}月-{self.day}日-{self.hour}时"
    
    def get_year(self) -> str:
        """
        获取年干支
        """
        return self.year
    
    def get_month(self) -> str:
        """
        获取月干支
        """
        return self.month
    
    def get_day(self) -> str:
        """
        获取日干支
        """
        return self.day
    
    def get_hour(self) -> str:
        """
        获取时干支
        """
        return self.hour

    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day}-{self.hour}"
    
class CalculateEightChar:
    """
    计算生辰八字类
    """

    @staticmethod
    def get_year(year: int) -> tuple[str, str]:
        """获取年干支"""
        gan_index = (year - 4) % 10  # 甲子年为基准
        zhi_index = (year - 4) % 12
        return TIANGAN[gan_index], DIZHI[zhi_index]

    @staticmethod
    def get_month(year: int, month: int) -> tuple[str, str]:
        """获取月干支"""
        month_zhi = DIZHI[month % 12]  # 根据月份计算地支
        year_tian_index = (year - 4) % 10  # 年干基准
        if month == 1 or month == 2:  # 如果是正月或二月，年份天干需要减一
            month_tian_index = (year_tian_index + 9) % 10  # 得到前一年最后一个天干
        else:
            month_tian_index = (year_tian_index * 12 + month) % 10  # 基于年干计算月份天干
        return TIANGAN[month_tian_index], month_zhi

    @staticmethod
    def get_day(date: datetime) -> tuple[str, str]:
        """获取日干支"""
        base_date = datetime(1900, 1, 31)  # 甲辰日
        days_diff = (date - base_date).days
        day_index = (days_diff + 40) % 60  # 甲日偏移40天
        return TIANGAN[day_index % 10], DIZHI[day_index % 12]

    @staticmethod
    def get_hour(day_gan: str, hour: int) -> tuple[str, str]:
        """获取时干支"""
        hour_zhi_index = (hour + 1) // 2 % 12  # 小时地支
        hour_zhi = DIZHI[hour_zhi_index]

        # 确定时干的偏移
        hour_gan_index = (TIANGAN.index(day_gan) * 2 + hour_zhi_index) % 10
        hour_gan = TIANGAN[hour_gan_index]

        return hour_gan, hour_zhi

    @staticmethod
    def get_eight_char(date: datetime) -> EightChar:
        """计算生辰八字"""
        year_gan, year_zhi = CalculateEightChar.get_year(date.year)
        month_gan, month_zhi = CalculateEightChar.get_month(date.year, date.month)
        day_gan, day_zhi = CalculateEightChar.get_day(date)
        hour_gan, hour_zhi = CalculateEightChar.get_hour(day_gan, date.hour)

        year = f"{year_gan}{year_zhi}"
        month = f"{month_gan}{month_zhi}"
        day = f"{day_gan}{day_zhi}"
        hour = f"{hour_gan}{hour_zhi}"

        return EightChar(year, month, day, hour)

# 示例使用
if __name__ == '__main__':
    date = datetime(2024, 10, 17, 22)
    bazi = CalculateEightChar.get_eight_char(date)
    print(f"生辰八字：{bazi}")