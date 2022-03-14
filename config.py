import hashlib
from urllib import parse

class Config:
    def __init__(self):

######################### 填写用户信息 ##############################
        # WgpSecBot API
        # 获取方式：加入微信群 WgpSec 狼组安全团队
        self.bot = 'e365023b8769914c2b15e5495c01543a'

        # 请输入用户名
        self.name = '1148202106@qq.com'

        # 请输入密码
        self.password = '********'
    

        # 请选择安全提问,填编号
        self.problem = '1'
        
        # 1、母亲的名字
        # 2、爷爷的名字
        # 3、父亲出生的城市
        # 4、您其中一位老师的名字
        # 5、您个人计算机的型号
        # 6、您最喜欢的餐馆名称
        # 7、驾驶执照的最后四位数字

        # 提问的答案
        self.answer = '*****'
        
#################################################################

    def Password(self):
        bety = bytes(self.password,encoding='utf-8')
        str_md5 = hashlib.md5(bety).hexdigest()
        return str_md5

    def Name(self):
        text = parse.quote_plus(self.name, 'utf-8')
        return text

    def Answer(self):
        txt = parse.quote_plus(self.answer, 'utf-8')
        return txt


    def main(self):
        self.Name()
        self.Password()
        self.Answer()

if __name__ == '__main__':
    user = Config()
    user.main()
