class Scope:
    is_super_user = False
    allow_api = []
    allow_redprint = []
    forbidden_api = []

    def __add__(self, other):
        self.allow_api = list(set(self.allow_api + other.allow_api))
        self.allow_redprint = list(
            set(self.allow_redprint + other.allow_redprint))
        self.forbidden_api = list(
            set(self.forbidden_api + other.forbidden_api))
        return self


class UserScope(Scope):
    allow_api = []
    allow_redprint = ['v1.gift']


class AdminScope(Scope):
    allow_api = ['v1.user:super_get_user']
    allow_redprint = ['v1.user']
    forbidden_api = ['v1.user:super_delete_user']
    # 视图 100个，维护起来会崩溃
    # 98个的权限， 能够排除其他的两个视图函数


# 超级管理员，不能任何情况都拥有所有的权限
class SuperScope(Scope):
    is_super_user = True


def is_in_scope(scope, endpoint):
    # token scope AdminScope UserScope
    # 权限有变化，需要重新生成token才行
    # AdminScope str
    # scope() ?
    # 反射 java c#
    # 一切都是对象
    # LEGB
    # endpoint  v1.view_func  v1.redprint:view_func
    # gl = globals()
    scope = globals()[scope]()

    splits = endpoint.split(':')
    redprint = splits[0]
    if scope.is_super_user:
        return True
    if endpoint in scope.forbidden_api:
        return False
    if endpoint in scope.allow_api:
        return True
    if redprint in scope.allow_redprint:
        return True
    else:
        return False
