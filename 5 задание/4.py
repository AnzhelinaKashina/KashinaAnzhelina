def asv(x ,y):
    izmenrasst=x
    k=1
    while y> izmenrasst:
        izmenrasst+=izmenrasst*0.1
        k+=1
    print(k)
asv(int(input()),int(input( )))

