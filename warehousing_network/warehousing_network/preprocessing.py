# 数据读取及预处理

import os


class PreProcessor:

    def __init__(self, parsed_input):
        self.path = parsed_input['path']
        self.data = self.read_data_from_excel()

    def read_data_from_excel(self):
        data = []  # 待完成
        return data

    def preprocess_demand_info(self):
        pass

    def preprocess_candidate_locations(self):
        pass

    def preprocess_distance_matrix(self):  # 初步计算, 根据经纬度直线距离，若该距离大于阈值, 则不需要调百度api
        pass

    def calculate_distance(self):  # 调用百度api计算两点实际距离
        pass


if __name__ == 'main':
    cwd = os.getcwd()
    parsed_input = {
        'path': cwd,
    }
    pass
