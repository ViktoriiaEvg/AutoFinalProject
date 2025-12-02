class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    """ Method for getting current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current Url " + get_url)

    """ Method for text assertion"""

    def assert_text(self, text, result):
        value_text= text.text
        assert value_text == result
        print("Text is expected")


    "Method for asserting URL"
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("The URL is correct")

