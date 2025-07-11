import pandas as pd
from string import digits

samp = pd.read_csv("sample.csv")

filt_df = samp[samp['Credit Line'] != ""]
filt_df = filt_df[["Object ID","Department","AccessionYear","Credit Line","Object Name","Classification"]]

credit_dep = []
for ind, row in filt_df.iterrows():
  obj = row["Object ID"]
  cred = row["Credit Line"]
  dep = row["Department"]
  creditors = []

  if ";" in cred:
    credits = cred.split("; ")
    for cr in credits:
      if "," in cr:
        sp = cr.split(",")
        res = any(char.isdigit() for char in sp[len(sp)-1])
        if res:
          sp.pop()
        c = ",".join(sp)
        creditors.append(c)
      else:
        creditors.append(cr)
  elif "," in cred:
    sp = cred.split(",")
    res = any(char.isdigit() for char in sp[len(sp)-1])
    if res:
      sp.pop()
    c = ",".join(sp)
    creditors.append(c)

  for creditor in creditors:
    pair = [creditor, dep]
    credit_dep.append(pair)


cred_dep_df = pd.DataFrame(credit_dep,columns=["Source","Target"])
cred_dep_df.to_csv("cred_dep.csv")

