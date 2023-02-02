# Codewars style ranking system

Task - Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.

CodeWars - [Kata](https://www.codewars.com/kata/51fda2d95d6efda45e00004e)

## Example

``` python
User user = new User();
user.rank; # => -8
user.progress; # => 0
user.incProgress(-7);
user.progress; # => 10
user.incProgress(-5); # will add 90 progress
user.progress; # => 0 // progress is now zero
user.rank; # => -7 // rank was upgraded to -7
```
