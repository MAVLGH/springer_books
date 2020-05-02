from src.transformations.url_transformation import URLTransformer
from src.utils import execute_or_load_csv


class DataFrameTransformation(object):
    def __init__(self, df):
        self.df = df

    def _generate_book_name(self):
        titles = []
        for el in self.df['title'].values.tolist():
            el = el.replace(' ', '_')
            el = el.replace('/', '_')
            titles.append(el)
        self.df.loc[:, 'book_name'] = titles

    def _transform_url(self):
        for i, raw_url in enumerate(self.df['url']):
            print(i, raw_url)
            url_transformer_obj = URLTransformer(raw_url)
            url_download = url_transformer_obj.transform()
            self.df.loc[i, 'download_url'] = url_download

    @execute_or_load_csv
    def get(self):
        self._generate_book_name()
        self._transform_url()
        return self.df
