import pandas as pd

xls = pd.ExcelFile("KAN1.xlsx")
df = pd.read_excel(xls,index_col=False, na_values=["NA"], engine='openpyxl')

def CollumnDeletion(x):
    x = x.drop(columns=["F"])
    return x

df = CollumnDeletion(df)

def highlight_col(row):
    if row["Echo"] == "YES":
        return ["background-color: yellow"] * len(row)
    else:
        return ["background-color: red"] * len(row)

df = df.style.apply(highlight_col, axis=1)
with pd.ExcelWriter("raport charlie.xlsx") as writer:
    df.to_excel(writer, index=False)

