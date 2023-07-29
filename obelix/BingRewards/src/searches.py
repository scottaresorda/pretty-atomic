import contextlib
import json
import random
import time
from datetime import date, timedelta

import requests
from selenium.common.exceptions import (
    NoAlertPresentException,
    UnexpectedAlertPresentException,
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from .constants import DESKTOP_USER_AGENT
from .utils import Utils


class Searches:
    def __init__(self, browser: WebDriver, lang: str, geo: str):
        self.browser = browser
        self.utils = Utils(browser)
        self.lang = lang
        self.geo = geo

    def getGoogleTrends(self, wordsCount: int) -> list:
        searchTerms: list[str] = []
        i = 0
        while len(searchTerms) < wordsCount:
            i += 1
            r = requests.get(
                f'https://trends.google.com/trends/api/dailytrends?hl={self.lang}&ed={(date.today() - timedelta(days=i)).strftime("%Y%m%d")}&geo={self.geo}&ns=15'
            )
            trends = json.loads(r.text[6:])
            for topic in trends["default"]["trendingSearchesDays"][0][
                "trendingSearches"
            ]:
                searchTerms.append(topic["title"]["query"].lower())
                searchTerms.extend(
                    relatedTopic["query"].lower()
                    for relatedTopic in topic["relatedQueries"]
                )
            searchTerms = list(set(searchTerms))
        del searchTerms[wordsCount : (len(searchTerms) + 1)]
        return searchTerms

    def getRelatedTerms(self, word: str) -> list:
        try:
            r = requests.get(
                f"https://api.bing.com/osjson.aspx?query={word}",
                headers={"User-agent": DESKTOP_USER_AGENT},
            )
            return r.json()[1]
        except Exception:  # pylint: disable=broad-except
            return []

    def bingSearches(
        self, numberOfSearches: int, isMobile: bool = False, pointsCounter: int = 0
    ):
        i = 0
        search_terms = self.getGoogleTrends(numberOfSearches)
        for word in search_terms:
            i += 1
            print("[BING]", f"{i}/{numberOfSearches}")
            points = self.bingSearch(word, isMobile)
            if points <= pointsCounter:
                relatedTerms = self.getRelatedTerms(word)[:2]
                for term in relatedTerms:
                    points = self.bingSearch(term, isMobile)
                    if not points <= pointsCounter:
                        break
            if points > 0:
                pointsCounter = points
            else:
                break
        return pointsCounter

    def bingSearch(self, word: str, isMobile: bool):
        self.browser.get("https://bing.com")
        self.utils.waitUntilClickable(By.ID, "sb_form_q")
        searchbar = self.browser.find_element(By.ID, "sb_form_q")
        searchbar.send_keys(word)
        searchbar.submit()
        time.sleep(random.randint(10, 15))
        stringPoints = None
        with contextlib.suppress(Exception):
            if not isMobile:
                stringPoints = self.browser.find_element(By.ID, "id_rc").get_attribute(
                    "innerHTML"
                )

            else:
                try:
                    self.browser.find_element(By.ID, "mHamburger").click()
                    time.sleep(1)
                except UnexpectedAlertPresentException:
                    with contextlib.suppress(NoAlertPresentException):
                        self.browser.switch_to.alert.accept()
                        self.browser.find_element(By.ID, "mHamburger").click()
                stringPoints = self.browser.find_element(
                    By.ID, "fly_id_rc"
                ).get_attribute("innerHTML")

        return int(stringPoints) if stringPoints is not None else 0
