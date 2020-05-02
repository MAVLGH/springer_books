import os
import shutil
import requests


class API(object):
    def __init__(self, path_out, verbose=False):
        self.base_url = "https://link.springer.com/"
        self.path_out = path_out
        self.verbose = verbose

    @staticmethod
    def _download_pdf(url, local_filename, chunk_size=8192, test_chunk=False):
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        if test_chunk:
                            break
        return local_filename

    def save_files(self, df, column_url, column_book_name, overwrite=False, test=False, chunk_size=8192):
        url_list = df[column_url].values.tolist()
        book_names_list = df[column_book_name].values.tolist()
        self._save_files(url_list, book_names_list, test, overwrite, chunk_size)

    def _save_files(self, url_list, book_names_list, test, overwrite, chunk_size):
        for url, book_name in zip(url_list, book_names_list):
            test_ = "[TEST]_" if test else ""
            path_out = f"{self.path_out}/{test_}{book_name}.pdf"
            path_tmp = f"{self.path_out}/temp/{test_}{book_name}.pdf"
            download_check = not os.path.exists(path_out) or overwrite
            if self.verbose:
                state = 'getting' if download_check else 'already exists'
                print(f"{state} | {book_name}")
            if download_check:
                _ = self._download_pdf(url, path_tmp, test_chunk=test, chunk_size=chunk_size)
                shutil.move(path_tmp, path_out)

