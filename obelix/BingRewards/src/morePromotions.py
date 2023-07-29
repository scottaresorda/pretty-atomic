from selenium.webdriver.chrome.webdriver import WebDriver

from .activities import Activities
from .utils import Utils


class MorePromotions:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.utils = Utils(browser)
        self.activities = Activities(browser)

    def completeMorePromotions(self):
        morePromotions = self.utils.getDashboardData()["morePromotions"]
        i = 0
        for promotion in morePromotions:
            try:
                i += 1
                if (
                    promotion["complete"] is False
                    and promotion["pointProgressMax"] != 0
                ):
                    self.activities.openMorePromotionsActivity(i)
                    if promotion["promotionType"] == "urlreward":
                        self.activities.completeSearch()
                    elif (
                        promotion["promotionType"] == "quiz"
                        and promotion["pointProgress"] == 0
                    ):
                        if promotion["pointProgressMax"] == 10:
                            self.activities.completeABC()
                        elif promotion["pointProgressMax"] in [30, 40]:
                            self.activities.completeQuiz()
                        elif promotion["pointProgressMax"] == 50:
                            self.activities.completeThisOrThat()
                    else:
                        self.activities.completeSearch()
            except Exception:  # pylint: disable=broad-except
                self.utils.resetTabs()
