def play():
    #GAME PART 1 (Rounds + Shuffling)
    import random
    import sys
    import time
    deck=[]
    with open("Deck.txt", "r") as Deck:#Loading Deck from file 'Deck.txt'
      for line in Deck:
        CurrentCard=str(line)#Each card is on a seperate line
        CurrentCard=CurrentCard.strip("\n")
        deck.append(CurrentCard)
    #Shuffling & Splitting the deck
    random.shuffle(deck)
    deck1=[]
    deck2=[]
    for i in range(1, 15):#Takes the first half of the shuffled deck and puts it in an array for player 1
      card=deck[i-1]
      card=str(card)
      card=card.strip("\n")
      card=card.strip(" ")
      deck1.append(card)
    for i in range(16, 30):#Takes the second half of the shuffled deck and puts it in an array for player 2
      card=deck[i-1]
      card=str(card)
      card=card.strip("\n")
      card=card.strip(" ")
      deck2.append(card)
    #Card Comparisons
    def comparison(Card1, Card2):
      print("\n")#solve the problem
      sameColour=False
      #uses string handling (searches for string within string) in order to determine the card.
      if "Red" in Card1 and "Black" in Card2:
        print("Player 1:\tRed\nPlayer 2:\tBlack\nPlayer 1 wins!")
        print("\n")
        return("1")
      elif "Black" in Card1 and "Red" in Card2:
        print("Player 1:\tRed\nPlayer 2:\tBlack\nPlayer 2 wins!")
        print("\n")
        return("2")
      elif "Yellow" in Card1 and "Red" in Card2:
        print("Player 1:\tYellow\nPlayer 2:\tBlack\nPlayer 1 wins!")
        print("\n")
        return("1")
      elif "Red" in Card1 and "Yellow" in Card2:
        print("Player 1:\tRed\nPlayer 2:\tYellow\nPlayer 2 wins!")
        print("\n")
        return("2")
      elif "Black" in Card1 and "Yellow" in Card2:
        print("Player 1:\tBlack\nPlayer 2:\tYellow\nPlayer 1 wins!")
        print("\n")
        return("1")
      elif "Yellow" in Card1 and "Black" in Card2:
        print("Player 1:\tYellow\nPlayer 2:\tBlack\nPlayer 2 wins!")
        print("\n")
        return("2")
      else:
        sameColour=True#as stated within the rules, if the two cards are of the same colour the one with the higher number wins!
      while sameColour==True:
        num1=Card1.strip("Red")
        num1=num1.strip("Yellow")
        num1=num1.strip("Black")
        num2=Card2.strip("Red")
        num2=num2.strip("Yellow")
        num2=num2.strip("Black")
        if int(num1)<int(num2):
          print("Player 1:\t" + Card1 + "\nPlayer 2:\t" + Card2 + "\nPlayer 2 wins!")
          print("\n")
          return("2")
        elif int(num2)<int(num1):
          print("Player 1:\t" + Card1 + "\nPlayer 2:\t" + Card2 + "\nPlayer 1 wins!")
          print("\n")
          return("2")
    #
    # Card Selection System - (Feeds into game)
    #
    input("Press return to begin.")
    print("\n")
    i=0
    j=0
    score1=0
    score2=0
    spoils1=[]
    spoils2=[]
    while i<14 and j<14:#ONLY PLAYS THE FIRST 15 CARDS - NOT NEWLY AQQUIRED CARDS.
      Card1=deck1[i]
      i+=1
      print("Player 1 draws the top card of their deck...")
      time.sleep(0.2)
      print("Player 1's card is " + Card1)
      time.sleep(0.2)
      Card2=deck2[j]
      j+=1
      print("Player 2 draws the top card of their deck...")
      time.sleep(0.2)
      print("Player 2's card is " + Card2)
      input("Press return to continue!")
      winner=comparison(Card1, Card2)
      if winner=="1":
        score1+=1
        spoils1.append(Card2)
      else:
        score2+=1
        spoils2.append(Card1)
    #
    #Giving the Winner the opponent's cards and taking the losses from them
    #
    deck1.append(spoils1)
    num1=len(spoils1)
    for i in range(0, num1):
      deck2.remove(spoils1[i])
    deck2.append(spoils2)
    num2=len(spoils2)
    for i in range(0, num2):
      deck1.remove(spoils2[i])
    #
    #Winner Praise and Deck Exposure
    #
    if score1>score2:
      print("OVERALL WINNER IS PLAYER 1.")
      print("Winning deck...")
      num=len(deck1)
      print(deck1)
    else:
      print("OVERALL WINNER IS PLAYER 2.")
      print("Winning deck...")
      num=len(deck2)
      print(deck2)
    #
