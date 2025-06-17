import os
import time
import logging
import pytest

def setup_logger():
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler("test_log.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.info("Starting pytest execution...")

    # 显式传递参数（覆盖 pytest.ini 的 addopts）
    args = [
        "-vs",
        "--alluredir=./temps",
        "--clean-alluredir",
        # 其他参数...
    ]
    pytest.main(args)

    logger.info("Pytest execution finished.")
    time.sleep(3)

    # 生成 Allure 报告（确保 allure 已安装）
    logger.info("Generating Allure report...")
    os.system("allure generate ./temps -o ./reports --clean")
    logger.info("Allure report generated.")