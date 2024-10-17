from datetime import datetime
import sys

# 《五不占》
ILTGEAR = """ 不义不占\n 心不诚不占 \n 目的不明不占 \n 心不静不占 \n 同卦不复占"""
# Program information
PROGRAM_NAME = "《梅花易经占卜》"
USING_SOURCE = "https://www.bilibili.com/video/BV1Fx4y1a78m/"
AUTHOR = "符玄(KOKOMI12345)"
GITHUB = "https://github.com/KOKOMI12345/FuxuanDivination"
VERSION = "0.2.1"
PYTHON_V = f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
UPDATE = "2024-10-17 19:30:00"
NOW = datetime.now()
INFOMATION_STRING = f"@Name: {PROGRAM_NAME}\n@Author: {AUTHOR}\n@Github: {GITHUB}\n@Version: {VERSION}\n@Python: {PYTHON_V}\n@Updated: {UPDATE}\n@Time: {NOW.strftime('%Y-%m-%d %H:%M:%S')}\n@Source: {USING_SOURCE}\n"
# Program information
DIVINATION_LOGO = r"""
    _______   __  ____    ____  __  .__   __.      ___   .___________. __    ______   .__   __. 
   |       \ |  | \   \  /   / |  | |  \ |  |     /   \  |           ||  |  /  __  \  |  \ |  |
   |  .--.  ||  |  \   \/   /  |  | |   \|  |    /  ^  \ `---|  |----`|  | |  |  |  | |   \|  |
   |  |  |  ||  |   \      /   |  | |  . `  |   /  /_\  \    |  |     |  | |  |  |  | |  . `  |
   |  '--'  ||  |    \    /    |  | |  |\   |  /  _____  \   |  |     |  | |  `--'  | |  |\   |
   |_______/ |__|     \__/     |__| |__| \__| /__/     \__\  |__|     |__|  \______/  |__| \__|

"""
def print_logo_and_some_infomation():
    print(f"\033[35m{DIVINATION_LOGO}\033[0m")
    print(f"\033[35m{INFOMATION_STRING}\033[0m \n")
    print(f"\033[32m{ILTGEAR}\033[0m \n")