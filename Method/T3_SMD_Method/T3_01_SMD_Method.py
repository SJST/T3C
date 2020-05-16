
from T3C_Config_Method import Config
import os
import re
from T3_M_Method import Method
from T3_SMD_Method.T3_02_ShuX_model import Model
import xlrd


class SmdMethod:
    pass


'''
这个是对SMD进行操作的一些方法；
1st 首先根据配置的 SMD Path 获取到所有 SMD 文件夹；
2st 通过获取到文件夹+父级目录获取到 SMD 文件夹下的所有文件；
3st 通过正则匹配 T3开头 xlsx 结尾的文件 即 SMD 文件；
4st 通过 获取到的文件+ 父级目录 拼接 SMD 文件地址；
5st 通过 xlrd 将文件解析；
6st 筛选需要的字段,改名；
7st 加入标记字段,
8st 通过民事案件smd 生成属性配置模板;
9st 根据模板 给 字段加入对应属性；
10st 连接数据库；

'''


def get_smd_root(key):
    """
    1st 首先根据配置的 SMD Path 获取到所有 SMD 文件夹；
    :param key: 配置的键值
    :return: 配置的value值
    """

    smd_dir_path = Config.smd_config(key)
    return smd_dir_path


def get_smd_dir(smd_dir_path):
    data = (os.walk(smd_dir_path))
    smd_dir_list = []
    for root, dirs, files in data:
        for i in dirs:
            if i == 'SMD':
                smd_dir_one = root+"\\SMD"
                smd_dir_list.append(smd_dir_one)
    return smd_dir_list


def get_smd_file(smd_dir_list):
    """
    2st 通过获取到文件夹+父级目录获取到 SMD 文件夹下的所有文件；
    3st 通过正则匹配 T3开头 xlsx 结尾的文件 即 SMD 文件；
    4st 通过 获取到的文件+ 父级目录 拼接 SMD 文件地址；
    :param smd_dir_list: smd 目录文件
    :return: smd file 列表
    """
    smd_file_list = []
    for i in smd_dir_list:
        data = (os.walk(i))
        for root, dirs, files in data:
            for j in files:
                if re.search('^T3.*xlsx$', j):
                    smd_flies_one = root+"\\"+j
                    smd_file_list.append(smd_flies_one)
    return smd_file_list


def get_all_smd_content(smd_file_list):
    """
    获取所有的smd的原始内容,根据配置字段增加需要的内容
    :param smd_file_list: 上一个方法获取的包含所有的要获取的smd 的path+filename 的地址；
    :return all_smd_data_list 返回全部的数据，这个数据是一个大列表中包含小列表，小列表中包含许多个小字典 格式为 [[{},{}]]
    """
    all_smd_data_list = []
    for one_smd_file in smd_file_list:
        file_name = Method.spilt_content(one_smd_file, "\\", -1)
        patten_rule = r'[\u4e00-\u9fa5]+'
        smd_flags = Method.re_patten(patten_rule, file_name)
        if smd_flags == "":
            smd_flags = "openapi"
        print(file_name)
        try:
            one_smd_content = Method.get_one_smd_data(one_smd_file, "COL", 0, 1)
            element_conf_list = Config.smd_config("need_field_list")
            changed_smd_data = Method.get_need_element(element_conf_list, one_smd_content, smd_flags)
            all_smd_data_list.append(changed_smd_data)
        except Exception as e:
            print(file_name+"出现异常")
    return all_smd_data_list


def need_data_list(all_data):
    """
    获取需要的字段的数据列表
    :param all_data:  所有字段的data 列表；
    :return: 所有需要字段组成的列表；
    """
    need_data = []
    for one_data in all_data:
        for one_dict in one_data:
            need_dict = Method.get_dict_element(Config.smd_config("need_field_list"), one_dict, "smd_flags")
            if need_dict.get("ZWM") != '':
                need_data.append(need_dict)
    add_attribute_data = Model(need_data)
    return add_attribute_data





















