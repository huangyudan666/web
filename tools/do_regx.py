import re
from tools.get_data import GetData
class DoRegx:
    @staticmethod
    def do_regx(s):
        while re.search('\$\{(.*?)\}',s):
            key=re.search('\$\{(.*?)\}',s).group(0)
            value=re.search('\$\{(.*?)\}',s).group(1)
            s=s.replace(key,str(getattr(GetData,value)))
        return s

if __name__ == '__main__':
    s='{"memberId":"${memberID}","password":"123456","loanId":"${loanId}","amount":"-100"}'
    res=DoRegx.do_regx(s)
    print(res)