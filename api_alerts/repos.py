"""Groups repositories in the same place. New repos can be made to
hit the same source differently, or use a new source altogether"""
from abc import abstractmethod
import requests


class Repo():
    """This is meant to function as an interface for checks to use.
    Checks shouldn't be aware of individual repo implementation"""

    @abstractmethod
    def get_data(self):
        """Logic for gathering data should be filled in by each separate
        repo implementation"""


class PublicApiRepo(Repo):
    """Simple Repository for Gemini's public REST API"""

    def get_data(self, ticker):
        base_url = "https://api.gemini.com/v2"
        response = requests.get(base_url + f'/ticker/{ticker}')
        return response
