import pandas as pd

df = pd.read_csv("sample.csv")

data = pd.DataFrame({
    "Source": df["Department"],
    "Target": df["Object ID"],
    "Start": df ["AccessionYear"]
})

total_rows=0
rows_with_acception_year=0
rows_without_acception_year=0
rows_with_ok_credit_line=0
rows_with_messed_up_credit_line=0
rows_with_no_credit_line=0

for idx, row in data.iterrows():
    total_rows+=1
    year = row["Start"]
    if pd.notna(year):
        rows_with_acception_year+=1
        y = str(year)[0:4]
        data.loc[idx, "Start"] = y
    else:
        credit = df.loc[idx, "Credit Line"]
        if pd.notna(credit):
            rows_without_acception_year+=1
            l = len(credit)
            year_credit = credit[-4:l]
            if year_credit[-1] in "0123456789":
                rows_with_ok_credit_line+=1
                data.loc[idx, "Start"] = y
            else:
                rows_with_messed_up_credit_line+=1
                data.drop(idx,axis=0,inplace=True)
        else:
            rows_with_no_credit_line+=1
            data.drop(idx,axis=0,inplace=True)

print(len(df))
print("Total rows",total_rows)
print("Total rows WITH acception year",rows_with_acception_year)
print("Total rows WITHOUT acception year",rows_without_acception_year)
print("Rows WITHOUT acception year BUT with GOOD credit line",rows_with_ok_credit_line)
print("Rows with MESSED UP CREDIT LINES that should be erased",rows_with_messed_up_credit_line)
print("Rows WITHOUT CREDIT LINE",rows_with_no_credit_line)

#data.to_csv("new_edges_department_acquisition.csv", index=False)

edges = pd.read_csv("new_edges_department_acquisition.csv")

data_nodes = pd.DataFrame({
    "Id": edges["Target"],
    "start": edges ["Start"],
    "end": edges["Start"],
    "type": "Object",
    "departement": edges["Source"]
})

for idx, row in data_nodes.iterrows():
    year = row["start"]
    y = str(year)[0:4]  
    data_nodes.loc[idx, "start"] = y 
    year = row["end"]
    y = str(year)[0:4]  
    data_nodes.loc[idx, "end"] = y 

departments_nodes = pd.DataFrame({
    "Id": edges["Source"],
    "start": "NaN",
    "end": "NaN",
    "type": "Department",
    "departement": edges["Source"]
}).drop_duplicates(ignore_index=True)

nodes = data_nodes._append(departments_nodes, ignore_index=True)

#nodes.to_csv("ultimate_nodes.csv", index=False)
#data_nodes.to_csv("new_nodes_department_acquisition.csv", index=False)
