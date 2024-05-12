list = ['Post', 'UserInfo', 'Image', 'Comment', 'Like', 'Group', 'Subscription']


for i in list:

    print(f'''class {i}ViewSet(ModelViewSet):
    serializer_class = {i}Serializer
    queryset = {i}.objects.all()'''.format(i))

for i in list:
    print(f'''router.register(r"{i.lower()}s", {i}ViewSet)'''.format(i))