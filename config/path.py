import os
current =os.path.abspath(__file__)                          #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径

#一级文件夹路径
config_path = BASE_DIR +os.sep+"config"
docs_path = BASE_DIR +os.sep+"docs"
file_path =BASE_DIR +os.sep+"file"
lib_path =BASE_DIR +os.sep+"lib"
logs_path = BASE_DIR +os.sep+"logs"
report_path =BASE_DIR +os.sep+"report"
testcase_path =BASE_DIR +os.sep+"testcase"
tools_data =BASE_DIR +os.sep+"tools"

#二级文件夹路径
result_path = report_path+os.sep+"result"
allure_report_path = report_path+os.sep+"allure_report"
guangdong_classify_path = testcase_path+os.sep+"guangdong_classify"
xampp_path = testcase_path+os.sep+"xampp"
photo_path = file_path+os.sep+"photo"
import_file_path = docs_path+os.sep + "import"

#文件路径
file_path_01= docs_path+os.sep+"广东诚信用例.xlsx"
file_path_02= import_file_path+os.sep+"01入职前诚信级别批量查询模板.xlsx"

