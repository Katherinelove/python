responds={}
polling_active=True
while polling_active:
    name=input("what's your name?")
    respond=input("which books would you like to read?")
    responds[name]=respond
    repeat=input("would you like to let another person respond?(yes/no)")
    if repeat=="no":
        polling_active=False
print("\nthe polling result")
for name,respond in responds.items():
    print(name+"like to read "+respond)