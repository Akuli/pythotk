from pythotk.font import NamedFont, AnonymousFont


def test_get_properties():
    font = AnonymousFont(
        family="Helvetica",
        weight="bold",
        overstrike=True,
        underline=False,
        size=42,
        slant="roman",
    )

    assert font.family == "Helvetica"
    assert font.weight == "bold"
    assert font.overstrike is True
    assert font.underline is False
    assert font.size == 42
    assert font.slant == "roman"


def test_set_properties():
    NAME = "set_properties_test"

    font1 = NamedFont(
        name=NAME,
        family="Helvetica",
        weight="bold",
        overstrike=True,
        underline=False,
        size=42,
        slant="roman",
    )
    font2 = NamedFont(name=NAME)

    assert font1 is not font2

    assert font1.name == font2.name
    assert font1.overstrike is True
    assert font2.overstrike is True

    font1.overstrike = False
    assert font1.overstrike is False
    assert font2.overstrike is False


def test_deletion():
    NAME = "deletion_test"

    font = NamedFont(name=NAME)

    assert NAME in NamedFont.names()
    font.delete()
    assert NAME not in NamedFont.names()


def test_actual_is_valid_init_args():
    prime_font = AnonymousFont(
        family="Helvetica", weight="bold", overstrike=True
    )
    clone_font = AnonymousFont(**prime_font.actual())

    assert clone_font.actual() == prime_font.actual()


def test_named_to_tcl():
    NAME = "to_tcl_test"

    font = NamedFont(
        name=NAME,
        family="Calibri",
        weight="bold",
        slant="italic",
        size=37,
        overstrike=True,
        underline=True,
    )

    assert font.to_tcl() == font.name


def test_anonymous_to_tcl():
    font = AnonymousFont.from_tcl(
        "-family Calibri "
        "-weight bold "
        "-slant italic "
        "-size 37 "
        "-overstrike 1 "
        "-underline 0"
    )

    assert font.family == "Calibri"
    assert font.weight == "bold"
    assert font.slant == "italic"
    assert font.size == 37
    assert font.overstrike is True
    assert font.underline is False


def test_named_from_tcl():
    font = NamedFont(
        name="from_tcl_test",
        family="Calibri",
        weight="bold",
        slant="italic",
        size=37,
        overstrike=True,
        underline=True,
    )
    assert NamedFont.from_tcl(font.name) == font


def test_anonymous_from_tcl():
    font = AnonymousFont.from_tcl("Helvetica 7 bold underline")
    assert font.family == "Helvetica"
    assert font.size == 7
    assert font.weight == "bold"
    assert font.underline is True

    font = AnonymousFont.from_tcl("-family Times -size 3 -overstrike 1")
    assert font.family == "Times"
    assert font.size == 3
    assert font.overstrike is True
