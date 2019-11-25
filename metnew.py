import re

#fx= "(x**3)+(3*x)+(2)"
fx= raw_input("ingresa una funcion\n")
t = fx.split("+")

d1 = r'^\([1-9]+\)$'
d2 = r'^\(([1-9]+)\*x\)$'
d3 = r'^\((x)\*\*([1-9]+)\)$'
d4 = r'^(([1-9]+)\*\((x)\*\*([1-9]+)\)\)$' 

df =""

for termino in t:
    termino = termino.strip()
    r= re.search(d1,termino)
    if r:
            pass
    r= re.search(d2,termino)
    if r:

            df += r.group(1)
    r = re.search (d3,termino)
    if r:

            n= int (r.group(2))
            df += "%s x** %s + "%(n, n-1)
    r = re.search(d4,termino)
    if r:

            print r.group(0), r.group(1), r.group(2), r.group(3),
            k= int(r.group(3))
            n= int(r.group(1))
            df +="%s x** %s + " %(n-1,k)

print fx
print df
