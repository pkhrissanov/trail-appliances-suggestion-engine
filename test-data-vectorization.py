from os import read
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MultiLabelBinarizer
import ast
import pandas as pd


data_raw = pd.read_csv("data/test-data/test.csv")
scaler = StandardScaler() # decided that standard scaler should be ok for this data set.
numeric_collumns = ["width_inches", "height_inches", "depth_inches", "burners", "price", "rating"]
data_raw_scalable_values = data_raw[numeric_collumns]
data_raw_scaled_values = scaler.fit_transform(data_raw_scalable_values)
numeric_data_scaled = pd.DataFrame(data_raw_scaled_values, columns=numeric_collumns)
numeric_data_scaled.to_csv("data/test-data/numeric_data_scaled.csv", index=True)


data_raw["features"] = data_raw["features"].apply(ast.literal_eval)

mlb = MultiLabelBinarizer()

features_encoded = mlb.fit_transform(data_raw["features"])

features_df = pd.DataFrame(
    features_encoded,
    columns=mlb.classes_,
    index=data_raw.index
)
features_df.to_csv("data/test-data/features_encoded.csv", index=True)


encoder_collumns = ["brand", "category", "range_type", "finish"]
encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

encoded_values = encoder.fit_transform(data_raw[encoder_collumns]) #learns what features exist
encoded_names = encoder.get_feature_names_out(encoder_collumns) #gets the feature names out
encoded_df = pd.DataFrame(encoded_values, columns=encoded_names)
encoded_df.to_csv("data/test-data/encoded_categorical_values.csv", index=True)



encoder = OrdinalEncoder(categories=[['budget', 'mainstream', 'premium', 'luxury']])
data_raw["brand_tier"] = encoder.fit_transform(data_raw[["brand_tier"]])
brand_tier_encoded = pd.DataFrame(data_raw[["brand_tier"]])
brand_tier_encoded.to_csv("data/test-data/brand_tier_encoded.csv", index=True)


brand_tier_encoded = pd.read_csv("data/test-data/brand_tier_encoded.csv")
encoded_categorical_values = pd.read_csv("data/test-data/encoded_categorical_values.csv")
numeric_data_scaled = pd.read_csv("data/test-data/numeric_data_scaled.csv")
features_encoded = pd.read_csv("data/test-data/features_encoded.csv")

final_data = pd.concat([brand_tier_encoded, encoded_categorical_values, numeric_data_scaled, features_encoded], axis=1)
final_data.drop("Unnamed: 0", axis=1, inplace=True)
final_data.to_csv("data/test-data/final_eval_data.csv", index=True)