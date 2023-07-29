from interface import interface


class Iterable:
    def do_loop(self):
        pass


@interface(Iterable)
class BusList:
    def normal_method(self):
        return 'bus here'

    def do_loop(self):
        return 'got it!'


class CarList:
    def normal_method(self):
        return 'car here'


def test_can_create_object_which_respects_interface():
    bl = BusList()
    assert bl.normal_method() == 'bus here'
    assert bl.do_loop() == 'got it!'


def test_isintance_of_correct_class():
    bl = BusList()
    assert isinstance(bl, BusList) is True
    assert isinstance(bl, Iterable) is False
    assert isinstance(bl, CarList) is False


def test_assert_type_correct():
    bl = BusList()
    assert type(bl) is BusList
    assert type(bl) is not Iterable
    assert type(bl) is not CarList
