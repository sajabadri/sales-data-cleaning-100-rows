import pandas as pd 
 
df=pd.read_csv("messy_sales_100_rows.csv")

new=[]
new2=[]

for city in df["city"]:
    if pd.isna(city):
        new.append(city)

    else:
        city=city.lower().strip()
        new.append(city)


df["city"]=new

for product in df["product_name"]:
    if pd.isna(product):
        new2.append(product)

    else:
        product=product.lower().strip()
        new2.append(product)

df["product_name"]=new2

df["quantity"]=pd.to_numeric(
    df["quantity"],errors="coerce"
)

df["unit_price"]=pd.to_numeric(
    df["unit_price"],errors="coerce"
)



df["order_date"]=pd.to_datetime(
    df["order_date"],errors="coerce"
)



need_review=df[
    df["order_date"].isna()|
    df["city"].isna()|
    df["quantity"].isna()|
    (df["quantity"]<=0)|
    (df["unit_price"] <= 0)|
    df["unit_price"].isna()|
    df["product_name"].isna()
]


new3=[]
for unit in df["unit_price"]:
    if unit<=0:
        unit=None
    new3.append(unit)


df["unit_price"]=new3


new4=[]
for unit in df["quantity"]:
    if unit<=0:
        unit=None
    new4.append(unit)


df["quantity"]=new4


df["total_sales"]=df["quantity"]*df["unit_price"]


df["month"]=df["order_date"].dt.month


df["order_status"] = "Valid"


invalid = (
    df["quantity"].isna() |
    (df["quantity"] <= 0)|
    df["order_id"].duplicated(keep=False)|
      df["order_date"].isna()|
        df["city"].isna()|
        df["quantity"].isna()|
        (df["quantity"]<=0)|
        (df["unit_price"] <= 0)|
        df["unit_price"].isna()|
        df["product_name"].isna()
)

need_review = df[invalid].copy()
df = df[~invalid].copy()



need_review["order_status"] = "Needs Review"
df["order_status"] = "Valid"

need_review.to_csv("need_review_100_rows.csv",index=False)
df.to_csv("cleaned_100_rows.csv",index=False)

print("Cleaned rows:", len(df))
print("Review rows:", len(need_review))
print("Total:", len(df) + len(need_review))

















