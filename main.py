import os

from src.transformations.file_transformation import TransformSpringerPDF
from src.transformations.df_transformation import DataFrameTransformation
from src.api.API import API

script_path = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
transform_springer_pdf_obj = TransformSpringerPDF(path_in=f'{script_path}/data/Springer.pdf')
df = transform_springer_pdf_obj.transform(path=f'{script_path}/data/springer_table.csv', overwrite=False)
df_transformation_obj = DataFrameTransformation(df)
df = df_transformation_obj.get(path=f'{script_path}/data/springer_table_transformed.csv', overwrite=False)
api = API(path_out=f'{script_path}/books/', verbose=True)
api.save_files(df,
               column_url='download_url',
               column_book_name='book_name',
               overwrite=False,
               chunk_size=2**17,
               test=False
               )
