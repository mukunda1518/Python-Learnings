class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = sentence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


my_sentence = Sentence("This is a test")
for word in my_sentence:
    print(word)


# generator

def sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence1 = sentence("This is a test")

for word in my_sentence1:
    print(word)
