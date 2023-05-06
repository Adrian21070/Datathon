import numpy as np
import pandas as pd
import scipy.stats as stats

def power_transform(df: pd.DataFrame, how: str = None, columns: list = None) -> pd.DataFrame:
    
    if not columns:
        columns = df.select_dtypes(include="number").columns.to_list()
    else:
        pass

    match how:
        case "log":
            for column in columns:
                if df[column].min() <= 0:
                    print(column, "- values must be greater than 0")
                    continue
                else:
                    df[column] = np.log(df[column])
            return df
        case "boxcox":
            for column in columns:
                if df[column].min() <= 0:
                    print(column, "- values must be greater than 0")
                    continue
                else:
                    boxcox, lmbda = stats.boxcox(df[column])
                    df[column] = boxcox
            return df
        case _:
            print("No transformation performed.")
            return df