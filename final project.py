file_contents = '“Do you not want to know who has taken it?” cried his wife impatiently.“You want to tell me, and I have no objection to hearing it.”This was invitation enough.“Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it, that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week.”“What is his name?”“Bingley.”'
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my"]
new = ""
for chars in file_contents:
    if chars == ".":
        new += " "
    if chars.isalpha() or chars == " ":
        new += chars
word_dicti = {}
for word in new.split(" "):
    if word.lower() in uninteresting_words:
        continue
    else:
        if word.lower() not in word_dicti:
            word_dicti[word.lower()] = new.count(word.lower())

print(new)
print(word_dicti)
