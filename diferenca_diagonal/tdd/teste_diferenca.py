from unittest import main, TestCase
from main import m, d, D, a, b


def matriz():
    x = m
    return x


class TestDiag(TestCase):

    def test_dif_dig(self):
        assert abs(b - a) == abs(sum(d) - sum(D))

        self.assertEqual(abs(b - a), abs(sum(d) - sum(D)))

    if __name__ == '__main__':
        main()

    def test_tam_mat(self):
        result = len(m)
        expected = 3

        self.assertEqual(result, expected)

    if __name__ == '__main__':
        main()

    def test_soma_dif(self):
        assert a == b

        self.assertEqual(a, b)

    if __name__ == '__main__':
        main()
