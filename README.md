# Jeu Solitaire Solver

Three engineers played a cooperative game of solitaire one evening.
There was a playboard with place for up to 37 balls. To begin with
3x3 balls are missing in the middle. The goal is to remove all
balls but one.

Each move one ball must jump over another ball. The ball jumped
over is removed from the board. Only vertical and horizontal
moves are allowed, and only one, single ball can be jumped over
and removed in one turn.

We failed to come up with a solution better than two remaining
balls. So later that weekend I set down to write this script
that should solve it for us.

Turns out *there is no solution* with less than 2 remaining balls!

But if the initial playboard is just slightly modified by for example
adding one extra ball (but not in the center) a solution with 1
remaining ball can be found.

This git contains both a C and a Python version. The C version
is of course a lot quicker to handle each step in the game, but
the Python version has an optimization that make the algorithm
skip early on board states that have already been tested. This
consumes a lot of memory (~9 GB), but solves the problem in less
than 10 minutes on my MacBook Pro.
