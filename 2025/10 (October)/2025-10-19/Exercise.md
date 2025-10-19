# HTML Attribute Extractor

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-19

Given a string of a valid HTML element, return the attributes of the element using the following criteria:

- You will only be given one element.
- Attributes will be in the format: `attribute="value"`.
- Return an array of strings with each attribute property and value, separated by a comma, in this format: `["attribute1, value1", "attribute2, value2"]`.
- Return attributes in the order they are given.
- If no attributes are found, return an empty array.

## Tests

1. `extract_attributes('<span class="red"></span>')` should return `["class, red"]`.
1. `extract_attributes('<meta charset="UTF-8" />')` should return `["charset, UTF-8"]`.
1. `extract_attributes("<p>Lorem ipsum dolor sit amet</p>")` should return `[]`.
1. `extract_attributes('<input name="email" type="email" required="true" />')` should return `["name, email", "type, email", "required, true"]`.
1. `extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>')` should return `["id, submit", "class, btn btn-primary"]`.
