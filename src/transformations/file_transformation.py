from tabula import read_pdf
import pandas as pd

from src.utils import execute_or_load_csv


class TransformSpringerPDF(object):
    def __init__(self, path_in):
        self.path_in = path_in

    @execute_or_load_csv
    def transform(self):
        df_list = read_pdf(self.path_in, pages='all')
        columns = ['n', 'title', 'author', 'edition', 'url']
        df_final = pd.DataFrame()
        for i, df in enumerate(df_list):
            cols_ = [[el] for el in df.columns.tolist()]
            df.columns = columns
            df = df[df['url'].str.contains('http', na=False)]
            df_row = pd.DataFrame(dict(zip(columns, cols_)))
            if df_row['url'].str.contains('http', na=False).values.tolist()[0]:
                df = df.append(df_row)
            df_final = pd.concat([df_final, df], ignore_index=True)
        df_final = df_final.drop('n', 1)
        for col in ['title', 'author', 'edition']:
            df_final[col] = df_final[col].replace({r'\r': ''}, regex=True)
        return df_final
