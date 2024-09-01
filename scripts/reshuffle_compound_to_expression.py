# Reorganize the rows of OmicsExpressionProteinCodingGenesTPMLogp1.csv to match the rows of /_PRISM24q2_data.csv

import pandas as pd
import numpy as np

df2 = pd.read_csv("../csv/OmicsExpressionProteinCodingGenesTPMLogp1.csv")
df3 = pd.read_csv("../csv/PRISM24q2_data.csv")

# Check if each element in the first column of df2 is unique
df2_model_id = df2.iloc[:, 0]

if df2_model_id.is_unique:
    print("The first column of df2 has all unique elements.")

# iterate over each row of df3 and find whether the cell line name is present in df2
# if present, then append the row to a new dataframe

df3_model_id = df3.iloc[:, 0]
df3__viability = df3.iloc[:, 1]

# List of matched rows in df2
matched_rows_df2 = []
# Mask of rows to keep in df3, where there is a matching row in df2
mask_df3 = []

# Iterate over each row in df3 and find matching rows in df2
for i in range(len(df3_model_id)):
    model_id = df3_model_id[i]

    matched_row = df2[df2.iloc[:, 0] == model_id]
    
    # if column 1 of matched_row is empty
    if matched_row.empty or np.isnan(df3__viability[i]):
        print("No matching row found for model_id: {0}".format(model_id))
        mask_df3.append(False)
    else: 
        matched_rows_df2.append(matched_row)
        mask_df3.append(True)

# Concatenate the matched rows into a new DataFrame
df2_new = pd.concat(matched_rows_df2, ignore_index=True)
df3_new = df3[mask_df3]

# check if df2_new has the same number of rows as df3
if len(df2_new) == len(df3_new):
    print("The number of rows in the two dataframes are equal.")

print("data_saved")

# save the new df2_new
df2_new.to_csv("../exported-csv/ReshuffledForOmicsExpressionProteinCodingGenesTPMLogp1.csv", index=False)
df3_new.to_csv("../exported-csv/ReshuffledFor__PRISM24q2_repurposing.csv", index=False)
