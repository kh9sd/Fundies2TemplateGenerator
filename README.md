# Fundies2TemplateGenerator
Generates template comments for the Northeastern Fundies 2 Java course

**THIS IS NOT A FULLY AUTOMATED PROCESS**, though with some work it
could approach it

## Setup
Have a working version of Python 3 on your computer. Download this code
above by clicking the green "Code" button and downloading the zip.

## Current input data setup
After you unpack the zip folder, in the folder create a text file named
`inputfile.txt`

The program needs to be able to read the class structures in your Java file.
It's way beyond my ability to actually parse the Java file, but Eclipse can actually 
provide a decent summary of it that we can use. 

Open `Window -> Show View -> Outline`
from the options at the top. Then, click the top class you want to start with, scroll
till you find the one you wan to stop at, and shift click it. Then, right-click and 
click `Copy qualified name`. Paste this into the `inputfile.txt`

Here, you need to manually input data. Notice for some reason the copy-paste
doesn't copy over method return types or class field types.

TODO


## Running the program
TODO

## Things to look out for
Hopefully you already have a natural mistrust of the program that compels
you to verify each template produced (so not my fault if something is off
and you lose points).

It should work for what we have learned so far, but Fundies will probably
introduce more features of Java that might work weirdly with the script.
From there the program will be in uncharted/broken territory.
And no promises on whether I or anybody will patch this stuff in, 
this isn't exactly a full time job.

Effectively, these are things that we MIGHT use in the future that ths script
cannot handle correctly. Else, we be chilling in this regard. As a rule of thumb
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
you can.




### Limitations/Improvements to be made
- obviously the way we input data, needing to add return types and such
manually is lame
  - if a solution is found, we would likely need to change the parser,
  but the classes for JavaData should not need changing
- cannot account for private classes/methods
  - technically unknown if we will actually use this in Fundies 2
  - aka, if a method is technically private and unable to be called 
  from a field, this program doesn't account for that and may need 
  the user to check manually to make sure invalid calls don't appear
  in the template
  - this is largely a constraint by the input data, which doesn't
  tell us anything about public/private. a solution here would probably
  require patching up the JavaClass class as well
- side effects would be pretty much impossible to format for
  - it would require being able to look at the actual source code,
  and effectively tracing calls and variables
  - (honestly would not be surprised if this was proved mathematically
  impossible even)
  
