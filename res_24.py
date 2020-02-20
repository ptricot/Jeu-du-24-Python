
def test (L):
    n=len(L)
    if n==1:
        return L[0]==24
    else:
        for i in range (n):
            for j in range (n):
                if j < i:
                    G=L[:]
                    a,b=G[i],G[j]
                    G.pop(max(i,j))
                    G.pop(min(i,j))
                    if ( test(G+[a+b]) or test(G+[a*b]) or test(G+[abs(b-a)])):
                        return True
                    if a!=0 and b!=0:
                        if (test(G+[max(a,b)/min(a,b)])):
                            return True
                        if (test(G+[min(a,b)/max(a,b)])):
                            return True
    return False


def test2 (L):
    n=len(L)
    if n==1:
        if L[0]==24:
            return (True,"")
        else:
            return (False," ")
    else:
        for i in range (n):
            for j in range (n):
                if j < i:
                    G=L[:]
                    a,b=G[i],G[j]
                    G.pop(max(i,j))
                    G.pop(min(i,j))
                    G1,G2,G3=test2(G+[a+b]),test2(G+[a*b]),test2(G+[abs(b-a)])
                    if G1[0]:
                        return (True," ("+str(a)[:5]+"+"+str(b)[:5]+")="+str(a+b)[:5]+ ',' +G1[1])
                    if G2[0]:
                        return (True," ("+str(a)[:5]+"*"+str(b)[:5]+")="+str(a*b)[:5]+','+G2[1])
                    if G3[0]:
                        return (True," (" + str(max(b,a))[:5] + "-" + str(min(b,a))[:5] + ")=" + str(max(b,a)-min(b,a))[:5] + ',' + G3[1])
                    if a!=0 and b!=0:
                        G4=test2(G+[max(a,b)/min(a,b)])
                        G5=test2(G+[min(a,b)/max(a,b)])
                        if G4[0]:
                            return (True,"  (" + str(max(b,a))[:5] + "/" + str(min(b,a))[:5]+")=" + str(max(b,a)/min(b,a))[:5] + "," + G4[1])
                        if G5[0]:
                            return (True,"  (" + str(min(b,a))[:5] + "/" + str(max(b,a))[:5]+")=" + str(min(b,a)/max(b,a))[:5] + "," + G5[1])
    return (False,"")