import time
from tools.Allure import alluer
from tools.logUtil import my_log
from tools.selenium import selenium
from config.fixed_options import *

class all:
    def __init__(self,driver,Data):
        self.new_driver = driver
        self.driver = selenium(driver)
        self.data = Data["data"]
        self.Data = Data
        self.driver.url_skip(self.Data["URL"])
        my_log().debug("["+self.Data["test_id"]+"--"+self.Data["module"]+"--"+self.Data["name"]+"]")

    def record_statistical_query_inquire(self):
        """培训记录统计模块-查询-操作"""
        try:
            print("培训记录统计模块-查询-操作 中.....")
            self.driver.zzl_company_inquire("中国人民财产保险股份有限公司广东省分公司")
            self.driver.zzl_pull_down_inquire(2,"2020")
            self.driver.zzl_pull_down_inquire(4,"线下")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_pull_down_inquire(4,"线上")
            self.driver.zzl_pull_down_inquire(5,"本机构")
            #self.driver.zzl_pull_down_inquire(7,"已达标")
            #self.driver.resfresh()
            self.driver.zzl_click("查询",type="xpath_starts-with")
            self.driver.zzl_click("重置",type="xpath_starts-with")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_text_input("//*/span[starts-with(.,\"前往\")]//input",10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        print("培训记录统计模块-查询-操作 已结束")
        return self.Data["actual_result"]

    def account_management_inquire(self):
        """
        账号管理-查询核对数据
        :return:
        """
        try:
            #操作
            self.driver.zzl_pull_down_inquire(2,type[0])
            self.driver.zzl_pull_down_inquire(3,status[0])
            self.driver.zzl_pull_down_inquire(4,login_status[1])
            gongsi = self.driver.text_acquire(column=8)
            self.driver.zzl_company_inquire(gongsi)
            name = self.driver.text_acquire(column=2)
            self.driver.zzl_text_input("input[placeholder=\"请输入昵称\"]",name,type="css")
            judge_data = [name,login_status[1],status[0]]
            list_position = [2,6,9]
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.list_judgment(judge_data=judge_data,list_position=list_position)
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def account_management_button_click(self):
        """
        点击操作
        :return:
        """
        try:
            self.driver.zzl_click("查询",type="xpath_starts-with")
            self.driver.zzl_click("重置",type="xpath_starts-with")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_text_input("//*/span[starts-with(.,\"前往\")]//input",10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def test_account_management_add(self):
        """
        添加账号
        :return:
        """
        try:
            self.driver.zzl_click("div.table-area div.export>span:nth-child(3)",type="css")
            self.driver.zzl_text_input("请输入用户名","denghui00001",type="css_text")
            self.driver.zzl_text_input("请输入用户昵称","denghui00001",type="css_text")
            self.driver.zzl_text_input("请输入手机号","18273435112",type="css_text")
            self.driver.zzl_text_input("请输入新密码","denghui921206",type="css_text")
            self.driver.zzl_text_input("再次输入密码","denghui921206",type="css_text")
            self.driver.zzl_company_inquire_s("大昌深业保险代理有限公司湛江分公司",
                                              location='div.content > div > form > div > div.el-col.el-col-24 > div > div > div > div > input',type="css")
            self.driver.zzl_click("确定",type="xpath_starts-with")

            if self.driver.text_acquire(column=2) !="denghui00001":
                self.Data["actual_result"] = False
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def test_account_management_delete(self):
        """
        删除账号
        :return:
        """
        try:
            # for x in range(15):
            #     ceshi1 = False
            #     for y in range(10):
            #         if self.driver.text_acquire(row=x+1,column=y+1)=="denghui00001":
            #             shuliang = x+1
            #             location = "div.el-table__body-wrapper tbody>tr:nth-child({0})>td:nth-child(11) svg:nth-child(2)".format(shuliang)
            #             time.sleep(10)
            #             self.driver.zzl_click(location=location,type="css")
            #             ceshi1 = True
            #     if ceshi1:
            #
            self.driver.zzl_click(location="div.el-table__body-wrapper tbody>tr:nth-child(1)>td:nth-child(11)>div>span>svg:nth-child(2)",type="css")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def inquire(self):
        """培训学分查询模块-字段查询"""
        try:
            print("培训学分查询模块-字段查询 中....")
            self.driver.FEBCS_CCSKK("input[placeholder=\"请选择所属机构\"]",self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(1) span"))
            self.driver.zzl_click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li:nth-child(1)","css")
            for index in range(len(check_range)):
                self.driver.pull_down_choose("div div:nth-child(2)>div.el-select>div>span",
                                             "//ul/li/*[contains(text(),\"{}\")]".format(check_range[index]),type="CSS_XPATH")
            for index in range(len(year)):
                self.driver.pull_down_choose("div div:nth-child(3)>div.el-select>div>span",
                                             "//ul/li/*[contains(text(),\"{}\")]".format(year[index]),type="CSS_XPATH")
            # for index in range(len(course_name)):
            #     self.driver.pull_down_choose("div div:nth-child(4) > div.el-select > div > span",
            #                                  "//ul/li/*[contains(text(),\"{}\")]".format(course_name[index]),type="CSS_XPATH")
            for index in range(len(reach_status)):
                self.driver.drop_down_box("div div:nth-child(5) > div.el-select > div > span ",
                                          "//li/span[contains(text(),\"{}\")]".format(reach_status[index]))
            for index in range(len(certificate_type)):
                self.driver.drop_down_box("div div:nth-child(7) > div.el-select > div > span",
                                          "//li/span[contains(text(),\"{}\")]".format(certificate_type[index]))
            for index in range(len(training_method)):
                self.driver.pull_down_choose("div div:nth-child(9) > div.el-select > div > span",
                                          "//li/span[contains(text(),\"{}\")]".format(training_method[index]),type="CSS_XPATH")
            # for index in range(len(units)):
            #     self.driver.pull_down_choose("div div:nth-child(10)>div.el-select>div>span",
            #                               "body>div>div>div.el-select-dropdown__wrap.el-scrollbar__wrap>ul>li:nth-child({})".format(index+1))
            self.driver.click("重置",type="starts-with")
            self.new_driver.implicitly_wait(50)
            self.driver.FEBCS_CCSKK("div:nth-child(6) > div.el-input > input[placeholder=\"请输入\"]",
                                    self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(2) span"),ifhuiche=True)
            self.driver.FEBCS_CCSKK("div:nth-child(8) > div.el-input > input[placeholder=\"请输入\"]",
                                    self.driver.text_acquire("div:nth-child(3) div.el-table__body-wrapper  tr:nth-child(1)>td:nth-child(4) span"),ifhuiche=True)

        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        print("培训学分查询模块-字段查询 已结束")
        return self.Data["actual_result"]

    def operation(self):
        """培训学分查询模块-操作(查询、重置、导出、分页跳转)"""
        try:
            print("培训学分查询模块-操作(查询、重置、导出、分页跳转) 中.....")
            self.driver.click("查询",type="starts-with")
            time.sleep(10)
            self.driver.click("重置",type="starts-with")
            time.sleep(10)
            self.driver.click("导出",type="starts-with")
            time.sleep(10)
            #self.driver.input_text("//*/span[starts-with(.,\"前往\")]//input",10,type="xpath",Enter=0)
            self.driver.text_input("//*/span[starts-with(.,\"前往\")]//input",10)
            time.sleep(10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        print("培训学分查询模块-操作(查询、重置、导出、分页跳转) 已结束")
        return self.Data["actual_result"]

    def overview_digital(self):
        """"数字概览-统计数据自动核对"""
        try:
            print("首页-数字概览;数据核对 中.....")
            #self.driver.click("//span[contains(text(),'数字概览')]")
            CXJHZRS=self.driver.text_acquire("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
            ZYCXRS = int(CXJHZRS.split("/")[0])
            ZJHRS = int(CXJHZRS.split("/")[1])
            CL=int(self.driver.text_acquire("span:nth-child(2) > span.value"))
            ZL=int(self.driver.text_acquire("span:nth-child(3) > span.value"))
            YCX=int(self.driver.text_acquire("span:nth-child(4) > span.value"))
            WCX=int(self.driver.text_acquire("span:nth-child(5) > span.value"))
            ZDBZCX = self.driver.text_acquire("div:nth-child(2) > div > div.container  span:nth-child(1) > span.total")
            ZDB = int(ZDBZCX.split("/")[0])
            ZCX = int(ZDBZCX.split("/")[1])
            YDB=int(self.driver.text_acquire("div:nth-child(2)  div.container  span:nth-child(2) > span.value"))
            WDB=int(self.driver.text_acquire("div:nth-child(2)  div.container  span:nth-child(3) > span.value"))
            if ZJHRS==(CL+ZL) and ZYCXRS==YCX and WCX==(ZJHRS-ZYCXRS) and ZDB==YDB and ZCX==(YDB+WDB) and WDB==(ZCX-YDB):
                self.Data["actual_result"] = True
            else:
                self.Data["actual_result"] = self.Data["assert_fail_hint"]
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        print("首页-数字概览;数据核对 已结束。")
        return self.Data["actual_result"]

    def charts(self):
        """数字概览-参训/达标走势图查询"""
        try:
            print("首页-数字概览;走势查询 中.....")
            self.driver.click("//span[contains(text(),'数字概览')]")
            self.driver.click("div  div.top > div:nth-child(2) > div span")
            self.driver.click("//li/span[contains(text(),\"线上\")]")
            self.driver.click("#app > div > div.container.main-right.scroll-bar > div.wrapper")
            self.driver.click("#app > div > div.container.main-right.scroll-bar")
            self.driver.click("div.wrapper > div.line div.right-wrapper > div > span.chart.active")
            self.driver.click("div.condition.conditions > div.right-wrapper > div > span.tables")
            self.driver.click("div.right-wrapper > div:nth-child(1) > span")
            self.driver.click("div.right-wrapper > div:nth-child(2) > span.chart")
            self.driver.click("div.left-wrapper > div:nth-child(1) div > span > span > i")
            self.driver.click("//li/span[contains(text(),\"达标走势\")]")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        print("首页-数字概览;走势查询 已结束。")
        return self.Data["actual_result"]

    def kinds_standards(self):
        """数字概览-各类达标情况-数据核对"""
        try:
            print("数字概览-各类达标情况-数据核对 中.....")
            self.driver.click("//span[contains(text(),'数字概览')]")
            CXJHZRS=self.driver.text_acquire("div:nth-child(1) > div > div.container  span:nth-child(1) > span.total")
            ZYCXRS = int(CXJHZRS.split("/")[0])
            self.driver.Page_scrolling()
            sum_new = 0
            dingwei = self.driver.text_acquire("div.pies > div:nth-child(2)  div:nth-child(1) > div > span:nth-child(1)")
            sum_new += int(dingwei.split(":")[1])
            if  sum_new>=ZYCXRS:
                self.Data["actual_result"] = self.Data["assert_fail_hint"]
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
        self.driver.screenShots()
        alluer(self.Data)
        print("数字概览-各类达标情况-数据核对 已结束。")
        return self.Data["actual_result"]

    def student_details(self):
        """学员详情-字段查询"""
        try:
            print("学员详情-字段查询 中.....")
            self.driver.click("//span[contains(text(),'学员详情')]")
            gongsi = self.driver.text_acquire("div.el-table__body-wrapper.is-scrolling-left  tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div > span")
            name = self.driver.text_acquire("div.el-table__body-wrapper.is-scrolling-left  tr:nth-child(1) > td.el-table_1_column_2.is-center > div > span")
            self.driver.FEBCS_CCSKK("div.condition-wrapper  div:nth-child(1) > div.el-input.el-input--suffix > input",name,ifhuiche=True)
            gongsi_new  =self.driver.text_acquire("div.el-table__body-wrapper.is-scrolling-left  tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div > span")
            if  gongsi != gongsi_new:
                self.Data["actual_result"] = self.Data["assert_fail_hint"]
            self.driver.FEBCS_CCSKK("div.condition-wrapper  div:nth-child(1) > div.el-input.el-input--suffix > input",gongsi,ifhuiche=True)
            self.driver.FEBCS_CCSKK("div.condition-wrapper  div:nth-child(1) > div.el-input.el-input--suffix > input"," ",ifhuiche=True)
            for x in range(0,6):
                kecheng = ["B类：新型寿险产品销售培训","D类：新型寿险和车险销售培训","C类：车险产品销售培训","车险业务知识","新型寿险业务知识","A类：基础保险销售业务知识培训"]
                self.driver.drop_down_box("div.condition-wrapper  div:nth-child(2) > div.el-select > div > span","//li/span[contains(text(),\"{}\")]".format(kecheng[x]))
            for xx in range(0,2):
                dabiao =["未达标","已达标"]
                self.driver.drop_down_box("div:nth-child(3) > div.el-select > div.el-input.el-input--suffix > span > span > i","//li/span[contains(text(),\"{}\")]".format(dabiao[xx]))
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        print("学员详情-字段查询 已结束。")
        return self.Data["actual_result"]

    def company_data(self):
        """公司数据-查询导出"""
        try:
             self.driver.zzl_click("//span[contains(text(),'公司数据')]")
             self.driver.zzl_click("div.top20.table-area > div.tabs > span.tables > svg","css")
             self.driver.zzl_click("div.top20.table-area > div.tabs > span.chart >svg","css")
             self.driver.FEBCS_CCSKK("div.condition > div > div > div:nth-child(1) > div > input",
                                     self.driver.text_acquire(" table > tbody > tr:nth-child(1) > td.el-table_1_column_1.is-center > div"),ifhuiche=True)
             self.driver.zzl_click("div.condition > div > div > div:nth-child(2) > span","css")
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        return self.Data["actual_result"]

    def tabulate_data(self):
        """汇总数据-查询"""
        try:
            print("汇总数据-查询 中.....")
            self.driver.click("//span[contains(text(),'汇总数据')]")
            CXRS = self.driver.text_acquire("tbody  tr td:nth-child(2) div")
            if int(CXRS)!=0:
                self.Data["actual_result"] =="有数据没问题"
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        print("汇总数据-查询 已结束。")
        return self.Data["actual_result"]

    def query_inquire(self):
        """培训记录查询-查询、按钮操作"""
        try:
            print("培训记录查询-查询、按钮操作 中......")
            self.driver.zzl_company_inquire(self.driver.text_acquire(column=1))
            self.driver.zzl_pull_down_inquire(2,"仅限本机构")
            self.driver.zzl_pull_down_inquire(2,"本机构及下级")
            self.driver.zzl_pull_down_inquire(4,"A类：基础保险销售业务知识培训")
            self.driver.zzl_pull_down_inquire(3,"2020")
            self.driver.zzl_pull_down_inquire(3,"2021")
            self.driver.zzl_pull_down_inquire(7,"身份证")
            self.driver.zzl_pull_down_inquire(9,"线上")
            self.driver.zzl_pull_down_inquire(10,"其他第三方")
            self.driver.zzl_click("重置",type="xpath_starts-with")
            self.driver.zzl_text_input("div:nth-child(6) > div.el-input > input[placeholder=\"请输入\"]",
                                       self.driver.text_acquire(column=2),type="css")
            self.driver.zzl_text_input("div:nth-child(8) > div.el-input > input[placeholder=\"请输入\"]",
                                       self.driver.text_acquire(column=4),type="css")
            self.driver.zzl_click("查询",type="xpath_starts-with")
            self.driver.zzl_click("重置",type="xpath_starts-with")
            self.driver.zzl_click("导出",type="xpath_starts-with")
            self.driver.zzl_text_input("//*/span[starts-with(.,\"前往\")]//input",10)
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]
        self.driver.screenShots()
        alluer(self.Data)
        print("培训记录查询-查询、按钮操作 已结束。")
        return self.Data["actual_result"]

    def submission_inquire(self):
        """培训计划报送模块-查询、导出"""
        try:
            print("培训计划报送模块-查询、导出 中....")
            self.driver.click("div:nth-child(6) > span.zzl-button")
            #self.driver.FEBCS_CCSKK("input[placeholder=\"请选择所属机构\"]","中国人寿保险股份有限公司广东省分公司")
            #self.driver.click("div.el-cascader__suggestion-panel.el-scrollbar > div.el-scrollbar__wrap > ul > li")
            self.driver.click("div:nth-child(5) > span.zzl-button")
            # self.driver.resfresh()
            for x in [1,3]:
                self.driver.pull_down_choose("div div:nth-child(2) > div.el-select > div > span","body>div.el-select-dropdown div>ul>li:nth-child({})".format(x))
        #截图/校验部分/用于判断用例是否通过/定位不到抛异常
        except BaseException as error:
            self.Data["actual_result"] = self.Data["location_fail_hint"]+error
            my_log().debug(self.Data["actual_result"])
        self.driver.screenShots()
        alluer(self.Data)
        print("培训计划报送模块-查询、导出 已结束。")
        return self.Data["actual_result"]