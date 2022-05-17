from typing import Union
import os
import requests
import appdirs
from bs4 import BeautifulSoup


class Api:
    """helper class to manage the downloads of all the advent of code inputs
    """

    def __init__(self, sessionid: str) -> None:
        """init function

        Args:
            sessionid (str): the session id for your AOC account
            debugmode (bool, optional): debugmode. Defaults to True.
        """

        self.cachedir = appdirs.user_cache_dir("python-adventutils")
        self.sessionid = sessionid
        self.cookies = {'session': self.sessionid}

    def get_data(self, year: int, day: int) -> Union[str, int]:
        """downloads the data to the cache directory and returns it

        Args:
            day (int): the day you want to download
            year (int): which year you want to download from

        Returns:
            Union[str, int]: returns a 0 if an error has occured else returns a string
        """

        # checks if the day is within the correct bounds
        if 0 >= day > 31:

            print("invalid day")
            return 0

        # checks if the year is withing the correct lower bound
        if year <= 2015:
            print("invalid year")
            return 0

        # creating the cache directory if it doesn't exist
        if not os.path.exists(self.cachedir):
            print("directory ", self.cachedir, " doesnt exist")
            print("creating directory")
            os.mkdir(self.cachedir)

        # if the cached file doesnt already exist download it
        if not os.path.exists(os.path.join(self.cachedir, str(year)+str(day))):
            print("downloading data")
            resq = requests.get(
                "https://adventofcode.com/{0}/day/{1}/input".format(year, day),
                cookies=self.cookies)

            if not resq.ok:
                print("error", resq.status_code, "raised")
                return 0

            with open(os.path.join(self.cachedir, str(year)+str(day)), "w") as fp:
                fp.write(resq.text)
                fp.close()

        # return the contents of the cached file
        with open(os.path.join(self.cachedir, str(year)+str(day)), "r") as fp:
            return fp.read()

    def submit(self, year: int, day: int, level: int, answer: str) -> int:
        """submit an answer for the advent of code

        Args:
            year (int): the year 
            day (int): the day
            level (int): the level
            answer (str): the answer

        Returns:
            int: a status code #! to be added
        """
        resq = requests.post(
            f"https://adventofcode.com/{year}/day/{day}/answer",
            cookies=self.cookies,
            data={"level": str(level), "answer": str(answer)})

        parsed = BeautifulSoup(resq.text, "html.parser")
        message = parsed.article.text.lower()
        answerstat = message.split(";")[0]

        print(answerstat)

# TODO: add more logging and use the error codes from the requests
