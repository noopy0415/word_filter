import word_filter

my_filter = word_filter.WordFilter("アーセナル")

print(my_filter.detect("昨日のアーセナルの試合アツかった!"))

print(my_filter.detect("昨日のリバプールの試合アツかった!"))
