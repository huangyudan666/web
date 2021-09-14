from tools.http_request import HttpRequest
from tools.do_excel import DoExcel
from tools.project_path import *
import unittest
from ddt import ddt,data
from tools.get_data import GetData
from tools.logger import MyLog
from tools.do_mysql import DoMysql

test_data=DoExcel().do_excel(test_data_path)
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_http_request(self,item):
        MyLog().info("现在执行的用例是{0}".format(item['title']))
        #请求之前获取loan_id
        if item['data'].find('${loanId}')!=-1:
            if getattr(GetData,'loanId')==None:
                query_sql = 'select max(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
                loanId = DoMysql().do_mysql(query_sql)[0][0]
                MyLog().info("loan_id是{0}".format(loanId))
                item['data']=item['data'].replace('${loanId}',str(loanId))
                setattr(GetData,'loanId',str(loanId))
            else:
                item['data']=item['data'].replace('${loanId}',getattr(GetData,'loanId'))
        if item['check_sql']!=None:
            MyLog().info("此条用例需要做数据库校验{0}".format(item['title']))
            # 请求之前查询余额
            # 查询数据库
            query_sql =eval(item['check_sql'])['sql']
            Before_Amount = DoMysql().do_mysql(query_sql,1)[0]
            MyLog().info("充值之前的余额是{0}".format(Before_Amount))
            MyLog().info("---------------------开始发起请求-----------------------------")
            res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'], getattr(GetData, 'COOKIE'))
            MyLog().info("---------------------发起请求结束-----------------------------")
            # 请求之后校验余额是否正确
            query_sql = eval(item['check_sql'])['sql']
            After_Amount = DoMysql().do_mysql(query_sql,1)[0]
            MyLog().info("充值之后的余额是{0}".format(After_Amount))
            if int(abs(Before_Amount - After_Amount))== eval(item['data'])['amount']:
                check_res = '金额正确'
            else:
                check_res = '金额不对'
            DoExcel().write_back(test_data_path, item['sheet_name'], item['case_id'] + 1, 10, check_res)

        else:
            MyLog().info("此条用例不需要做数据库校验{0}".format(item['title']))
            MyLog().info("---------------------开始发起请求-----------------------------")
            res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'],getattr(GetData,'COOKIE'))
            MyLog().info("--------------------发起请求结束-----------------------------")


        if res.cookies:
            setattr(GetData,'COOKIE',res.cookies)
        try:
            self.assertEqual(str(item['excepted']),res.json()['code'])
            MyLog().info("第{0}条用例执行通过".format(item['case_id']))
            result='PASS'
        except AssertionError as e:
            result='FAIL'
            MyLog().error("第{0}条用例执行失败".format(item['case_id']))
            raise e
        finally:  # 不管错还是对 他里面的代码是一定会执行的
            DoExcel().write_back(test_data_path, item['sheet_name'], item['case_id'] + 1, 8, str(res.json()))
            DoExcel().write_back(test_data_path, item['sheet_name'], item['case_id'] + 1, 9, result)
            MyLog().error("获取到的结果是：{0}".format(res.json()))

    def tearDown(self):
        pass
