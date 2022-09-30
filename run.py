'''
HTMLTestRunnerPlugins是一个第三方的工具，可以自动生成测试报告
放在python的lib下
'''

from HTMLTestRunnerPlugins import HTMLTestRunner
import unittest
import time

now_time = time.strftime('%Y-%m-%d %H_%M_%S')

dis = unittest.defaultTestLoader.discover('./case','*case.py')  # 实例化一个discover测试对象

runner = HTMLTestRunner(open(f'report/ecshop{now_time}.html','wb'),title='ecshop自动化测试报告',description='本轮测试的详细信息')  # 生成一个测试对象，里面需要传入要保存的测试报告的路径
                                                          # 文件名必须是html  打开方式是wb  也就是说覆盖写入二进制文件

runner.run(dis)
