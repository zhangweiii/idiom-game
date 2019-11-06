from spider import Spider
from itertools import filterfalse


class Game():
    def __init__(self, all_text):
        self.all_text = all_text

    def start(self):
        """
        开始
        """
        idiomsArr = []
        for item in self.all_text:
            spider = Spider(item)
            idiomsArr.append(spider.get_idioms())

        print(self.filter(idiomsArr))

    def filter(self, idioms):
        exitIdiom = []
        for arr in idioms:
            for item in arr:
                flag = True
                for ch in item:
                    if ch not in self.all_text:
                        flag = False
                        break
                if flag and item not in exitIdiom and item != '':
                    exitIdiom.append(item)

        return exitIdiom
