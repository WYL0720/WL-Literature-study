import pandas as pd
import re

csv_path = "../../Literature List.csv"
df = pd.read_csv(csv_path)

ml_models = [
    "SVM", "Random Forest", "XGBoost", "CNN", "Autoencoder","neural network"
    "LASSO", "Logistic Regression", "Gradient Boosting", "Decision Tree", "RandomForest","Deep learning"
]


data = []
for index, row in df.iterrows():
    title = str(row.get("Title", ""))
    abstract = str(row.get("Abstract", ""))
    
    year = row.get("Year", "")
    authors = row.get("Author", "")
    journal = row.get("Journal", "")
    
    data_source = ""
    matches = re.findall(r"plasma|urine|serum|tissue|cell line|cohort|hospital", abstract, re.I)
    if matches:
        data_source = ", ".join(list(set([x.lower() for x in matches])))
    
    cohort_size = ""
    match = re.search(r"(\d{1,5})\s*(patients|subjects|volunteers|cases)", abstract, re.I)
    if match:
        cohort_size = match.group(1)
    
    models_found = [m for m in ml_models if re.search(r"\b"+re.escape(m)+r"\b", abstract, re.I)]
    model_found = ", ".join(models_found)
    
    data.append([year, authors, journal, data_source, cohort_size, model_found])

output_path = "../../literature_summary.csv"
df_out = pd.DataFrame(data, columns=["Year","Author","Journal","Data source","Cohort size","Machine Learning Model"])
df_out.to_csv(output_path, index=False)

print(f"saved at {output_path}")
