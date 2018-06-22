import pytest

# package import for test
from python_template.sub_package.methods import returns_true


# test if returns_true returns true
def test_returns_true():
  expect = True
  actual = returns_true()
  assert expect == actual
