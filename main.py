from __future__ import division


import math
from game import Game
from treasure import Treasure
from player import Player
from randomNum import Random
import sys
rand= Random()
if len(sys.argv) > 1:
  rand.setSeed(int(sys.argv[1])) 





class Game:
    
    # the constructor (initialize all game variables)
    def __init__(self,gameBoardWidht,gameBoardHeight,numberofplayers):  
        self.gameBoardWidth = gameBoardWidht
        self.gameBoardHeight = gameBoardHeight
        self.numberofplayers = numberofplayers
        self.listOfPlayers = []
        self.listOfTreasures = []
        self.listOfWeapons = []

        number = 0
        for p in range(0,numberofplayers):
          number += 1
          
          w = rand.randrange(gameBoardWidht)
          h = rand.randrange(gameBoardHeight)
          
          self.listOfPlayers.append(Player(w,h,number))
      
        
        
        
        t1 = Treasure("silver","S",20, rand.randrange(gameBoardWidht), rand.randrange(gameBoardHeight))
        self.listOfTreasures.append(t1)
        t2 = Treasure("gold","G", 25,rand.randrange(gameBoardWidht) ,rand.randrange(gameBoardHeight) )
        self.listOfTreasures.append(t2)
        t3 = Treasure("platinum", "P", 50,rand.randrange(gameBoardWidht), rand.randrange(gameBoardHeight) )
        self.listOfTreasures.append(t3)
        t4 = Treasure("diamond", "D", 40,rand.randrange(gameBoardWidht), rand.randrange(gameBoardHeight) )
        self.listOfTreasures.append(t4)
        t5 = Treasure("emerald", "E", 35, rand.randrange(gameBoardWidht), rand.randrange(gameBoardHeight) )
        self.listOfTreasures.append(t5)

        w1 = Weapon("gun", rand.randrange(gameBoardWidht), rand.randrange(self.gameBoardHeight),"/", 7)
        self.listOfWeapons.append(w1)
        w2 = Weapon("grenade",rand.randrange(gameBoardWidht), rand.randrange(self.gameBoardHeight), "o", 4)
        self.listOfWeapons.append(w2)
        
       

    
    
    def play(self):
        self.printInstructions()
      
        self.drawUpdatedGameBoard()
    
    
        # MAIN GAME LOOP to ask players what they want to do
        currentPlayerNum = 0
        while (len(self.listOfTreasures) >= 1):
            
            # get the player object for the player whose turn it is
            currentPlayer = self.listOfPlayers[currentPlayerNum];
         
            
            choice = input("Player " + str(currentPlayer.gameBoardSymbol) + ", do you want to (m)ove or (r)est? ")
            self.processPlayerInput(currentPlayer, choice)
            
            if len(self.listOfPlayers) < 2:
              break
            
            # show the updated player information and game board
            self.printUpdatedPlayerInformation();
            self.drawUpdatedGameBoard()
            
            # update whose turn it is
            currentPlayerNum += 1
            if currentPlayerNum >= len(self.listOfPlayers):
                currentPlayerNum = 0
        
        loop = 0 
        highest = 0
        for i in self.listOfPlayers:
          if i.getPoints() > self.listOfPlayers[highest].getPoints():
            highest = loop
          loop += 1
        print("Player",str(self.listOfPlayers[highest].gameBoardSymbol) + " has " + str(self.listOfPlayers[highest].getPoints()) + " points and has " + str(self.listOfPlayers[highest].energy) + " energy")
        self.drawUpdatedGameBoard()
        print("Player", self.listOfPlayers[highest].gameBoardSymbol, "wins!")
 
        
        
    
    
    def processPlayerInput(self, plyr, action) :
        if action == "m":  # move
            direction = input("Which direction (r, l, u, or d)? ")
            distance = int(input("How Far? "))
            plyr.move(direction,distance)

            for player in self.listOfPlayers:
              if plyr != player:
               if plyr.x == player.x and plyr.y == player.y:
                self.listOfPlayers.remove(player)
                print("You eliminated player", player.gameBoardSymbol ,"from the game!")
            for weapon in self.listOfWeapons:
              if plyr.x == weapon.x and plyr.y == weapon.y:
                plyr.collectWeapon(weapon)
                print("You acquired the", weapon.name + "!")
                self.listOfWeapons.remove(weapon)
                  
              
                
            # check to see if player moved to the location of another game item
            for treasure in self.listOfTreasures:
                if plyr.x == treasure.x and plyr.y == treasure.y:
                    plyr.collectTreasure(treasure)
                    print("You collected",treasure.name,"worth",treasure.pointValue,"points!")
                    self.listOfTreasures.remove(treasure)  # remove the treasure from the list of available treasures
                    break
        elif action == "a":
          highest = 0
          loop = 0
          if len(plyr.collectedWeapons) == 0:
            return
          
          for weapon in plyr.collectedWeapons: 
             if weapon.strikedistance > plyr.collectedWeapons[highest].strikedistance:
              highest = loop
             loop += 1
          
          for players in self.listOfPlayers:
            if plyr != players:
              if ((plyr.x-players.x)**2 + (plyr.y-players.y)**2)**.5 <= plyr.collectedWeapons[highest].strikedistance:
                self.listOfPlayers.remove(players)
                print("You eliminated player",players.gameBoardSymbol,"from the game!")
              
         
        elif action == "r":
          plyr.energy += 4.0
        else :
            print("Sorry, that is not a valid choice")
    
    
    
    def printUpdatedPlayerInformation(self):
        for p in self.listOfPlayers:
            print("Player " + str(p.gameBoardSymbol) + " has " + str(p.getPoints()) + " points and has " + str(p.energy) + " energy")
      
    
    def drawUpdatedGameBoard(self) :     
        # loop through each game board space and either print the gameboard symbol
        # for what is located there or print a dot to represent nothing is there
        for y in range(0,self.gameBoardHeight):
            for x in range(0,self.gameBoardWidth):
                symbolToPrint = "."
                for treasure in self.listOfTreasures:
                   if treasure.x == x and treasure.y == y:
                      symbolToPrint = treasure.gameBoardSymbol
                for player in self.listOfPlayers:
                   if player.x == x and player.y == y:
                      symbolToPrint = player.gameBoardSymbol
                for weapon in self.listOfWeapons:
                  if weapon.x == x and weapon.y == y:
                      symbolToPrint = weapon.gameBoardSymbol
                print(symbolToPrint,end="")
            print() # go to next row
        print()
       
  
    def printInstructions(self) :
        print("Players move around the game board collecting treasures worth points")
        print("The game ends when all treasures have been collected or only 1 player is left")
        print("Here are the point values of all of the treasures:")
        for treasure in self.listOfTreasures :
            print( "   " + treasure.name + "(" + treasure.gameBoardSymbol + ") " + str(treasure.pointValue) )
        print()

class Player :

    # the constructor (initialize all Player variables)
    def __init__(self, initialX, initialY, symb) :     
        self.x = initialX
        self.y = initialY
        self.energy = 8
        self.collectedTreasures = []
        self.collectedWeapons = []
        self.gameBoardSymbol = symb
    
    
    def getPoints(self):
        totalPoints = 0
        for i in self.collectedTreasures:
          totalPoints += i.pointValue
        return totalPoints
    
    def dist(pt1,pt2):
     return ((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)**.5
  
    def collectTreasure(self, treasureItem):
        self.collectedTreasures.append(treasureItem)
        
    
    def collectWeapon(self, weaponItem):
        self.collectedWeapons.append(weaponItem)
        
      
    
    def move(self, direction, distanceToMove):
        if direction == "r":
            if self.energy * 2 < distanceToMove:
              distanceToMove = self.energy * 2
              
                
            self.x = self.x + distanceToMove
            self.energy -= 0.5 * distanceToMove
        elif direction == "l":
            if self.energy * 2 < distanceToMove:
              distanceToMove = self.energy * 2
            self.x = self.x - distanceToMove
            self.energy -= 0.5 * distanceToMove
        elif direction == "u":
            if self.energy * 2 < distanceToMove:
              distanceToMove = self.energy * 2
            self.y = self.y - distanceToMove
            self.energy -= 0.5 * distanceToMove
        elif direction == "d":
            if self.energy * 2 < distanceToMove:
              distanceToMove = self.energy * 2
            self.y = self.y + distanceToMove
            self.energy -= 0.5 * distanceToMove
        else:
            print("That is not a valid direction")
        
class Treasure :

    # constructor (initialilze all variables for a treasure)
    def __init__(self, nm, symb, pointVal, xCoord, yCoord) :
        self.name = nm
        self.gameBoardSymbol = symb
        self.pointValue = pointVal
        self.x = xCoord
        self.y = yCoord

import time
import math

class Random(object):

    def __init__(self, seed = None):
        """
        Create a new random number generator.
        """

        if seed is None:
            seed = int(time.time() * 1000)
        self.seed = seed

        self.nextNextGaussian = None

    def setSeed(self, seed):
        """
        Explicit setter for seed, for compatibility with Java.
        """

        self.seed = seed

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, seed):
        self._seed = (seed ^ 0x5deece66d) & ((1 << 48) - 1)

    def next(self, bits):
        """
        Generate the next random number.
        As in Java, the general rule is that this method returns an int that
        is `bits` bits long, where each bit is nearly equally likely to be 0
        or 1.
        """

        if bits < 1:
            bits = 1
        elif bits > 32:
            bits = 32

        self._seed = (self._seed * 0x5deece66d + 0xb) & ((1 << 48) - 1)
        retval = self._seed >> (48 - bits)

        # Python and Java don't really agree on how ints work. This converts
        # the unsigned generated int into a signed int if necessary.
        if retval & (1 << 31):
            retval -= (1 << 32)

        return retval

    def nextBytes(self, l):
        """
        Replace every item in `l` with a random byte.
        """

        for i in range(0, len(l)):
            if not i % 4:
                n = self.nextInt()
            b = n & 0xff
            # Flip signs. Ugh.
            if b & 0x80:
                b -= 0x100
            l[i] = b
            n >>= 8

    def randrange(self, n = None):
        """
        Return a random int in [0, `n`).
        If `n` is not supplied, a random 32-bit integer will be returned.
        """

        if n is None:
            return self.next(32)

        if n <= 0:
            raise ValueError("Argument must be positive!")

        # This tricky chunk of code comes straight from the Java spec. In
        # essence, the algorithm tends to have much better entropy in the
        # higher bits of the seed, so this little bundle of joy is used to try
        # to reject values which would be obviously biased. We do have an easy
        # out for power-of-two n, in which case we can call next directly.

        # Is this a power of two?
        if not (n & (n - 1)):
            return (n * self.next(31)) >> 31

        bits = self.next(31)
        val = bits % n
        while (bits - val + n - 1) < 0:
            bits = self.next(31)
            val = bits % n

        return val

    def nextLong(self):
        """
        Return a random long.
        Java longs are 64 bits wide, but the generator is only 48 bits wide,
        so we generate two 32-bit numbers and glue them together.
        """

        return (self.next(32) << 32) + self.next(32)

    def nextBoolean(self):
        """
        Return a random bool.
        """

        return bool(self.next(1))

    def nextFloat(self):
        """
        Return a random float in (0, 1).
        Python floats always carry double precision, so this function's return
        values may appear less-than-random, but they are random in single
        precision space.
        """

        return self.next(24) / float(1 << 24)

    def nextDouble(self):
        """
        Return a random float in (0, 1).
        """

        return ((self.next(26) << 27) + self.next(27)) / float(1 << 53)

    def nextGaussian(self):
        """
        Return a normally-distributed double with mean 0 and standard
        deviation 1.
        This method may not be strict enough to perfectly match the produced
        values of Java's Random.nextGaussian().
        """

        if self.nextNextGaussian is None:
            s = 0
            while s == 0 or s >= 1:
                v1 = 2 * self.nextDouble() - 1
                v2 = 2 * self.nextDouble() - 1
                s = v1 * v1 + v2 * v2
            multiplier = math.sqrt(-2 * math.log(s) / s)
            self.nextNextGaussian = v2 * multiplier
            return v1 * multiplier
        else:
            retval = self.nextNextGaussian
            self.nextNextGaussian = None
            return retvalPK
class Weapon:
  def __init__(self,name,locationx,locationy,gameboardsymb,strikedistance):
    self.name = name
    self.x = locationx
    self.y = locationy
    self.gameBoardSymbol = gameboardsymb
    self.strikedistance = int(strikedistance)


    
    



w = int(input("Enter the width of the game board: "))
h = int(input("Enter the height of the game board: "))
numPlayers = int(input("How many players will play? "))
g = Game(w,h,numPlayers)
g.play()


from treasure import Treasure
from player import Player
from randomNum import Random
import sys
from randomNum import Random
rand= Random()
if len(sys.argv) > 1:
  rand.setSeed(int(sys.argv[1]))