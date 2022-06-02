from unittest import main, TestCase
from main import word_1, word_2, word_3, lista

def palavras():
    x = lista
    return x

class TestPalavra(TestCase):

    def palavra(self):
        result = word_1
        expected = True

        self.assert(result, expected)

    if __name__ == '__main__':
        main()
