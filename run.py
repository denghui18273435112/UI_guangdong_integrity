import pytest
from config.path import *
if __name__ == "__main__":
    pytest.main(["-s", "./testcase/test_all.py",
                  "-m", "not(role_association)",
                  "-m", "test",
                  "--alluredir", result_path])
    os.system("allure generate {0} -o {1} --clean".format(result_path, allure_report_path))
    os.system("allure serve {}".format(result_path))
