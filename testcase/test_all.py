import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *
from tools.ExcelData import *

class Test_all(object):
    """广东诚信系统"""

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("Data",ExcelData("test_OD_inquire"))
    def test_OD_inquire(self,driver,Data):
        """个人信息查询-单个查询"""
        assert_result = all(driver,Data).OD_inquire()
        assert "通过" == assert_result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("Data",ExcelData("test_Batch_query_Reset"))
    def test_Batch_query_Reset(self,driver,Data):
        """个人信息查询-批量查询、重置"""
        assert_result = all(driver,Data).Batch_query_Reset()
        assert "通过" == assert_result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("Data",ExcelData("test_import_query_"))
    def test_import_query(self,driver,Data):
        """导入批量查询"""
        assert_result = all(driver,Data).import_query()
        assert "通过" == assert_result

    #@pytest.mark.test
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("Data",ExcelData("test_Default_condition_query"))
    def test_Default_condition_query(self,driver,Data):
        """所有模块默认条件查询"""
        assert_result = all(driver,Data).Default_condition_query()
        assert "通过" == assert_result