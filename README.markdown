Pyff Exercise
=============

Since every participant has a different background and therefore a different
skill set regarding programming and Python, we tried to design the exercises in
a way that everyone can benefit.

The first exercise does not require any Python or programming skills at all,
the second one involves some Python programming and the third one requires
Python and Pygame knowledge.

Please pick one or more exercises to solve.


1. Get Familiar with Pyff
-------------------------

In this exercise you don't have to program at all. Just start Pyff and get
familiar with the GUI. Start some Feedbacks get them to run, inspect variables,
play with the filter and try to modify some variables.


2. Relax Feedback
-----------------

For some experiments it is necessary to get the subject relaxed. We often use
the so called *Relax Feedback*, a Feedback that resembles the classic *Mystify*
screen saver ([Mystify Screensaver on YouToube][Mystify]).

The Relax Feedback consists of a Polygon with a fixed number of vertices. Each
vertex has it's own speed vector and moves along the direction until it hit's
the border of the screen where it is reflected. The polygon defined by the
vertices is also filled with a color which changes over time.

In the materials you'll find a directory `Relax` where a working yet incomplete
Relax Feedback is implemented. Your task is to modify the `update_polygon`
method in a way that the polygon moves and changes its color.

Please remember that the subject is supposed to relax, so try to avoid
aggressive movements and color changes!

Please note that you have to start the Feedback Controller with the `-a`
parameter pointing to the Relax directory!

[Mystify]: http://youtu.be/p-howMhFecQ


3. Brain Pong
-------------

Some of you might remember the classic game Pong, where two opponents play a
ball back and forth until one of the opponents misses the ball ([Pong on
YouTube][Pong]).

Your task is to implement a *Brain Pong* where one subject plays Pong using BCI
against a Computer. The subject uses left- and right hand imagination to
control the paddle and plays against the computer which should keep the subject
motivated by letting him win from time to time...

You can use the `Pong` provided in the materials directory as a starting point
and modify it or you can start from scratch if you prefer.



[Pong]: http://youtu.be/pDrRnJOCKZc
[Pygame]: http://pygame.org
