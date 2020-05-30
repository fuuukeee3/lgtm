import requests
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self.path = path

    def get_image(self):
        return open(self._path, "rb")


class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        return BytesIO(data.content)


class _LoremFlicker(RemoteImage):
    LOREM_FLIKR_URL = "https://loremflickr.com"
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        print(f"{self.LOREM_FLIKR_URL}/{self.WIDTH}/{self.HEIGHT}/{keyword}")
        return f"{self.LOREM_FLIKR_URL}/{self.WIDTH}/{self.HEIGHT}/{keyword}"


KeywordImage = _LoremFlicker


def ImageSource(keyword):
    """最適なイメージソースクラスを返す"""
    if keyword.startswith(("http://", "https://")):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return ImageSource(keyword).get_image()
