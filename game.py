from spider import Spider
from itertools import filterfalse
import concurrent.futures


class Game():
    def __init__(self, all_text):
        self.all_text = all_text

    def start(self):
        """
        开始
        """
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futureArr = []
            for item in self.all_text:
                spider = Spider(item)
                r = executor.submit(spider.get_idioms)
                futureArr.append(r)
            resultArr = []
            for future in concurrent.futures.as_completed(futureArr):
                resultArr.append(future.result())

            result = self.filter(resultArr)
            return result

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
