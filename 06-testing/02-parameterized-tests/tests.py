import pytest
from parentheses import *

@pytest.mark.parametrize("string", [
    '()',
    '(())'
    '()()'
    '(()())'
])
def test_parentheses_correct(string):
    assert matching_parentheses(string)


@pytest.mark.parametrize('string', [
    '(',
    ')',
    '(()',
    '(()()',
    '(((()()))))'
])
def test_parentheses_incorrect(string):
    assert not matching_parentheses(string)