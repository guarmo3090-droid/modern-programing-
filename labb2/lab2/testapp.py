from app import get_greeting

def test_greeting():
    assert get_greeting("Alice") == "allah babah, Alice!"
    assert get_greeting("Bob") == "allah babah, Bob!"
    #.
