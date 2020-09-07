from math import sin,cos,radians
import random

#TODO: Deal with all TODOs in this file and also remove the TODO and HINT comments.

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        p1 = Player("blue", -90, 0, self)
        p2 = Player("red", 90, 1, self)
        self.players = [p1,p2]
        self.currentPlayer = 0
        self.otherPlayer = 1
        randwind = random.randint(-10,10)
        self.wind = randwind
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
        return self.players[self.currentPlayer]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.players[self.otherPlayer]
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.currentPlayer
    
    """ Switch active player """
    def nextPlayer(self):
        tmp_player = self.currentPlayer
        self.currentPlayer = self.otherPlayer
        self.otherPlayer = tmp_player

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
    def __init__(self, col, pos, numb, game):
        self.color = col
        self.position = pos
        self.playerNumber = numb
        self.Game = game
        self.score = 0
        self.angle = 0
        self.velocity = 0


    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        if self == self.Game.getPlayers()[1]:
            velocity = -velocity
            angle = -angle

        
        self.angle = angle
        self.velocity = velocity
        
        projectile = Projectile(angle, velocity, self.Game.getCurrentWind(), self.getX(), self.Game.getCannonSize()/2, -110, 110)
        return projectile 

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        cannonMid = self.getX()
        cannonMaxMin = self.Game.getCannonSize()/2

        cannonMin = cannonMid - cannonMaxMin
        cannonMax = cannonMid + cannonMaxMin

        projMid = proj.getX()
        projMaxMin = self.Game.getBallSize()

        projMin = projMid - projMaxMin
        projMax = projMid + projMaxMin

        if projMin > cannonMax:
            return projMin - cannonMax
        elif projMax < cannonMin:
            return projMax - cannonMin
        else:
            return 0

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
