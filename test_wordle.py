from wordle import *

def test_check_word():
    assert check_word("OPENS", 'EPICS') == ["yellow", "green", "grey", "grey", "green"]
    assert check_word("MISTS", "MISTY") == ["green", "green", "green", "green", "grey"]
    assert check_word("LERED", "DRUID") == ["grey", "yellow", "grey", "grey", "green"]
    assert check_word("ELUDE", "LEDGE") == ["yellow", "yellow", "yellow", "grey", "green"]
    assert check_word("CRANE", "BEEPS") == ["grey", "yellow", "grey", "grey", "grey"]
    assert check_word("ROBOT", "REORG") == ["green", "grey", "yellow", "grey", "grey"]

def test_check_w():
    assert check_word("OPENS", 'EPICS') == ["yellow", "green", "grey", "grey", "green"]
    assert check_word("MISTS", "MISTY") == ["green", "green", "green", "green", "grey"]
    assert check_word("LERED", "DRUID") == ["grey", "yellow", "grey", "grey", "green"]
    assert check_word("ELUDE", "LEDGE") == ["yellow", "yellow", "yellow", "grey", "green"]
    assert check_word("CRANE", "BEEPS") == ["grey", "yellow", "grey", "grey", "grey"]
    assert check_word("ROBOT", "REORG") == ["green", "grey", "yellow", "grey", "grey"]