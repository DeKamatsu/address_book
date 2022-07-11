import pytest

from contact import Contact

# def contact_creation(a, b, expected):
#     cont = Contact(a)
#     assert cont == expected
#
# def test_output(capsys):
#     print_some_message_func()
#     assert capsys.readouterr().out == """\
#     some
#     multi-line
#     message
#     """
#
# @pytest.mark.parametrize(
#     "n, expected", (
#             (1, True),
#             (2, True),
#             (3, False),
#             (4, True),
#             (5, False),
#             (8, True),
#             (256, True),
#     )
# )
# def test_check_number(n, expected):
#     assert check_number(n) is expected


data = [
    ["Иван", "Иванов", +3205-25-38, "Примечание", ],
    ["Ив", "Петров", 32357938, 1564, ],
    ["Сема", "", '32 (05) 25 19', ''],
    ["", "Степанов", '+32 (05) 25-38', "-", ],
    ("", "Женин", '+32 (05) 25-38', "", ),
]
for d in data:
    ab.add(contact.Contact(d))

ab.show_all()

ab.add("Serg", "Sergeev", 123, "")
ab.add()
ab.add()
ab.add()
ab.add()
ab.delete(1)
ab.delete("Denis")
ab.show("Mila")
ab.modify("2")
ab.delete("1")
ab.show_all()

