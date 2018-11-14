from ..interface import interface


class Iterable:
    def do_loop(self):
        pass


@interface(Iterable)
class BusList:
    def be_iterable(self):
        return 'I\'m a bus.'

    def do_loop(self):
        return 'got it!'


def test_create():
    bl = BusList()
    assert bl.be_iterable() == 'I\'m a bus.'
    assert bl.do_loop() == 'got it!'

# # TODO make this better
# print('type', type(bl))
# # <class '__main__.interface.__call__.<locals>.NewKlass'>
# print('BusList?', isinstance(bl, BusList))
# # True
# print('Iterable?', isinstance(bl, Iterable))
# # False
