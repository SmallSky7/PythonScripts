import os
import sys

'''
批量修改文件夹下所有文件的后缀名
'''

def Modify_suffix():
    old_suffix = sys.argv[1]
    new_suffix = sys.argv[2]
    filepath = sys.argv[3]
    count = 0

    if filepath == ' ' or filepath == None:
        filepath = os.path.dirname(os.path.abspath(__file__))

    files = os.listdir(filepath)

    for file in files:
        portion = file.split('.')
        portionLength = len(portion)
        if portion[portionLength-1] == old_suffix:
            count = count + 1
            filename = []
            for i in range(0,portionLength-1):
                filename.append(portion[i])
                filename = ".".join(filename)
            newname = filename + "." + new_suffix
            os.chdir(filepath)
            os.rename(file, newname)
    if count == 0:
        print("\n该文件夹下没有后缀为" + old_suffix + "的文件")
    else:
        print("\n后缀已经修改为" + new_suffix)


if __name__ == '__main__':
    Modify_suffix()

