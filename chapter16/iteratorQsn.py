
# Question on iterator problem of iterating through the sentence using the class

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.word = self.sentence.split() # by default delimiter is space 

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.word[index]

my_sentence = Sentence("This is a Test")

''' general way to iterate through the sentence using the class
 for word in my_sentence:
    print(word)
'''
# Manual iteration
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))

# if we call next() again it will raise StopIteration exception because there is no more word to iterate through the sentence
print(next(my_sentence))


