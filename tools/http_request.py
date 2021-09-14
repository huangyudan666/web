import requests

class HttpRequest:
    def http_request(self,url,data,http_method,cookie=None):
        try:
           if http_method.upper()=='GET':
               res=requests.get(url,data,cookies=cookie)
           elif http_method.upper()=='POST':
               res=requests.post(url,data,cookies=cookie)
           else:
               print("输入的请求方式有误")
           return res
        except Exception as e:
            print("错误是{0}".format(e))
            raise e

if __name__ == '__main__':
    register_url='http://test.lemonban.com/futureloan/mvc/api/member/register'
    register_data={"mobilephone":"13392193984","pwd":"123456"}
    register_res=HttpRequest().http_request( register_url, register_data,'get')
    print(register_res.json())

    login_url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    login_data={"mobilephone":"13392193984","pwd":"123456"}
    login_res=HttpRequest().http_request(login_url,login_data,'post')
    print(login_res.json())

    recharge_url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    recharge_data={"mobilephone":"13392193984","amount":"1000"}
    recharge_res=HttpRequest().http_request(recharge_url,recharge_data,'post',login_res.cookies)
    print(recharge_res.json())
    