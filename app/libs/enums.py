from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100  # 本课程还是使用邮件
    USER_MOBILE = 101

    # 微信小程序 免密登录  公众号 OAuth2 跳转  半天的时间 前端 页面 css
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
