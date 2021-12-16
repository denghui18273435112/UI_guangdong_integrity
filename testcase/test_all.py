import pytest
from tools.Yaml_read import Yaml_read
from lib.all import *

class Test_all(object):
    """广东分类系统"""
    @pytest.mark.test
    @pytest.mark.run(order=1)
    def test_overview_digital(self,driver):
        """数字概览-统计数据自动核对"""
        assert_result = all(driver,Yaml_read("all.yaml","overview_digital")).overview_digital()
        assert True == assert_result

    @pytest.mark.run(order=2)
    def test_charts(self,driver):
        """数字概览-参训/达标走势图查询"""
        assert_result = all(driver,Yaml_read("all.yaml","charts")).charts()
        assert True ==assert_result

    @pytest.mark.run(order=3)
    def test_kinds_standards(self,driver):
        """数字概览-各类达标情况-数据核对"""
        assert_result = all(driver,Yaml_read("all.yaml","kinds_standards")).kinds_standards()
        assert True ==assert_result

    @pytest.mark.run(order=4)
    def test_student_details(self,driver):
        """学员详情-字段查询"""
        assert_result = all(driver,Yaml_read("all.yaml","student_details")).student_details()
        assert True ==assert_result

    @pytest.mark.run(order=5)
    def test_company_data(self,driver):
        """公司数据-查询导出"""
        assert_result = all(driver,Yaml_read("all.yaml","company_data")).company_data()
        assert True ==assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=6)
    def test_tabulate_data(self,driver):
        """汇总数据-查询"""
        assert_result = all(driver,Yaml_read("all.yaml","tabulate_data")).tabulate_data()
        assert True ==assert_result

    @pytest.mark.run(order=7)
    def test_submission(self,driver):
        """培训计划报送模块-查询、导出"""
        assert_result = all(driver,Yaml_read("all.yaml","submission_inquire")).submission_inquire()
        assert True ==assert_result

    @pytest.mark.run(order=8)
    def test_query_inquire(self,driver):
        """培训记录查询-查询、按钮操作"""
        assert_result = all(driver,Yaml_read("all.yaml","query_inquire")).query_inquire()
        assert True ==assert_result

    @pytest.mark.run(order=9)
    def test_inquire(self, driver):
        """培训学分查询模块-字段查询"""
        assert_result = all(driver,Yaml_read("all.yaml","inquire")).inquire()
        assert True == assert_result

    @pytest.mark.run(order=10)
    def test_operation(self, driver):
        """培训学分查询模块-操作(查询、重置、导出、分页跳转)"""
        assert_result = all(driver,Yaml_read("all.yaml","operation")).operation()
        assert True == assert_result

    @pytest.mark.run(order=11)
    def test_query_inquire(self,driver):
        """培训记录统计"""
        assert_result =all(driver,Yaml_read("all.yaml","record_statistical_query_inquire")).record_statistical_query_inquire()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=12)
    def test_account_management_inquire(self,driver):
        """账号管理-查询"""
        assert_result = all(driver, Yaml_read("all.yaml", "account_management_inquire")).account_management_inquire()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=13)
    def test_account_management_button_click(self,driver):
        """账号管理-按钮操作"""
        assert_result = all(driver, Yaml_read("all.yaml", "account_management_button_click")).account_management_button_click()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=14)
    def test_account_management_add(self,driver):
        """账号管理-账号添加"""
        assert_result = all(driver, Yaml_read("all.yaml", "test_account_management_add")).test_account_management_add()
        assert True == assert_result

    @pytest.mark.role_association
    @pytest.mark.run(order=15)
    def test_account_management_delete(self,driver):
        """账号管理-账号删除"""
        assert_result = all(driver, Yaml_read("all.yaml","test_account_management_delete")).test_account_management_delete()
        assert True == assert_result