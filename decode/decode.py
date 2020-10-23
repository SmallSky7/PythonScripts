import base64
import os

'''
对文件作base64解码，并转存为相应的文件
'''

def decode(input_data):
    dir_name = os.path.dirname(__file__)
    file_path = dir_name + '\\' + '输出结果.xlsx'

    # 对传入数据作base64解码
    raw_data = base64.b64decode(input_data)
    save_bin(file_path, raw_data)


def save_bin(path, data, mode = 'wb+'):
    try:
        with open(path, mode = mode) as fp:
            fp.write(data)
            fp.flush()
            print(u'保存文件：' + path)
    except IOError as e :
        print(str(e))
        return
