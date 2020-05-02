import requests


class URLTransformer(object):
    def __init__(self, raw_url):
        self.raw_url = raw_url
        self.base_url = "https://link.springer.com/"

    def transform(self):
        response = requests.get(self.raw_url)
        extracted_url = response.url
        book = extracted_url.split('/')[-1]
        url_download = f"{self.base_url}/content/pdf/{book}.pdf"
        return url_download
