# coding=utf-8
"""Addition feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from template_py.sub_package.methods import add

@scenario('features/addition.feature', 'Add two numbers')
def test_add_two_numbers():
    """Add two numbers."""


@given('x = <x> and y = <y>')
def x_and_y(x, y):
    """x = <x> and y = <y>."""
    return dict(
        x=int(x),
        y=int(y)
    )


@when('x and y are added together')
def x_and_y_are_added_together(x_and_y):
    """x and y are added together."""
    x_and_y['z'] = add(x_and_y['x'], x_and_y['y'])


@then('The result should equal <z>')
def the_result_should_equal_z(x_and_y, z):
    """The result should equal <z>."""
    assert(int(z) == x_and_y['z'])
