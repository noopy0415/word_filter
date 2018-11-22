import word_filter

my_filter = word_filter.WordFilter("アーセナル", "リバプル")

print(my_filter.detect("昨日のアーセナルの試合アツかった!"))

print(my_filter.detect("昨日のリバプールの試合アツかった!"))

# print(my_filter.censor("昨日のアーセナルの試合アツかった！"))

# print(my_filter.censor("昨日のリバプールの試合アツかった！"))

print(my_filter.replace("昨日のアーセナルの試合アツかった！"))

print(my_filter.replace("昨日のリバプールの試合アツかった！"))
