from code import hackernews


def test_clear() -> None:
    assert hackernews.clean("MOLLY") == "MOLLY"
    assert hackernews.clean("MOl-ly.") == "MOlly"
    assert hackernews.clean("M, O, L, L, Y") == "M O L L Y"
