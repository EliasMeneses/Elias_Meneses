NAcl = int(input("Cual es el número IPV4 ACL? "))
if NAcl >= 1 and NAcl <= 99:
    print("Este es un ACL IPv4 estandar ")
elif NAcl >=100 and NAcl <= 199:
    print("Este es una ACL IPv4 extendida ")
else:
    print("Esta ACL IPv4 no es extendida o estandar. ")