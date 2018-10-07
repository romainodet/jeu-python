"""
                 /
    |      /  |////:  o////  ./////    s`      y////-
    |         |       /      s-    s.  h`      h
    |         |////.  /      s-    s-  h`      d////`
    |         |       /      s-    s.  h`      h
    |////     |////:  o/::/  -o/::/o   y////.  d////-

        -mmmmm.   ymmmmmmmmmy-   ymmmm-       -ymmmmmmmo
        -mmmmm.   ymmmm+ohmmmm-  ymmmm-     :mmmmdo/+s+
        -mmmmm.   ymmm     hmmmo ymmmm-    hmmmm:
        -mmmmm:   hmmm     mmmm/ ymmmm/    ymmmmy:
        -mmmmmmmmmmmmmmmmmmmms   ymmmmmmmm  dommmmmmmmo
        -hhhhhhhhhhhhhhhhys+/    shhhhhhhhy  ./shddhh/
        
        
     file :ascii_art_library.py
     By: romain.odet <romain.odet@lecole-ldlc.com>           
     Created: 07/10/2018 19:02 by Romain ODET  
"""


def ascii_art_hangman(num):
    if num == 0:
        ascii_output = "Well done, you don't have make mistakes."
    elif num == 1:
        ascii_output = """
                    1st try...
==================================="""
    elif num == 2:
        ascii_output = """
          /  \\
         //  \\\\     2d try...
==================================="""
    elif num == 3:
        ascii_output = """
           ||
           ||
           ||
           ||
           ||
           ||
          /||\\
         //||\\\\     3rd try...
==================================="""
    elif num == 4:
        ascii_output = """
           ||  /
           || /
           ||/
           ||
           ||
           ||
          /||\\
         //||\\\\     4th try...
==================================="""
    elif num == 5:
        ascii_output = """
           ,==============
           ||  /
           || /
           ||/
           ||
           ||
           ||
          /||\\
         //||\\\\     5th try...
==================================="""
    elif num == 6:
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/
           ||
           ||
           ||
          /||\\
         //||\\\\     6th try...
==================================="""
    elif num == 7:
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/        O
           ||         |
           ||         |
           ||
          /||\\
         //||\\\\     7th try...
==================================="""
    elif num == 8:
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/        O
           ||        /|\\
           ||         |
           ||
          /||\\
         //||\\\\     8th try...
==================================="""
    elif num == 9:
        ascii_output = """
           ,==========Y===
           ||  /      |
           || /       |
           ||/        O
           ||        /|\\
           ||        /|\\
           ||
          /||\\
         //||\\\\     9th try and the last...
==================================="""
    elif num == 10:
        ascii_output = """
                     _
                    | |
 _   _  ___  _   _  | | ___   ___  ___  ___
| | | |/ _ \| | | | | |/ _ \ / _ \/ __|/ _ \\
| |_| | (_) | |_| | | | (_) | (_) \__ \  __/_ _ _
 \__, |\___/ \__,_| |_|\___/ \___/|___/\___(_|_|_)
  __/ |
 |___/
           ,==========Y===
           ||  /      |
           || /       |
           ||/
           ||
           ||
           ||
          /||\ 
         //||\\\\    o-|-<
==================================="""
    else:
        exit(404)
    cr = """
    
    """
    return (cr + ascii_output + cr)
