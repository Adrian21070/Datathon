import numpy as np
import pandas as pd
from typing import Union

def remove_outliers(data: Union[pd.DataFrame, pd.Series, np.ndarray], iqr_factor: Union[float, int] = 1.5) -> Union[pd.DataFrame, pd.Series, np.ndarray]:
    
    if isinstance(data, pd.DataFrame):
        return rm_outliers_df(data, iqr_factor)
    
    elif isinstance(data, pd.Series):
        return rm_outliers_series(data, iqr_factor)

    elif isinstance(data, np.ndarray):
        return rm_outliers_np(data, iqr_factor)


def rm_outliers_df(df: pd.DataFrame, iqr_factor: Union[float, int]) -> pd.DataFrame:
    columns = df.select_dtypes(include="number").columns.to_list()
    for column in columns:
        print(column)
        print(df.shape)
        q3, q1 = np.percentile(df.loc[:,column].dropna(), [75 ,25])
        iqr = q3 - q1
        low = q1 - iqr*iqr_factor
        high =  q3 + iqr*iqr_factor
        df = df[(df[column] < high) & (df[column] > low)]
    return df


def rm_outliers_series(series: pd.Series, iqr_factor: Union[float, int]) -> pd.Series:
    q3, q1 = np.percentile(series.dropna(), [75 ,25])
    iqr = q3 - q1
    low = q1 - iqr*iqr_factor
    high =  q3 + iqr*iqr_factor
    series = series[(series < high) & (series > low)]
    return series


def rm_outliers_np(array: np.ndarray, iqr_factor: Union[float, int]) -> np.ndarray:
    
    if array.ndim < 2 or array.shape[1] < 2:
        array = array.flatten()
        try:
            array = array[~np.isnan(array)]
        except:
            print("Only numeric ndarrays are supported for outlier removal.")
            return array
        q3, q1 = np.percentile(array, [75 ,25])
        iqr = q3 - q1
        low = q1 - iqr*iqr_factor
        high =  q3 + iqr*iqr_factor
        return array[(array < high) & (array > low)]
    
    else:
        for column_n in range(array.shape[1]):
            try:
                column = array[:, column_n]
                column = column.astype("float64")
            except:
                print("Only numeric ndarrays are supported for outlier removal.")
                continue

            if np.issubdtype(column.dtype, np.floating) or np.issubdtype(column.dtype, np.integer):
                q3, q1 = np.percentile(column[~np.isnan(column)], [75 ,25])
                iqr = q3 - q1
                low = q1 - iqr*iqr_factor
                high =  q3 + iqr*iqr_factor
                array = array[(column < high) & (column > low)]
            else:
                continue
        return array
    

# # Testing 
# def main():
#     df = pd.read_csv("https://raw.githubusercontent.com/crisb-7/TitanicML/main/datasets/titanic_train.csv")
#     df = remove_outliers(data=df[["Name", "Fare"]].dropna().to_numpy(), iqr_factor=1.5)

# if __name__ == "__main__":
#     main()