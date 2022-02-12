# Fundies2TemplateGenerator
Generates template comments for the Northeastern Fundies 2 Java course

**THIS IS NOT A FULLY AUTOMATED PROCESS**, though with some work it
could approach it

## Setup
Have a working version of Python 3 on your computer. 
Download this code above by clicking the green "Code" button and selecting the zip option. Extract
the files. The two files you have to concern yourself with are `Main.py` and `inputfile.txt`

## Current input data setup
The program needs to be able to get the class structures in your Java file.
It's beyond my ability to actually parse the Java file, but Eclipse can actually 
provide a decent summary of it that we can use, which is the Outline view

Open `Window -> Show View -> Outline`
from the options at the top. Then, click the top class you want to start with, scroll
till you find the one you wan to stop at, and shift click it. Then, right-click and 
click `Copy qualified name`. Paste this into the `inputfile.txt`

Here, you **need to manually input data**. Notice for some reason the copy-paste
doesn't copy over method return types or class field types. Basically 
Eclipse hates us, and this is the only real work you need to do each time to get
this program prepped to run. *If someone could find a way around this part, that would be swell.*

So, after each field/method, add ONE space and write out the type. You should be copying
the Eclipse Outline for this, so it's pretty braindead if you just keep it visible in the background
to view it.

Also, to support inheritance, if one of your classes EXTENDS another clas, write the parent class
next to the class name
- I do mean ONLY if you use the "extend" keyword in your code. If you use the keyword "implement" you don't
have to do anything

**For this program to return correctly, you need to make sure**
- The first line of your text file MUST be a class name
- Methods and fields must be followed by a single space, and a single type

Constructors will be automatically ignored, so don't write anything after them to save yourself
both time and possible headaches if something breaks from an edge case

## Running the program
After you've prepped the input file, right click the `Main.py` and click `Edit with IDLE`. You can run 
it on the Terminal, but I find copy pastign to be easier this way. At the top then click `Run` -> `Run module`.
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

If all you want is know how to run the program, then we're done here.
However, if by chance you want to actually contribute some code/improvements,
please do.



### Limitations/Improvements to be made
- obviously the way we input data, needing to add return types and such
manually is lame
  - if a solution is found, we would likely need to change the parser,
  but the classes for JavaData should not need changing

- cannot account for private classes/methods
  - aka, if a method is technically private and unable to be called 
  from a field, this program doesn't account for that and may need 
  the user to check manually to make sure invalid calls don't appear
  in the template
  - this is largely a constraint by the input data, which doesn't
  tell us anything about public/private. a solution here would probably
  require patching up the JavaClass class as well
  
- side effects would be pretty much impossible to detect let alone format for
  - it would require being able to look at the actual source code,
  and effectively tracing calls and variables
    - aka, basically running the Java file
  
