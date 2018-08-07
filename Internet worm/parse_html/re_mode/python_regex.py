# coding:utf-8
import re

def match_test():
    '''re.match()只有当string起始匹配成功才有返回值'''
    # 将正则表达式compile成pattern对象
    pattern = re.compile(r'\d+')
    # 使用re.match匹配文本，获取匹配结果
    result1 = re.match(pattern, '192abc')
    result2 = re.match(pattern, 'abc192adf')
    if result1:
        print(result1.group())
    else:
        print("匹配失败")
    if result2:
        print(result2.group())
    else:
        print("匹配失败")

def search_test():
    '''re.search（）扫描整个string进行匹配'''
    pattern=re.compile(r'\d+')
    result=re.search(pattern,'168abc192adc172')
    if result:
        print(result.group())
    else:
        print("匹配失败")

def split_test():
    '''利用re.split()将字符串string分割后返回列表'''
    #按一个或多个数字分割
    pattern=re.compile(r'\d+')
    result=re.split(pattern,'L1O2V23E4')
    print(result)

def findall_test():
    '''re.findall()搜索string，以列表list的形式返回能匹配的全部子串'''
    pattern=re.compile(r'\d+')
    result=re.findall(pattern,'A1B2c3d4')
    print(result)

def finditer_test():
    '''re.finditer()搜索string，以迭代器形式返回能匹配的全部match对象'''
    pattern = re.compile(r'\d+')
    result = re.finditer(pattern, 'A1B2c3d4')
    #遍历迭代器，利用group（）函数获取捕获的值
    for match in result:
        print(match.group(),end='\t')
    print()

def sub_test():
    '''pattern.sub()利用repl替换string中每一个匹配的子串后返回替换后的字符串'''
    #当repl为字符串时 可以用\id   \g<name>引用分组
    s='i say,i love you ever'
    pattern=re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')
    print(pattern.sub(r'\g<word2> \g<word1>',s))  #使用名称
    p=re.compile(r'(\w+) (\w+)')    #使用编号
    print(p.sub(r'\2 \1',s))

def subn_test():
    '''pattern.subn()返回sub（）函数替换次数'''
    s='i say,i love you ever'
    p=re.compile(r'(\w+) (\w+)')    #使用编号
    print(p.subn(r'\2 \1',s))


def match_items():
    #简化参数
    pattern=re.compile(r'(\w+) (\w+) (?P<word>.*)')
    match_item=pattern.match('I love you!')

    #match_object属性
    print("match.string:",match_item.string)
    print("match.re:", match_item.re)
    print("match.pos:", match_item.pos)
    print("match.endpos:", match_item.endpos)
    print("match.lastindex:", match_item.lastindex)
    print("match.lastgroup:", match_item.lastgroup)

    #match_object 方法
    print("match.group(1,2):", match_item.group(1,2))
    #无参默认为0
    print("match.group():", match_item.group())
    print("match.groupdict():", match_item.groupdict())
    print("match.start(2):", match_item.start(2)) #即第二组字符串的起始索引
    print("match.end(2):",match_item.end(2))      #即第二组字符串的终止索引
    print("match.start(3):", match_item.start(3))  # 即第三组字符串的起始索引
    print("match.span(2):", match_item.span(2))       #返回第二组的起始终止索引
    print("match.expand(r'\\2 \\1 \\3'):",match_item.expand(r'\2 \1 \3'))    #输出时交换组位置

print("="*20+"match()"+"="*20)
match_test()
print("="*20+"search()"+"="*20)
search_test()
print("="*20+"split()"+"="*20)
split_test()
print("="*20+"findall()"+"="*20)
findall_test()
print("="*20+"finditer()"+"="*20)
finditer_test()
print("="*20+"sub()"+"="*20)
sub_test()
print("="*20+"subn()"+"="*20)
subn_test()
print("="*20+"match_items()"+"="*20)
match_items()