import os

from app.data.default import default_gifs, default_jokes, default_quotes
from random import randint, choice
import requests
from abc import ABC, abstractmethod
from dotenv import load_dotenv


class APIRequest(ABC):
    def __init__(self, url, params=None, headers=None):
        self.url = url

        if headers is not None:
            self.headers = headers
        else:
            self.headers = {'accept':'application/json'}

        if params is not None:
            self.params = params
        else:
            self.params = {}

    def __call__(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            print(e)

    @abstractmethod
    def unpack(self):
        pass


class QuoteAPI(APIRequest):
    def __init__(self, params=None, headers=None):
        super().__init__(params, headers)
        self.url = 'https://zenquotes.io/api/today'

    def unpack(self):
        try:
            response = self.__call__()
            clean_response = response.json()
            quote = clean_response[0]['q']
            author = clean_response[0]['a']
        except Exception as e:
            print('QuoteAPI: ', e)
            random_quote = choice(list(default_quotes))
            quote = random_quote['q']
            author = random_quote['a']
        return [quote, author]

class JokeAPI(APIRequest):
    def __init__(self, params=None, headers=None):
        super().__init__(params, headers)
        self.url = 'https://icanhazdadjoke.com/'

    def unpack(self):
        try:
            response = self.__call__()
            clean_response = response.json()
            joke = clean_response['joke']
        except Exception as e:
            print('JokeAPI: ', e)
            joke = choice(default_jokes)
        return joke


class MoodAPI(APIRequest):
    def __init__(self, mood, headers=None):
        load_dotenv()
        super().__init__(headers)
        self.url = "http://api.giphy.com/v1/gifs/search"
        self.params = {"q": mood,
            "api_key": os.getenv('GIPHY_API_KEY'),
            "limit": "1",
            "offset": randint(0, 300)}

    def unpack(self):
        try:
            response = self.__call__()
            clean_response = response.json()
            list = clean_response['data']
            item = list[0]
            gif_url_mp4 = item['images']['fixed_width']['mp4']
            gif_url_gif = item['images']['fixed_width']['url']
        except Exception as e:
            print('MoodAPI: ', e)
            mood = self.params['q']
            gif_url_mp4 = default_gifs[mood]
            gif_url_gif = default_gifs[f"{mood}_gif"]
        return [gif_url_mp4, gif_url_gif]


class MoodDict(object):

    def __init__(self):
        self.dict = {}
        self.list = ['happy', 'calm', 'sad', 'worried', 'frustrated', 'angry']

    def make_dict(self):
        for mood in self.list:
            link_tuple = MoodAPI(mood).unpack()
            self.dict[mood] = link_tuple[0]
            self.dict[f"{mood}_gif"] = link_tuple[1]
        return self.dict


