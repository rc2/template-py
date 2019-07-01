Feature: Addition

Scenario Outline: Add two numbers
  Given x = <x> and y = <y>
  When x and y are added together
  Then The result should equal <z>
  Examples:
  | x | y | z |
  | 0 | 1 | 1 |
  | 1 | 0 | 1 |
  | 1 | 1 | 2 |
  | 1 | 2 | 3 |
  | 2 | 3 | 5 |
  | 3 | 5 | 8 |
