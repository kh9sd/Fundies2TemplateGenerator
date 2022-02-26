# Fundies2TemplateGenerator
Generates template comments for the Northeastern Fundies 2 Java course

## Setup
Have a working version of Python 3 on your computer. 
Download this code above by clicking the green "Code" button and selecting the zip option. Extract
the files. The only files you have to concern yourself with is `Main.py`

## Running the program
Right click the `Main.py` and click `Edit with IDLE`. You can run 
it on the Terminal, but I find copy-pasting to be easier this way. At the top then click `Run` -> `Run module`.

The program will now ask for a path to the Java file you want a template for. On Windows, you should navigate to your
Java file in the folder, shift right-click it, and hit "Copy as path". Now paste this in the Python program, it should
look something like `"C:\Users\ SOME BLAH BLAH BLAH... .java"`. Before you hit enter, remove the quote marks around
the path, so now you should have something like `C:\Users\... .java` entered. Now hit enter and let it run.

If you're on a different platform, I don't know how to get a file path, search it up. But otherwise same thing
should apply, paste and remove the quote marks around the path, then enter.

You should see some confirmation text that the program has read you file.


Now, you have a few choices. If you want a template for a class, type `c` like said and follow the instructions.
If you are creating a template for a complex data method parameter, type `p` and follow through.

Afterwards just paste the block of text that the program spat out into the appropriate place in your Java program,
comment it out with `Ctrl-/`, and indent as necessary.

## Things to look out for
Hopefully you have a natural mistrust of this program that compels
you to verify each template produced (so don't try to displace the blame if
it spits out a wrong template that you didn't check, losing you points during grading).

It should work for what we have learned so far as of HW 3, but Fundies will probably
introduce more features of Java that might work weirdly with the script.
From there the program will be in uncharted/broken territory.
And no promises on whether I or anybody will patch this stuff in, 
this isn't exactly a full time job.

Effectively, these are things that we MIGHT use in the future that ths script
cannot handle correctly right now. As a rule of thumb
if you don't know what these things listed below are, you don't have to worry 
about it.

1. private things
   1. aka, if a method is technically private and unable to be called 
  from a field, this program doesn't account for that and may need 
  the user to check manually to make sure invalid calls don't appear
  in the template
2. static things
   1. they're weird, and the professors might require us to note them
   in templates in a different way
3. methods with side-effects
   1. if the professors require that you note side-effects in the template,
   this will 100% REQUIRE you to check it manually, pretty much no chance
   of this being automated by the program


