import pytest

from typedflow.batch import Batch
from typedflow.tasks import Dumper

from typedflow.tests.tasks.base import Arg


class PrintableArg(Arg):
    def __str__(self):
        return f'{self.string} {str(self.int_value)}'


@pytest.fixture
def dumper():

    def func(batch):
        for arg in batch.data:
            print(str(arg))

    dumper = Dumper(func=func)
    return dumper


def test_print_dump(dumper, capsys):
    data = [PrintableArg('hi', i) for i in range(3)]
    batch = Batch(data=data, batch_id=1)
    dumper.dump(batch)
    out, _ = capsys.readouterr()
    assert out == ('\n'.join([str(a) for a in data]) + '\n')