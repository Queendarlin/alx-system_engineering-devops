# Oniguruma Regular Expression Project

## Overview

This project involves building a Ruby script using Oniguruma regular expressions.
Regular expressions (regex or regexp) are powerful sequences of characters that define a search pattern. They are widely used in various programming languages and text processing tools to match, search, and manipulate strings based on specific patterns.
In this project, we leverage the Oniguruma regular expression library within Ruby.

## Basics
### Literal Characters
Example: abc
Description: Matches the literal characters 'a', 'b', and 'c' in sequence.
### Character Classes
Example: [0-9]
Description: Matches any single digit from 0 to 9.
### Quantifiers
Example: a{2,4}
Description: Matches 'a' repeated 2 to 4 times.
### Anchors
Example: ^start
Description: Matches 'start' only at the beginning of a line.
### Escaping Special Characters
Example: \d
Description: Escapes the 'd' character, matching any digit.
## Advanced Concepts
### Grouping and Capturing
Example: (abc)
Description: Groups the characters 'abc' and captures the match for later use.
### Alternation
Example: cat|dog
Description: Matches either 'cat' or 'dog'.
### Lookahead and Lookbehind
Example: (?<=@)\w+
Description: Matches a word that is preceded by the '@' symbol.
### Non-Capturing Groups
Example: (?:abc)
Description: Groups the characters 'abc' without capturing the match.

## Tools
Rubular
Rubular is an interactive web-based tool for testing Ruby regular expressions. It allows you to input a regex pattern and test it against various strings.

## Conclusion
Mastering regular expressions is a valuable skill for text processing and pattern matching. The Oniguruma library, integrated with Ruby, provides a robust platform for building and testing regex patterns. Use the provided script in this project as a starting point to explore and apply regular expressions in your Ruby projects.
