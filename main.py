from AI import AI
from Game import Game
from Player import Player


def main():
    #  Instiantiate the Game, Player, and AI objects.
    game = Game(3)
    player = Player()
    ai = AI()

    #  Prompt the user for who goes first.
    first = player.prompt_start()

    #  Run the game loop.
    game.loop(
        first=first, 
        player=player, 
        ai=ai,
        )
if __name__ == '__main__':
    main()



