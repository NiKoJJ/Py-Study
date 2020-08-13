# 天气建议
class WeatherSearch(object):
    def __init__(self, input_daytime):
        self.input_daytime = input_daytime

    def search_visibility(self):  # 能见度级别
        visible_leave = 0
        if self.input_daytime == 'daytime':
            visible_leave = 9
        if self.input_daytime == 'night':
            visible_leave = 3
        return visible_leave

    def search_temperature(self):  # 温度
        temper = 0
        if self.input_daytime == 'daytime':
            temper = 20
        if self.input_daytime == 'night':
            temper = 0
        return temper

    def search_wetness(self):  # 湿度
        wetness = 0
        if self.input_daytime == 'daytime':
            wetness = 50
        if self.input_daytime == 'night':
            wetness = 100
        return wetness


# 依据天气建议给出出行建议
class OutAdvice(WeatherSearch):  # 继承WS类，给出能见度、温度、湿度
    def __init__(self, input_time):
        WeatherSearch.__init__(self, input_time)

    def out_tool(self):  # 依据input_time 给出交通工具
        tool = 'none'
        if self.input_daytime == 'daytime':
            tool = 'bike'
        if self.input_daytime == 'night':
            tool = 'taxi'
        return tool

    def out_advice(self):  # 最终建议
        viki = self.search_visibility()
        wet = self.search_wetness()
        tep = self.search_temperature()
        tool = self.out_tool()
        if self.input_daytime == 'daytime':
            print(f'当前时间：{self.input_daytime}  \n    '
                  f'天气情况：能见度：{viki}  空气湿度：{wet}  温度：{tep} 适合使用的交通工具：{tool}')
        elif self.input_daytime == 'night':
            print(f'当前时间：{self.input_daytime}  \n    '
                  f'天气情况：能见度：{viki}  空气湿度：{wet}  温度：{tep} 适合使用的交通工具：{tool}')
        else:
            print('当前天气恶劣，不宜出行！')


# 白天出行建议
check1 = OutAdvice('daytime')
check1.out_advice()

# 晚上出行建议
check2 = OutAdvice('night')
check2.out_advice()

# 下雪天出行建议
check3 = OutAdvice('snow')
check3.out_advice()
