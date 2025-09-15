import numpy as np
import pandas as pd

def f(x):
    return (x*np.exp(2*x))

def simpson(a,b,n):
    h=(b-a)/n
    df=pd.DataFrame(columns=["Xi","f(xi)"])
    for i in np.arange(a,b+h,h):
        df.loc[len(df)]=[i,f(i)]
    o=np.sum([df.iloc[j,1] for j in range(1,n,2)])
    e=np.sum([df.iloc[k,1] for k in range(2,n-1,2)])
    s=((b-a)/(3*n))*(f(a)+f(b)+(4*(o))+(2*(e)))
    return s

segments=np.arange(2,22,2)
exact=5216.9
a=0
b=4
df2=pd.DataFrame(columns=["Error","Approximate Results","Segments"])
for n in segments:
    app=simpson(a,b,n)
    err=abs(exact-app)
    df2.loc[len(df2)]=[err,app,n]
print(df2)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6),dpi=150)
plt.style.use('ggplot')
plt.title("Error Vs. Number of segments curve")
plt.xlabel("Number of segments (n)",fontsize=12,color="black")
plt.ylabel(r"$\text{Error} = \left| M_{\text{exact}} - M_{\text{approx}} \right|$",fontsize=12,color="black")
plt.plot(segments,df2["Error"],color="blue",linestyle="-",marker="o")
plt.grid(True)
ax=plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.xticks(range(0, int(np.max(segments))+2, 1))
plt.yticks(range(0, int(np.max(df2["Error"]))+500, 500))
plt.show()