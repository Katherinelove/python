from email.utils import parseaddr,formataddr
addr="15281857366@16.com"
print(parseaddr("loveyou<{}>".format(addr)))
print(parseaddr("loveyou<%s>"%addr))