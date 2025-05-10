# Memorize Math Constants
I decided that just PI was not enough. I added expandability and a few more constants.

These constants are *e*, *phi*, *sqrt2*, *sqrt3*, and *sqrt5*.

I also removed the API from the PI part, and replaced it with a file like the rest. 1 million digits each shouldn't be too bad. I mean *I* could never memorize 1 *trillion* digits. 

Edit: Due to terminal limitations, the bigger file size is now 16,400

Edit 2: The limitations are from VSCode, not the terminal. I will not change the files though, because who will memorize that much anyway.

`main` has some customizable variables. These are:
- `window`: *Number of digits to look ahead when checking for matches.*
- `match_level`: *Number of digits that need to match in a row.*
- `extra_digs`: *Number of digits to add after finished checking for matches.*
- `limit`: *Maximum number of digits to read.* <br>

It includes some files that have the first 16,400 digits of each (changed from 1mil), but I also included a **much** smaller file for each, consisting of 200 digits, which is still *way* more than the average person will ever need. What it will do is use the file in *hundreds* folder, but if you use over 200 digits, then it will switch to the *cappped* version automatically. This will help with... idk. I don't think it will do anything better.

This program lets you customize your experience as much as I could think of. I am sure proud of the ideas I had, I hope you all appreciate the customizability as well. It shows distinctly what digits that you skipped, added, etc. If you choose a start point, then it will highlight all the digits before your starting point in green, as to not be confused. I also mad it to where it automatically prints the constant(eg. `3.` for Pi) that matches the number you want to memorize. This just made things way simpler to program tbh, and it doesn't hurt anything. If you start more than 20 digits after the decimal, it will elipse most of the digits (`3.14159...9793238462<start typing>643383...`) as to not cover the screen with extraneous numbers. This program is a mix of practical and lenient, and I love it. I am sure to memorize more and more of every famous constant out there.

This program is also very expandable. If there is a constant you want to add, just get some of the digits in a text file and add it to the dictionary at the top of `main()`. There is so much you can do with this to expand and learn, and I wouldn't want anything less. Have fun!!!
