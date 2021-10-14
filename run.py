import unittest
from Config.HTMLTestRunner import HTMLTestRunner
import os
import time

# 用例路径
case_path = os.path.join(os.getcwd(), "TestCase")

# 报告存放路径
report_path = os.path.join(os.getcwd(), "Reports")

"""
unittest 提供了可以共享的 defaultTestLoader类，可以使用其子类或方法
创建实例，discover()方法就是其中之一。
"""
# 加载用例
discover = unittest.defaultTestLoader.discover(case_path,
                                               pattern="test*.py",
                                               top_level_dir=None)

if __name__ == "__main__":
    # 获取当前时间
    times = time.strftime("%Y-%m-%d %H_%M_%S")

    # html报告文件地址
    report_abspath = os.path.join(report_path, times + "-result.html")

    # 打开文件，并赋予可写权限
    fp = open(report_abspath, "wb")

    # 把测试结果写进测试报告，并装载到HTHMLTestRunner模块
    runner = HTMLTestRunner(stream=fp,
                            title="测试报告YYDS",
                            description="用例执行情况",
                            verbosity=2)
    # 运行测试用例
    runner.run(discover)
    # 关闭文件
    fp.close()



