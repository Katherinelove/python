favoriet_lang={"zengshuai":["english","chinese"],
               "gouto":["python","c"],
               "yueren":["python"],
               }
for name,langs in favoriet_lang.items():
    if len(langs)==1:
        print(name+"favorite book is",end="")
    else:
        print(name+"favorite book are：",end="")
    for lang in langs:
        print("\t"+lang,end="")
    print()

