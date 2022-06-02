from unittest import main, TestCase
from main import lista, soma_lista, menor_que_11


def array():
    x = lista
    return x


class TestSoma(TestCase):

    def test_tam_array(self):
        result = len(lista)
        expected = 10

        self.assertEqual(result, expected)

    if __name__ == '__main__':
        main()

    def test_soma_array(self):
        assert soma_lista == sum(lista)

        self.assertEqual(soma_lista, sum(lista))

    if __name__ == '__main__':
        main()

    def test_num_array(self):
        result = menor_que_11
        self.assertTrue(result)


    if __name__ == '__main__':
        main()

