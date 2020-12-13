import re


def get_js_str(path, file):
    f = open(path + file, 'r', encoding='utf-8')
    line = f.readline()
    js_str = ''
    while line:
        js_str = js_str + line
        line = f.readline()
    return js_str


def index_str(base_str, tag_str):
    tag_len = len(tag_str)
    base_len = len(base_str)
    tag_index = []
    i = 0
    while tag_str in base_str[i:]:
        tmp_index = base_str.index(tag_str, i, base_len)
        tag_index.append(tmp_index)
        i = (tmp_index + tag_len)
    return tag_index


def get_class_inner_str(js_str):
    a_list, b_list = index_str(js_str, '{'), index_str(js_str, '}')
    c_list = (a_list + b_list)
    c_list.sort()
    class_start, class_end = 0, 0
    d_list = []
    for tag in c_list:
        d_list.append('a' if tag in a_list else 'b')
    for num in range(0, len(c_list) - 1):
        if d_list[num] == d_list[num + 1]:
            if c_list[num] in a_list:
                class_start = c_list[num]
            if c_list[num] in b_list:
                class_end = c_list[num + 1]
    return js_str[class_start + 1: class_end] \
        .replace('\n', '') \
        .replace('   ', ' ') \
        .replace('  ', ' ') \
        .replace('  ', ' ')


def get_class_name(js_str):
    a1 = js_str.find('class') + 5
    a2 = js_str[a1:].find('{') + a1
    s1 = js_str[a1:a2]
    return s1[:s1.find('extend')].replace(' ', '') if len(re.findall('extends', js_str)) > 0 else s1.replace(' ', '')


def get_field_list(inner_str):
    field_list = []
    b1 = inner_str[inner_str.find('constructor') + 11:].find('(')
    b2 = inner_str[inner_str.find('constructor') + 11:].find(')')
    field_list += inner_str[inner_str.find('constructor') + 11 + b1 + 1: inner_str.find('constructor') + 11 + b2].replace(' ', '').split(',')
    return field_list


def get_constructor_content(inner_str):
    b1 = inner_str[inner_str.find('constructor') + 11:].find('(')
    b2 = inner_str[inner_str.find('constructor') + 11:].find(')')
    return 'constructor(' + inner_str[inner_str.find('constructor') + 11 + b1 + 1 : inner_str.find('constructor') + 11 + b2]\
        .replace(' ', '')\
        .replace(',', ', ') + ')'


def get_method_list(inner_str):
    a_list = index_str(inner_str, '{')
    method_list = []
    for c in a_list:
        if inner_str[c - 2: c].replace(' ', '') == ')':
            method_name = ''
            for num in (
                    range(2, inner_str.rfind('(', 0, c)) if inner_str[inner_str.rfind('(', 0, c) - 1] == ' ' else
                    range(1, inner_str.rfind('(', 0, c))):
                if inner_str[inner_str.rfind('(', 0, c) - num] != ' ':
                    method_name += inner_str[inner_str.rfind('(', 0, c) - num]
                else:
                    break
            method_name = method_name[::-1]
            if not method_name == 'constructor':
                method_list.append(method_name + '(' +
                                   inner_str[inner_str.rfind('(', 0, c) + 1: inner_str.rfind(')', 0, c)]
                                   .replace(' ', '').replace(',', ', ') + ')')
    return method_list


def ex_print(content):
    str_len = len(content)
    if str_len <= 25:
        print('| - ' + content, end='')
        for num in range(str_len, 25):
            print(' ', end='')
        print('|')
    else:
        print('| - ' + content[: 24], end=' |\n')
        p = int((str_len - 24) / 26)
        for num in range(0, p):
            print('| ' + content[24 + num * 26: 24 + (num + 1) * 26] + ' |')
        print('| ' + content[24 + p * 26: str_len], end='')
        for num in range((str_len - 24) % 26, 27):
            print(' ', end='')
        print('|')
