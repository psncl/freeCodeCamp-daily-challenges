# Extension Extractor

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-10

Given a string representing a filename, return the extension of the file.

- The extension is the part of the filename that comes after the last period (`.`).
- If the filename does not contain a period or ends with a period, return `"none"`.
- The extension should be returned as-is, preserving case.

## Tests

1. `get_extension("document.txt")` should return `"txt"`.
1. `get_extension("README")` should return `"none"`.
1. `get_extension("image.PNG")` should return `"PNG"`.
1. `get_extension(".gitignore")` should return `"gitignore"`.
1. `get_extension("archive.tar.gz")` should return `"gz"`.
1. `get_extension("final.draft.")` should return `"none"`.
