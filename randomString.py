from random import randint

def radomStr(length: int or tuple, *, string: str = None):
    '''
    生成随机指定长度的字符串，可选母字符串
    :param length: 生成长度，(8, 16)为8位到16位之间随机长度。(int, int)
    :param string: 生成字符串的样本,默认：'0123456789qwertyuiopasdfghjklzxcvbnm'
    :return: 随机字符串
    '''
    strs = '0123456789qwertyuiopasdfghjklzxcvbnm' if not string else string
    return ''.join([strs[i] for i in [randint(0, len(strs) - 1) for _ in range(length)]]) if isinstance(length, int) else \
           ''.join([strs[i] for i in [randint(0, len(strs) - 1) for _ in range(randint(length[0], length[-1]))]])

if __name__ == '__main__':
    print(radomStr((6, 16), string='01'))
    print(radomStr(12))
