flags = 0

admin_permission = 1 << 0
content_creator_permission = 1 << 1

flags |= admin_permission
flags |= content_creator_permission

you_content_creator = flags & content_creator_permission != 0

if you_content_creator:
    print('ti content creator')
else:
    print('ti ne content creator')

print(f'user flags: {flags}')
