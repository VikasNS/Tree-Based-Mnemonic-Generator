from nltk import word_tokenize,sent_tokenize
import pandas as pd
import pickle
data = []
words_in_data = []
words_in_embedding = []
missing_words_in_data = []
to_delete = "./:;<=>?@[\]^_`{|}~#$%&'()*+,!“”’■—‘🙏�"
to_delete2 = '"\\'
to_replace = "-"


files = ['india-news-headlines.csv', 'headlines.csv']
for l, file in enumerate(files):
    print('Article')
    df = pd.read_csv(file)
    for z, paragraph in enumerate(df.headline_text):
        print(l, z)
        sentences = sent_tokenize(paragraph.lower())
        for sentence in sentences:
            sentence = sentence.strip()
            if (len(sentence) != 0):
                sentence = sentence.rstrip().strip().translate(str.maketrans('', '', to_delete)).translate(
                    str.maketrans('', '', '1234567890')).translate(str.maketrans('', '', to_delete2)).translate(
                    str.maketrans(to_replace, " "))
                words = word_tokenize(sentence)
                words_in_data += words

with open('set_all_words','wb') as output_file:
    pickle.dump(set(words_in_data), output_file)


