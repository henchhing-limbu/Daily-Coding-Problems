"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds
Example:
1s -> f(8)
2s -> 
3s -> f(2)
4s -> f(4) 
5s -> Execute job f(2)
6s -> 
7s -> 
8s -> Execute job f(4)
9s -> Execute job f(8)
"""

# This is more of a design question.
# Can use timer and a background thread.
