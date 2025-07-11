import pandas as pd
from string import digits

samp = pd.read_csv("sample.csv")

filt_df = samp[samp['Object Name'] != ""]
filt_df = filt_df[["Object ID","Department","AccessionYear","Credit Line","Object Name","Classification"]]

type_dep = []
for ind, row in filt_df.iterrows():
  obj_name = row["Object Name"].lower()
  obj = row["Object ID"]
  dep = row["Department"]
  remove_digits = str.maketrans(' ', ' ', digits)
  obj_name = obj_name.translate(remove_digits)
  obj_name = obj_name.replace(" ; ","; ")
  if ";" in obj_name:
    type_list = []
    s = obj_name.split("; ")
    cls = row["Classification"].lower()
    for i in s:
      if i not in cls:
        type_list.append(i)
    if len(type_list) == 0:
      obj_type = s
    else:
      obj_type = type_list

  elif "," in obj_name:
    type_list = []
    s = obj_name.split(", ")
    cls = row["Classification"].lower()
    for i in s:
      if i not in cls:
        type_list.append(i)
    if len(type_list) == 0:
      obj_type = s
    else:
      obj_type = [type_list[0]]

  else:
    obj_type = [obj_name]

  for i in obj_type:
    pair = [i,dep]
    type_dep.append(pair)

type_dep_df = pd.DataFrame(type_dep,columns=["Source","Target"])
type_dep_df.to_csv("type_dep.csv")

