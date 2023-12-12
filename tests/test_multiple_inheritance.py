from interface import interface


class Iterable:
    def do_loop(self):
        pass


class VehicleList:
    def another_method(self) -> str:
        return 'vehicles are cool'


class PublicTransportVehicle:
    def __init__(self):
        pass


@interface(Iterable)
class BusList(PublicTransportVehicle, VehicleList):
    def do_loop(self):
        return 'looping bus'

    def another_method(self) -> str:
        return 'especially buses'


def test_type_respects_inheritance():
    bl = BusList()
    assert type(bl) is BusList
    assert type(bl) is not Iterable
    assert type(bl) is not VehicleList
    assert type(bl) is not PublicTransportVehicle


def test_issubclass_respects_inheritance():
    assert issubclass(BusList, VehicleList)
    assert issubclass(BusList, PublicTransportVehicle)


def test_isinstance_respects_inheritance():
    bl = BusList()
    assert isinstance(bl, BusList)
    assert isinstance(bl, VehicleList)
    assert isinstance(bl, PublicTransportVehicle)
    assert not isinstance(bl, Iterable)
