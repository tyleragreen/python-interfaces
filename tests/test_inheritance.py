from interface import interface


class Iterable:
    def do_loop(self):
        pass


class AbstractList:
    def another_method(self) -> str:
        return 'not much here'


class VehicleList(AbstractList):
    def another_method(self) -> str:
        return 'vehicles are cool'


@interface(Iterable)
class BusList(VehicleList):
    def do_loop(self):
        return 'looping bus'

    def another_method(self) -> str:
        return 'especially buses'


def test_type_respects_inheritance():
    bl = BusList()
    assert type(bl) is BusList
    assert type(bl) is not Iterable
    assert type(bl) is not VehicleList


def test_issubclass_respects_inheritance():
    assert issubclass(VehicleList, AbstractList)
    assert issubclass(BusList, VehicleList)


def test_isinstance_respects_inheritance():
    vl = VehicleList()
    assert isinstance(vl, VehicleList)
    assert isinstance(vl, AbstractList)

    bl = BusList()
    assert isinstance(bl, BusList)
    assert isinstance(bl, VehicleList)
    assert isinstance(bl, AbstractList)
    assert not isinstance(bl, Iterable)
