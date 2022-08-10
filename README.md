# Wordle Tool

This is a monte carlo simulation for the popular game Wordle. Based on my tests,
"clasp" is the best word to use, with slate having the highest positional letter
score, and alert having the highest total letter score. Included "ocean" as a
known control

python wordle.py
('clasp', {'L': 2, '1': 0, '3': 321, '2': 43, '5': 161, '4': 450, '6': 23})
('slate', {'L': 5, '1': 0, '3': 391, '2': 60, '5': 118, '4': 410, '6': 16})
('alert', {'L': 6, '1': 1, '3': 357, '2': 62, '5': 130, '4': 416, '6': 28})
('ocean', {'L': 17, '1': 0, '3': 287, '2': 45, '5': 181, '4': 419, '6': 51})
