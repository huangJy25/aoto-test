#写入
import os

import yaml

def write_yaml(data):
    with open(os.path.join(os.getcwd(), "extract.yaml"), "a+", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)
def read_yaml(key):
    with open(os.path.join(os.getcwd(), "extract.yaml"), "r", encoding="utf-8") as f:
        value = yaml.safe_load(f)  # 使用 safe_load 避免安全问题
        return value[key]


#清空:
def clear_yaml():
    with open(os.path.join(os.getcwd(), "extract.yaml"), "w", encoding="utf-8") as f:
        f.truncate()

#读取测试用例
def read_testcase(path):
    with open(path, "r", encoding="utf-8") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value




if __name__ == '__main__':
    print(read_testcase("test_case_1.yaml"))