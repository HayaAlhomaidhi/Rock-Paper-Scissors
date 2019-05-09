#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random
moves = ['rock', 'paper', 'scissors']
enemys = ['random', 'reflect', 'rocker', 'cycle' ]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)
        self.score = 0
        
    def move(self):
        return 'rock'
    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            print("Your move is...:")
            m = input().lower()
            if m in moves:
                return m
                print("Make sure you enter(rock/paper/scissors)!")


class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))


class ReflectPlayer(Player):
    def move(self):
        k = self.their_move
        if k is None:
            return random.choice(moves)
        else:
            return k

    def learn(self, my_move=None, their_move=None, n=None):
        self.my_move = my_move
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'Player 1 :{move1} , Player 2 : {move2}')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        r = beats(move1, move2)
        if r:
            self.p1.score += 1
            print ('Player 1 win this round')
        elif r is False:
            self.p2.score += 1
            print ('Player 2 win this round')
        else:
            print('No one win')

    def play_game(self):
        print("Game start!, let's see who is the winner!!")

        while True:
            try:
                self.round_no = int(input("Enter the number of rounds:"))
                break
            except ValueError:
                print("You can enter a number only!")

        for round in range(self.round_no):
            print("**************")
            print(f'Round {round+1} :')
            self.play_round()
            print(f'score of Player 1 = {self.p1.score}')
            print(f'score of Player 2 = {self.p2.score}')
        print("********************************************")
        print("Final Result")
        print(f'score of Player 1 = {self.p1.score}')
        print(f'score of Player 2 = {self.p2.score}')
        if self.p1.score > self.p2.score:
            print("Player 1 WINS")
        elif self.p1.score < self.p2.score:
            print("Player 2 WINS")
        else:
            print("Scores are equal, it's a tie!")
        print("Game over")


while True : 
    enemy = input("You want to play against...? * random, reflect, rocker, cycle *").lower()
    if enemy in enemys :  
        break

    if enemy == "random" :
        game = game(HumanPlayer), RandomPlayer()
    elif enemy == "reflect" :
        game = game(HumanPlayer), ReflectPlayer()
    elif enemy == "rocker" :
        game = game(HumanPlayer), Player()
    else: 
        game = game(HumanPlayer), CyclePlayer()
game.play_game()
