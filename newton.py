import re

fx = "(2*x)+(4*(x**2))+(4*x)+(2)"

t = fx.split("+")

d1 = r'^\(([0-9]+)\)$'
d2 = r'^\(([0-9]+)\*x\)$'
d3 = r'^\((x)\*\*([0-9]+)\)$'
d4 = r'^\(([0-9]+)\*\((x)\*\*([0-9])\)\)$'

df = ""
for termino in t:
    termino = termino.strip()
    r= re.search(d1,termino)
    if r:
        pass   

    r= re.search(d2,termino)
    if r:
        if df != "":
            df += "+"

        df += "(%s)" %(r.group(1))

    r=re.search(d3,termino)
    if r:
        if df != "":
            df += "+"

        n=int(r.group(2))
        df +="(%s*(x**%s))" %(n,n-1)

    r= re.search(d4,termino)
    if r:
        if df != "":
            df += "+"

        n=int(r.group(3))
        m=int(r.group(1))
        o=m*n
        df+="(%s*(x**%s))" %(o,n-1)

print "fx = %s" %(fx)
print "dx = %s" %(df)
