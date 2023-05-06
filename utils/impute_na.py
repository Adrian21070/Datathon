import pandas as pd

def impute_na(df: pd.DataFrame, method: str, numeric_only: bool = True) -> pd.DataFrame:
    if numeric_only:
        numeric_cols = df.select_dtypes(include="number").columns.to_list()
        if method == "median":
            df.fillna(df.select_dtypes(include="number").median(), inplace=True)
            return df
        elif method == "mean":
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            return df
        elif method == "sample":
            for column in numeric_cols:
                sample = df[column].dropna().sample(df[column].isna().sum()).to_list()
                sample = pd.Series(sample, index=df[df[column].isna()].index)
                df[column].fillna(sample, inplace=True)
            return df
        elif method == "drop":
            return df.loc[:, numeric_cols].dropna(axis=0)
        else:
            print("No imputation performed.")
            return df
    else:
        if method == "drop":
            df.dropna(axis=0, inplace=True)
            return df
        else:
            print("No imputation performed.")
            return df