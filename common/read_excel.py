'''
封装读取表格的公共方法
'''

import pandas


class ReadExcel:
    def __init__(self,file_path):
        if file_path.endswith('.csv'):
            self.file = pandas.read_csv(file_path)
        else:
            self.file = pandas.read_excel(file_path)

    def read_to_dict(self):
        lists = []
        for i in self.file.index.values:
            lists.append(self.file.loc[i].to_dict())
        return lists


if __name__ == '__main__':
    re = ReadExcel(r'F:\PyCode\T87\testdata.csv')
    print(re.read_to_dict())
    re = ReadExcel(r'F:\PyCode\T87\testdata.xls')
    print(re.read_to_dict())