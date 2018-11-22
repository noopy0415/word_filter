class WordFilter(object):
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, word):
        return self.ng_word in word

    def censor(self, word):
        return word.replace(self.ng_word, "<censored>")


if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")

    my_filter.detect("昨日のアーセナルの試合アツかった!")

    my_filter.detect("昨日のリバプールの試合アツかった!")

    my_filter.censor("昨日のアーセナルの試合アツかった！")

    my_filter.censor("昨日のリバプールの試合アツかった！")
