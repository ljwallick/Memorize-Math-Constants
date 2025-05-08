# Memorize Math Constants
I decided that just PI was not enough. I added expandability and a few more constants.

These constants are *e*, *phi*, *sqrt2*, *sqrt3*, and *sqrt5*.

I also removed the API from the PI part, and replaced it with a file like the rest. 1 million digits each shouldn't be too bad. I mean *I* could never memorize 1 *trillion* digits. (Edit: Due to terminal limitations, the bigger file size is now 16,400)

`check_shifted_match` still has the same *changeable* variables.
- `window`: *The amount of digits it will check if you added/skipped some*
- `match_level`: *How many digits you want to be correct in a row to determine a(n) added/skipped group*
- `extra_digs`: *How many digits you want to add to the end to give a preview to help memorize more*<br>

There is another one, but don't try to change it, as it is needed to let the function know which constant you are trying to memorize.
- `const`: *The constant that is being memorized*<br>

It includes some files that have the first 16,400 digits of each (changed from 1mil), but I also included a **much** smaller file for each, consisting of 200 digits, which is still *way* more than the average person will ever need. What it will do is use the file in *hundreds* folder, but if you use over 200 digits, then it will switch to the *cappped* version automatically. This will help with... idk. I don't think it will do anything better.

I learned during testing that the terminal has a max input length (because I decided to try to paste the entire *million* file into the terminal like the smartie I am :D ). This magical number seems to be 16,381. How specific. I edited the *million* files to be *capped*, and now have 16,400 digits. The current *recognized* world record for recited digits is 70,000 long. Due to limitations, Rajveer Meena will not get to use this tool to his fullest extent. I do not want to make a multiline input workaround (bc 99.¯9% of you will never reach the cap), so it will do as of now.
