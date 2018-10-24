class Ten:
    name = 'ten'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ['name', 'age']

    def __getitem__(self, item):
        return getattr(self, item)


# r = {
#     'name': 'ten'
# }
# r = dict(name='ten')

t = Ten()
d = dict(t)
print(d)

# # __dict__ 不会记录类的属性值
# t = Ten()
# print(t.__dict__)
