from math import sin,cos,radians
import random

#TODO: Deal with all TODOs in this file and also remove the TODO and HINT comments.

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        p1 = Player("blue", -90, 0, self, 0)
        p2 = Player("red", 90, 1, self, 0)
        self.players = [p1,p2]
        self.currentPlayer = p1
        self.otherPlayer = p2
        self.currentPlayerNumber = 0
        self.wind = 0
        self.cannonsize = cannonSize
        self.ballsize = ballSize

    """ A list containing both players """
    def getPlayers(self):
        return self.players 

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannonsize

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ballsize

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.currentPlayer

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.otherPlayer
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.currentPlayerNumber
    
    """ Switch active player """
    def nextPlayer(self):
        if self.currentPlayerNumber == 0:
            self.currentPlayerNumber = 1
            self.currentPlayer = self.players[1]
            self.otherPlayer = self.players[0]
        else:
            self.currentPlayerNumber = 0
            self.currentPlayer = self.players[0]
            self.otherPlayer = self.players[1]

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.wind = wind

    def getCurrentWind(self):
        return self.wind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        randwind = random.randint(-10,10)
        self.wind = randwind
        

""" Models a player """
class Player:
    def __init__(self, col, pos, numb, game, score):
        self.color = col
        self.position = pos
        self.playerNumber = numb
        self.Game = game
        self.score = score

    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        if self == self.Game.getPlayers()[1] :
            velocity = -velocity
            angle = -angle

        
        self.angle = angle
        self.velocity = velocity
        projectile = Projectile(angle, velocity, self.Game.getCurrentWind(), self.getX(), self.Game.getCannonSize()/2, -110, 110)
        return projectile 

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        mid_cannon = self.getX()
        cannonDiff = self.Game.getCannonSize()/2

        cannon_Pos = [mid_cannon - cannonDiff, mid_cannon + cannonDiff]

        mid_proj = proj.getX()
        projDiff = self.Game.getBallSize()

        proj_Pos = [mid_proj - projDiff, mid_proj + projDiff]

        if proj_Pos[0] > cannon_Pos[1]:
            return proj_Pos[0] - cannon_Pos[1]
        elif proj_Pos[1] < cannon_Pos[0]:
            return proj_Pos[1] - cannon_Pos[0]
        else:
            return 0

        
        '''
        cann_left = self.getX() - self.Game.getCannonSize()
        cann_right = self.getX() + self.Game.getCannonSize()

        proj_left = proj.getX() - self.Game.getBallSize()
        proj_right = proj.getX() + self.Game.getBallSize()

        
        if cann_left > proj_right:
            dist = proj_right - cann_left
        elif cann_right < proj_left:
            dist = proj_left - cann_right
        else:
            dist = 0
        '''


    """ The current score of this player """
    def getScore(self):
        return self.score

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self.score += 1

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.position

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.angle, self.velocity 



""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
