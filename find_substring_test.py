from find_substring import *


def test_longest_common_subst_dp():

    result = longest_common_subst_dp("","")
    assert result == ""
    result = longest_common_subst_dp("","toto")
    assert result == ""
    result = longest_common_subst_dp("toto","")
    assert result == ""
    result = longest_common_subst_dp("matata","atmos")
    assert result == "at"
    result = longest_common_subst_dp("atmos", "matata",)
    assert result == "at"
    result = longest_common_subst_dp("fish", "wish",)
    assert result == "ish"
    result = longest_common_subst_dp("wish", "wish",)
    assert result == "wish"
    result = longest_common_subst_dp("fishbourne", "misha",)
    assert result == "ish"


