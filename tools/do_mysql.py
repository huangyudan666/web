import mysql.connector
from tools import project_path
from tools.read_config import ReadConfig

class DoMysql:
    def do_mysql(self,query_sql,state='all'):#query_sql--->查询语句  state---all 多条 1 一条
        db_config=eval(ReadConfig().read_config(project_path.case_conmysql.connectorfig_path,'DB','db_config'))
        #利用这个类从配置文件里面读取db info
        cnn=mysql.connector.connect(**db_config)
        #游标cursor
        cursor=cnn.cursor()
        #执行语句
        cursor.execute(query_sql)
        #获取结果 打印结果
        if state==1:
            res=cursor.fetchone()#元组  针对一条数据
        else:
            res=cursor.fetchall()#列表 针对多行数据 列表嵌套元组
        #关闭游标
        cursor.close()
        #关闭连接
        cnn.close()

        return res

if __name__ == '__main__':
     from tools.get_data import GetData
     query_sql='select max(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
     res=DoMysql().do_mysql(query_sql)
     print(res)
     print(res[0][0])
