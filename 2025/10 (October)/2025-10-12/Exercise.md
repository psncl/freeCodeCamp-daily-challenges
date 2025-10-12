# Battle of Words

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-12

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

- The given sentences will always contain the same number of words.
- Words are separated by a single space and will only contain letters.
- The value of each word is the sum of its letters.
- Letters `a` to `z` correspond to the values `1` through `26`. For example, `a` is `1`, and `z` is `26`.
- A capital letter doubles the value of the letter. For example, `A` is `2`, and `Z` is `52`.
- Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
- A word wins if its value is greater than the opposing word's value.
- The team with more winning words is the winner.

Return `"We win"` if your team is the winner, `"We lose"` if your team loses, and `"Draw"` if both teams have the same number of wins.

## Tests

1. `battle("We must never surrender", "Our team must win")` should return `"Draw"`.
1. `battle("hello world", "hello word")` should return `"We win"`.
1. `battle("Hello world", "hello world")` should return `"We win"`.
1. `battle("lorem ipsum", "kitty ipsum")` should return `"We lose"`.
1. `battle("hello world", "world hello")` should return `"Draw"`.
1. `battle("git checkout", "git switch")` should return `"We win"`.
1. `battle("Cheeseburger with fries", "Cheeseburger with Fries")` should return `"We lose"`.
