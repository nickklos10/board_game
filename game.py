class Game:
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
          
          w = rand.randrange(gameBoardWidht - 1)
          h = rand.randrange(gameBoardHeight - 1)
          
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

        w1 = Weapon("Gun", rand.randrange(gameBoardWidht), rand.randrange(self.gameBoardHeight),"/", 7)
        self.listOfWeapons.append(w1)
        w2 = Weapon("Grenade",rand.randrange(gameBoardWidht), rand.randrange(self.gameBoardHeight), "o", 4)
        self.listOfWeapons.append(w2)
        
       

    
    
 def play(self):
        self.printInstructions()
      
        self.drawUpdatedGameBoard()
    
    
        # MAIN GAME LOOP to ask players what they want to do
        currentPlayerNum = 0
        while (len(self.listOfTreasures) >= 1):
            
            # get the player object for the player whose turn it is
            currentPlayer = self.listOfPlayers[currentPlayerNum];
         
            # ask the player what they would like to do
            choice = input("Player " + str(currentPlayer.gameBoardSymbol) + ", do you want to (m)ove, (r)est or (a)ttack? ")
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
          for weapons in self.listOfWeapons:
            if weapons.strikedistance > self.listOfWeapons[highest].strikedistance:
              highest = loop
            loop += 1
          
          for player in self.listOfPlayers:
            if plyr != player:
             if ((plyr.x-player.x)**2 + (plyr.y-player.y)**2)**.5 < self.listOfWeapons[highest].strikedistance:
                self.listOfPlayers.remove(player)
                print("You eliminated player",player.gameBoardSymbol,"from the game!")
         
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