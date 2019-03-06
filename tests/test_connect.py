import pytest
from netcli.connect import ConnectThread

# pylint: disable=protected-access


@pytest.mark.parametrize("command,arg,expected", [
    ("aaa bbb [ccc (ddd)]", ("ddd", "None"), "aaa bbb"),
    ("aaa bbb [(ccc) ddd]", ("ccc", "None"), "aaa bbb"),
    ("aaa bbb [ccc (ddd)]", ("ddd", "111"), "aaa bbb ccc 111"),
    ("aaa bbb [(ccc) ddd]", ("ccc", "111"), "aaa bbb 111 ddd"),
    ("aaa bbb [(ccc) ddd] eee", ("ccc", "111"), "aaa bbb 111 ddd eee"),
])
def test_get_command_argument(command, arg, expected):
    command = ConnectThread._get_command_argument(command, arg[0], arg[1])
    assert command == expected
