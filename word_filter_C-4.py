class WordFilter(object):

    def __init__(self, ng_word="アーセナル", replace_word="<censored>"):
        self.replace_word = {ng_word: replace_word}

    def detect(self, word):
        for ng_word in self.replace_word:
            if ng_word in word: return True
        return False

    def censor(self, word):
        for ng_word in self.replace_word:
            word = word.replace(ng_word, "<censored>")
        return word

    def replace(self, word):
        for ng_word in self.replace_word:
            word = word.replace(ng_word, self.replace_word[ng_word])
        return word

    def ng_word_add(self, ng_word, replace_word):
        if not (ng_word in self.replace_word):
            self.replace_word.update({ng_word: replace_word})


if __name__ == "__main__":
    my_filter = WordFilter()
    print(my_filter.detect("昨日のアーセナルの試合アツかった!"))  # True
    print(my_filter.detect("昨日のリバプールの試合アツかった!"))  # False

    print(my_filter.censor("昨日のアーセナルの試合アツかった！"))  # 昨日の<censored>の試合アツかった！
    print(my_filter.censor("昨日のリバプールの試合アツかった！"))  # 昨日のリバプールの試合アツかった！

    ng_word = input("NGワードを入力してください > ")  # アツ
    replace_word = input("変換する文字を入力してください > ")  # 寒
    my_filter.ng_word_add(ng_word, replace_word)
    print(my_filter.replace("昨日のアーセナルの試合アツかった！"))  # 昨日の<censored>の試合寒かった！
    print(my_filter.replace("昨日のリバプールの試合アツかった！"))  # 昨日のリバプールの試合寒かった！
