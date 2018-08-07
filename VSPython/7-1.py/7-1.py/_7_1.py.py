unconfirmed_users=["zengshuai","hongliu","wuyue"]
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("verifying user:"+current_user)
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user)

lst=["cat","dog","cat","ox","cat"]
print(lst)
while "cat" in lst:
    lst.remove("cat")
print(lst)
