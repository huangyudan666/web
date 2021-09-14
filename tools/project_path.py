import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
test_data_path=os.path.join(project_path,'test_data','test_data.xlsx')
case_config_path=os.path.join(project_path,'test_data','case.config')
test_report_path=os.path.join(project_path,'outputs','report','test_api.html')
log_path=os.path.join(project_path,'outputs','log','my_log.txt')
if __name__ == '__main__':
    print(project_path)