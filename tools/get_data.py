import pandas as pd
from tools.project_path import *

class GetData:
    COOKIE=None
    loanId=None
    tel= pd.read_excel(test_data_path,'init').iloc[0, 0]
    normal_tel= pd.read_excel(test_data_path, 'init').iloc[1, 0]
    admin_tel = pd.read_excel(test_data_path, 'init').iloc[2, 0]
    loan_member_id = pd.read_excel(test_data_path, 'init').iloc[3, 0]
    memberID=pd.read_excel(test_data_path,'init').iloc[4,0]
if __name__ == '__main__':
    print(GetData().loan_member_id)