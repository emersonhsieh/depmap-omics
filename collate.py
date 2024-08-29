# Match the cell line name prefixed with ACH- in fake_dummy_AUC_MATRIX.csv with the cell line name in Model.csv

import pandas as pd

# load the two csv files
df1 = pd.read_csv("./csv/Model.csv")
# df2 = pd.read_csv("./csv/OmicsExpressionProteinCodingGenesTPMLogp1.csv")
df3 = pd.read_csv("./csv/fake_dummy_AUC_MATRIX.csv")

# take the first column of df3
df3_cell_line_collated = df3.iloc[:, 0]

# strip the strings after the underscore in the first column of df3
df3_cell_line_collated = df3_cell_line_collated.str.split("_", expand=True)[0]

print(df3_cell_line_collated)

# keep modelId and cell line in a new dataframe
df1_model_id = df1["ModelID"]
df1_cell_line_name = df1["StrippedCellLineName"]

# define new column in df3 called CellLineName
df3["ModelID"] = ""

# new column in df3 to store corresponding CellLine names with ModelID of df1
for i in range(len(df3_cell_line_collated)):
    for j in range(len(df1_model_id)):
        if df3_cell_line_collated[i] == df1_cell_line_name[j]:
            df3.loc[i, "ModelID"] = df1_model_id[j]

# save the new df3 with ModelID
df3.to_csv("./csv/fake_dummy_AUC_MATRIX_with_ACH.csv", index=False)