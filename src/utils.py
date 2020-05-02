import os
import functools
import pandas as pd


def execute_or_load_csv(func):
    @functools.wraps(func)
    def wrapper(*args, path=None, overwrite=True, **kwargs):
        if path is None:
            res = func(*args, **kwargs)
            res.to_csv(path, index=False)
            return res
        if not os.path.exists(path) or overwrite:
            res = func(*args, **kwargs)
            res.to_csv(path, index=False)
            return res
        else:
            res = pd.read_csv(path)
            return res
    return wrapper

