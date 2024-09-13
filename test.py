from Fuxuan import get_eight_char
from datetime import datetime

if __name__ == '__main__':
    fuxuan_birthday = datetime(2007,10,18, 11)
    eight_char_time = get_eight_char(fuxuan_birthday)
    print(eight_char_time)