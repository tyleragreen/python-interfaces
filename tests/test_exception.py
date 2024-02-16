import pytest

from interface import interface, InterfaceException


class Iterable:
    def do_loop(self):
        pass


def test_raises_exception():
    with pytest.raises(InterfaceException) as e:

        @interface(Iterable)
        class BusList:
            def other_method(self):
                return "not the method"

    assert "Missing interface methods" in str(e.value)
