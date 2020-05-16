from T3_SMD_Method import T3_01_SMD_Method
from T3_SMD_Method import T3_02_ShuX_model
if __name__ == '__main__':
    '''获取本机smd path'''
    smd_dir_path = T3_01_SMD_Method.get_smd_root('smd_file_path')
    print(smd_dir_path)
    '''拼接SMD文件所在目录列表'''
    a = T3_01_SMD_Method.get_smd_dir(smd_dir_path)
    '''便利获取所有的smd文件'''
    b = T3_01_SMD_Method.get_smd_file(a)
    c = T3_01_SMD_Method.get_all_smd_content(b)
    d = T3_01_SMD_Method.need_data_list(c)
    data = T3_02_ShuX_model.Model(d).RangeDataList
#  Mongodb_client.MongoCLient().MongoCLient("T3-zt", "SMD_data", "patch", d)
