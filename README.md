# Memorize Math Constants
I decided that just PI was not enough. I added expandability and a few more constants.

These constants are *e*, *phi*, *sqrt2*, *sqrt3*, and *sqrt5*.

I also removed the API from the PI part, and replaced it with a file like the rest. 1 million digits each shouldn't be too bad. I mean *I* could never memorize 1 *trillion* digits.

`check_shifted_match` still has the same *changeable* variables.
- `window`: *The amount of digits it will check if you added/skipped some*
- `match_level`: *How many digits you want to be correct in a row to determine a(n) added/skipped group*
- `extra_digs`: *How many digits you want to add to the end to give a preview to help memorize more*<br>

There is another one, but don't try to change it, as it is needed to let the function know which constant you are trying to memorize.
- `const`: *The constant that is being memorized*<br>

It includes some files, of course, that have the first 1 million digits of each, but I will include a **much** smaller file for each, consisting of 200 digits, which is still *way* more than the average person will ever need.
