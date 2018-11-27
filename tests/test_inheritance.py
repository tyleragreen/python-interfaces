import pytest

from interface import interface


class Iterable:
    def do_loop(self):
        pass


class AbstractList:
    def another_method(self):
        return 'not much here'


class VehicleList(AbstractList):
    def another_method(self):
        return 'vehicles are cool'


@interface(Iterable)
class BusList(VehicleList):
    def do_loop(self):
        return 'looping bus'

    def another_method(self):
        return 'especially buses'


def test_type_respects_inheritance():
    bl = BusList()
    assert type(bl) == BusList
    assert type(bl) != Iterable
    assert type(bl) != VehicleList


def test_issubclass_respects_inheritance():
    assert issubclass(VehicleList, AbstractList)
    assert issubclass(BusList, VehicleList)


def test_isinstance_respects_inheritance():
    vl = VehicleList()
    assert isinstance(vl, VehicleList)
    assert isinstance(vl, AbstractList)

    bl = BusList()
    assert isinstance(bl, BusList)
    # TODO these two should be true
    assert isinstance(bl, VehicleList)
    assert isinstance(bl, AbstractList)
    assert not isinstance(bl, Iterable)
