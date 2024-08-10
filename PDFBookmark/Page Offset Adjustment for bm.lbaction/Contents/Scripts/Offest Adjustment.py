#!/usr/bin/env python3

import os
import re
import sys

def main():
    path = sys.argv[-1]
    offset = int(input('请输入页码偏移量：'))
    file_name = os.path.basename(path)
    new_file_name = file_name.split(".")[0] + "_new.bm"
    new_file_path = os.path.join(os.path.dirname(path), new_file_name)

    with open(path, "r") as f:
        lines = f.readlines()

    with open(new_file_path, "w") as f:
        i = 0
        j = 1
        for line in lines:
            match = re.search('(\d+)$', line)
            i += 1
            if match:
                num = int(match.group(1))
                if num - j >= 20:
                    print("第 %d 行目录页码与前一行目录页码差值达 %d 页，请检查是否缺失部分目录！" % (i , num - j))
                elif num - j < 0:
                    print("第 %d 行出现页码倒挂（此行目录项页码 %d 小于前一目录项 %d），请检查OCR结果是否有误！" % (i , num ,j ))
                j = num
                new_num = num + offset
                # new_line = line[::-1].replace(str(num)[::-1], str(new_num)[::-1] , 1 )[::-1] # 实现从右到左替换一次
                new_line = re.sub(r'(\d+)$', str(new_num), line)
                f.write(new_line)
            else:
                print("第 %d 行不以数字结尾，请检查OCR结果是否有误！" % (i))
                f.write(line)
    print('偏移量纠正完成！新文件路径：%s！' %(new_file_path))
                
                
if __name__ == '__main__':
    main()
