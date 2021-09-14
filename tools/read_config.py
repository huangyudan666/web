import configparser

class ReadConfig:
    def read_config(self,file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]

if __name__ == '__main__':
    from tools.project_path import *
    print(ReadConfig().read_config(case_config_path,'MODE','mode'))