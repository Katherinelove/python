names=[]
for i in range(5):
	new_name=input()
	names.append(new_name.lower())
print(names)
current_users=names[:]
print(current_users)
print(names)
print("*"*20)
new_users=[]
for i in range(5):
	new_name=input()
	new_users.append(new_name)
print(new_users)
for new_user in new_users:
	if new_user.lower() in current_users:
		print("sorry!{} �Ѿ����ڣ�".format(new_user))
	else:
		print("{} �Ϸ�".format(new_user))
