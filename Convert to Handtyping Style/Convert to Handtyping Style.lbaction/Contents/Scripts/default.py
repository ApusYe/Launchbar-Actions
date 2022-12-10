#!/opt/homebrew/bin/python3
#
# LaunchBar Action Script
#
import sys
import re

def remove_spaces(str):
    str = re.sub('([\u4e00-\u9fa5\d]{1})[\u00A0\u0020\u3000]+([\u4e00-\u9fa5\d]{1})','\g<1>\g<2>',str) #去除汉字（含阿拉伯数字）之间的空格
    str = re.sub('[\u00A0\u0020\u3000]+([，。？！（）：；]+)','\g<1>',str) #去除标点符号前的空格
    str = re.sub('([，。？！（）：；]+)[\u00A0\u0020\u3000]+','\g<1>',str) #去除标点符号后的空格
    str = re.sub('([\u4e00-\u9fa5]{1})[\u00A0\u0020\u3000]+([A-Za-z]{1})','\g<1>\g<2>',str) #去除汉字（含阿拉伯数字）与英语单词之间的空格
    str = re.sub('([A-Za-z]{1})[\u00A0\u0020\u3000]+([\u4e00-\u9fa5]{1})','\g<1>\g<2>',str) #去除英语单词与汉字（含阿拉伯数字）之间的空格
    # 没有对引号进行处理，因为暂时没想到可以一步到位的方案
    return str

def C_trans_to_E(str):
    C_pun = u'，。？！（）：；'
    E_pun = u',.?!():;'
    table = {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}
    return str.translate(table)

print(remove_spaces(C_trans_to_E(sys.argv[1])))
# print(remove_spaces(C_trans_to_E('这是一条 test用代码 ,. ?!()  :; 我是 中国 人')))

