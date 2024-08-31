import hardware_setup  # Create a display instance
from gui.core.ugui import Screen, ssd

from gui.widgets import Label, Button, CloseButton
from gui.core.writer import CWriter

# Font for CWriter
import gui.fonts.arial10 as arial10
from gui.core.colors import *

import gc
import urequests
from machine import RTC


class ClockScreen(Screen):
    def __init__(self, wri: CWriter):
        super().__init__()
        row = 2
        col = 2
        label = Label(wri, row, col, "Time")

        row = row + label.height + 4
        current_time = self.get_beijing_time()
        current_time.append(0)  # 微秒
        rtc = RTC()
        rtc.datetime(current_time)  # 时间（年，月，日，星期，时，分，秒，微秒），其中星期使用0-6表示星期一至星期日。
        time_label = Label(wri, row, col, "%s/%s/%s-%s %s:%s:%s" % rtc.datetime()[0:7])

        gc.collect()
        CloseButton(wri)

    @staticmethod
    def get_beijing_time():
        try:
            # 设置头信息，没有访问会错误400！！！
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'
            }
            # 设置访问地址，我们分析到的；
            url = r'https://www.beijing-time.org/t/time.asp'
            # 用requests get这个地址，带头信息的；
            r = urequests.get(url=url, headers=headers)
            # 检查返回的通讯代码，200是正确返回；
            if r.status_code == 200:
                # 定义result变量存放返回的信息源码；
                result = r.text
                # 通过;分割文本；
                data = result.split(";")
                # ======================================================

                # 以下是数据文本处理：切割、取长度，最最基础的东西就不描述了；
                year = data[1][len("nyear") + 3: len(data[1])]
                month = data[2][len("nmonth") + 3: len(data[2])]
                day = data[3][len("nday") + 3: len(data[3])]
                wday = data[4][len("nwday") + 3: len(data[4])]
                hrs = data[5][len("nhrs") + 3: len(data[5])]
                minute = data[6][len("nmin") + 3: len(data[6])]
                sec = data[7][len("nsec") + 3: len(data[7])]
                # ======================================================
                # 这个也简单把切割好的变量拼到beijinTimeStr变量里；
                # beijingTimeStr = "%s/%s/%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
                # 把时间打印出来看看；
                # print(beijingTimeStr)
                # 将beijingTimeStr转为时间戳格式；
                # beijingTime = time.mktime(time.strptime(beijingTimeStr, "%Y/%m/%d %X"))
                # 返回时间戳；
                return [int(year), int(month), int(day), int(wday), int(hrs), int(minute), int(sec)]
        except Exception as e:
            return str('get_beijing_time() Exception Error! Info: ', e)
