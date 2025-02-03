# WDR Paper Computer Game Night


## Introduction
The WDR paper computer or Know-how Computer is an educational model of a computer consisting only of a pen, a sheet of paper, and individual matches.

For my 30th birthday, I organized a game night with the WDR paper computer. The goal was to have fun and to learn something about the basics of CPUs and assembly programming. The audience was a mix of tech-savvy and non-tech-savvy people. The game night was a great success, and I would like to share the materials and the experience with you.


## Game Night Concept
I used a presentation to introduce the WDR paper computer and the WDR instruction set. I recommend you to prepare a similar presentation to introduce the WDR paper computer to your friends with the information preesented in the next section, [WDR Paper Computer](#wdr-paper-computer).

I divided my friends into teams of two. Each team received a WDR paper computer kit consisting of a pencil, a sheet of paper, and individual matches. The teams had to draw the WDR paper computer and then solve a series of challenges by writing the WDR assembly code on the left side of the sheet of paper.

I didn't awarded points to the teams (but you can if you want!). Instead, for each challenge I praised the teams that solved the challenge first and the teams that solved the challenge with the fewest lines of code.

A simple WDR implementation in Python is available in the repository, `wdr.py`. You can use it to test the challenges before the game night and to test the solutions of the teams in real-time.


## WDR Paper Computer
The WDR paper computer is a simple model of a computer consisting only of a pencil, a sheet of paper, and individual matches. A WDR Computer can have between 2 and 8 general-purpose registers `R0, R1, ..., R7` and a program counter. 

The WDR instruction set consists of 5 instructions:
- `inc <register>`: increment the value of the given register by 1
- `dec <register>`: decrement the value of the given register by 1
- `jmp <line>`: jump to the given line
- `isz <register>`: if the value of the given register is zero, skip the next line
- `stp`: stop the program

The pencil acts as a program counter and is used to indicate the line of code which is about to be executed. The user steps through the program, adding and subtracting matches from the appropriate registers and following program flow until the `stp` instruction is encountered.

Decreasing a register below zero is not allowed. If a register is decremented when its value is zero, the program crashes.


## Challenges
I proposed 4 challenges:
1. Countdown
2. Addition
3. Subtraction
4. Even or Odd

The challenges are available in the `challenges` folder. Each challenge is a markdown file with the description of the challenge and the solution.


## Additional Resources
- [WDR Paper Computer](https://en.wikipedia.org/wiki/WDR_paper_computer) - Wikipedia
- [Paper Computer](https://wiki.xxiivv.com/site/paper_computer.html) - Devine Lu Linvega website
- [Youtube video](https://www.youtube.com/watch?v=Z27KQiBnkJI) by Chris Staecker
- [know-how-computer](https://github.com/poelstra/know-how-computer) - a similar repository with a Gleam implementation
