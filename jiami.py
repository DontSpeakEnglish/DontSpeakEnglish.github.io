from json import load  # 导入 JSON 加载函数

def fenge(word: str) -> list:  # 定义 fenge 函数，接收一个字符串并返回列表
    '''
        用于分割字符串
        Args:
            word (str): 需要分割的字符串
        Returns:
            list: 字符串拆分后的字符列表
    '''
    return [*word]  # 将字符串中的每个字符放入列表中返回


def zimu_sajinzhi(zimu: str) -> str or dict:  # 添加返回类型注释
    '''
        将字母转换为三进制表中指定值
        Args:
            zimu (str): 须转换的字母
        Returns:
            str: 转换后的值;
            dict: 错误内容，包含错误信息
    '''
    try:
        suanjinzhima = ducujson("sanjinzhibiao.json")  # 读取三进制字母表
        return suanjinzhima[zimu]  # 返回对应的三进制值
    except KeyError:  # 处理未找到的键
        return {'E': f'字母"{zimu}"不在三进制表中'}  # 返回具体的错误信息
    except Exception as e:  # 捕获其他异常
        return {'E': str(e)}  # 返回错误信息


def ducujson(json_path: str) -> dict:  # 添加参数类型和返回类型注释
    '''
        从指定路径读取 JSON 文件并返回其内容
        Args:
            json_path (str): JSON 文件的路径
        Returns:
            dict: 读取的 JSON 数据
    '''
    with open(json_path, "r", encoding='utf-8') as f:  # 打开 JSON 文件
        zhanhuan = load(f)  # 加载 JSON 数据
        return zhanhuan  # 返回加载的数据


def jiachen(shu: str, count: int = 4) -> str:  # 允许用户指定循环次数，默认为 4
    '''
        对字符串中的数字进行处理，计算（每个数字 + 1) * 2 的值
        Args:
            shu (str): 需要处理的字符串，包含数字
            count (int): 处理的数字个数，默认为 4
        Returns:
            str: 处理后拼接的字符串
    '''
    list_shu = fenge(shu)  # 将输入的字符串分割成列表
    for i in range(min(count, len(list_shu))):  # 遍历列表中前 count 个元素
        list_shu[i] = (int(list_shu[i]) + 1) ** 2  # 计算
    return ''.join(map(str, list_shu))  # 使用 join 拼接字符串，返回最终结果


def junenhuan(word: str, htgu: int = 3) -> str:  # 定义函数 junenhuan，接收一个字符串和环形后推的个数
    '''
        聚能环加密，将字符串中的字符根据给定的 htgu 值进行循环移动
        Args:
            word (str): 输入的字符串
            htgu (int): 环形后推的个数，默认为 3
        Returns:
            str: 移动后的字符串
    '''
    aword = fenge(word)  # 将输入的字符串分割成列表
    n = len(aword)  # 获取 aword 的长度
    for i in range(n):  # 遍历 aword 的每一个字符索引
        hi = (i + htgu) % n  # 计算新的索引 hi，使用模运算避免边界检查
        aword[i] = aword[hi]  # 将 aword 中 hi 索引处的字符赋值给 aword 的当前索引
    return ''.join(aword)  # 使用 str.join() 方法将 aword 中的字符拼接成字符串并返回


def bijiami(word: str, htgs: int = 5) -> str:  # 定义函数 bjiami，接收一个字符串和字母表后推的个数
    '''
        B加密
        使用b加密加密单词中的英文字母
        Args:
            word (str): 须加密单词
            htgs (int): 字母表后推个数 默认5个字母
        Returns:
            str: 加密后的单词 (全部大写）
    '''
    aword = fenge(word)  # 将输入的字符串分割成列表
    for i in range(len(aword)):  # 遍历每个字母
        asc = ord(aword[i])
        if (asc > 64 and asc < 91) or (asc > 96 and asc < 123):
            asc = asc + htgs if asc <= 90 else asc - 32 + htgs  # 计算后推后字母的ASCII
            hasc = asc - 26 if asc > 90 else asc
            aword[i] = chr(hasc)
    return ''.join(aword)

print(bijiami("djkhf"))