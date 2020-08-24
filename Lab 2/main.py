from gamemodel import *
from gamegraphics import *

def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()
    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1/50)
        update(50)
    return gproj

def getInput(graphicgame):
    player = graphicgame.getCurrentPlayer()
    oldAngle, oldVel = player.getAim()

    if player == graphicgame.getPlayers()[1]:
        oldVel = -oldVel
        oldAngle = -oldAngle

    print(player.getColor() + ' players turn!')
    print('The wind is howling at a good {0:.1f} speed'.format(graphicgame.getCurrentWind()))
    print('Previous angle was {0:.1f}, enter new angle'.format(oldAngle))

    box = InputDialog(, 30, graphicgame.getCurrentWind())
    box.interact()
    newAngle, newVel = box.getValues()
    box.close()

    return newAngle, newVel

def graphFinishShot(game, proj):
    # The current player
    player = game.getCurrentPlayer()
    # The player opposing the current player
    other = game.getOtherPlayer()

    # Check if we won
    distance = other.projectileDistance(proj) 
    if distance == 0.0:
        print('Direct hit! ' + player.getColor() + ' player wins the round!')
        player.increaseScore()
        print('the current score is ' + player.getColor()+':' + str(player.getScore()) + ', ' + other.getColor() + ':' + str(other.getScore()))
        # Start a new round
        game.newRound()
    else:
        print('missed by a distance of {0:.1f}'.format(distance))

    # Switch active player
    game.nextPlayer()

def graphicPlay():

    game = Game(10,3)
    ggame = GraphicGame(game)
    while True:
        angle, vel = getInput(ggame)
        gproj = graphicFire(ggame, angle, vel)
        graphFinishShot(ggame, gproj)




# Run the game with graphical interface
graphicPlay()
