# %%
!uv add openpyxl

# %%
import pandas as pd
# %%
df_sales1 = pd.read_csv("../data/Sales_MedicStore_part1.csv", sep=";")
df_sales2 = pd.read_csv("../data/Sales_MedicStore_part2.csv", sep=";")
df_sales1
df_sales2
#%%
df_mapping = pd.read_excel("../data/Mapping.xlsx")
df_mapping

# assemble the two sales dataframes into one
# %%
df_sales = pd.concat([df_sales1, df_sales2], ignore_index=True)
df_sales


df_final_sales = pd.merge(df_sales, df_mapping, left_on="Sub-Category", right_on="Sub-Category")
df_final_sales

# compute the total sales
# %%
df_final_sales.columns
df_final_sales["Total Sales"] = df_final_sales["Unit Price"] * df_final_sales["Quantity"]
print("Total Sales: ", df_final_sales["Total Sales"].sum()  )

# export the final dataframe to an excel file

# %%
df_final_sales.to_excel("../data/Final_Sales.xlsx", index=False)

# 1.What is the number of lines and columns in our original datasets and in our final dataset ?
#%%
df_sales1.shape, df_sales2.shape, df_final_sales.shape

# 2. What are the column names in the final dataset?
# %%
df_final_sales.columns

# 3. what are the top 5 lines of the dataset?
# %%
df_final_sales.head(5)

# 4. what are the last 5 lines of the dataset?
# %%
df_final_sales.tail(5)

# 5. Make a statistical description of all the dataset
# %%
df_final_sales.describe()

# 1) how many orders do we have?
# %%
df_final_sales["Order ID"].nunique()

# 2) what is the total sales amount?
# %%
df_final_sales["Total Sales"].sum()

# 3) who is the top 3 customers that make the most purchases?
# %%
df_final_sales.value_counts("Customer Name").head(3)

# 4) what is the total sales for france?
# %%
df_final_sales[df_final_sales["Country"] == "France"]["Total Sales"].sum()

# 5) how much does the total sales of france represent compared to the total global sales?
# %%
df_final_sales[df_final_sales["Country"] == "France"]["Total Sales"].sum() / df_final_sales["Total Sales"].sum() * 100
