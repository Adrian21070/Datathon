import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def pca(df: pd.DataFrame, ncomp: int = 2) -> pd.DataFrame:
    
    cols = df.corr(numeric_only=True).columns
    dfs = df[cols]

    scaler = StandardScaler()
    dfs = scaler.fit_transform(dfs.dropna(axis=0))

    pca = PCA(n_components=ncomp)
    X = pca.fit_transform(dfs)

    names = ["PC" + str(x) for x in range(1, ncomp+1)]

    return pd.DataFrame(X, columns=names)