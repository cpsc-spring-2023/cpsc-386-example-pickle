#!/usr/bin/env python3

from game.player import BlackJackPlayer
from random import randint
import os
import os.path
import pickle
import locale


def main():
    names = "Kai Madison Riley Jayden Harper Noah Sara".split()
    num_players = 0
    main_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(main_dir, "data")
    pickle_file = os.path.join(data_dir, "players.pkl")
    locale.setlocale(locale.LC_ALL, "en_US")
    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as fh:
            players = pickle.load(fh)
        num_players = len(players)
    else:
        while num_players > len(names) or num_players < 1:
            num_players = int(input("How many players? "))
            if num_players > len(names) or num_players < 1:
                print(f"Please select a number between 1 and {len(names)}")

        print(f"Let's make {num_players} players...")
        players = [BlackJackPlayer(i + 1, names[i]) for i in range(num_players)]
    print("We made the following players:")
    for player in players:
        print(f"{player} has {player.bankroll}")
    print("Let's change each player's balance by deducting a random amount of money...")
    for player in players:
        player.bet = randint(100, 1000)
        print(f"{player} has wagered {player.bet}.")
        player.deduct_bet()
        print(f"{player} has lost {player.bet} and now has {player.bankroll}.")
    print("Let's save the players to a file...")
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    with open(pickle_file, "wb") as fh:
        pickle.dump(players, fh, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
