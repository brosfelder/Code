class ScoreSheet:
    # Upper section of card
    # TODO: If the upper section totals >=63; add 35 points to upper section score
    ones = 0 # Count and add only 1's
    twos = 0 # Count and add only 2's
    threes = 0 # Count and add only 3's
    fours = 0 # Count and add only 4's
    fives = 0 # Count and add only 5's
    sixes = 0 # Count and add only 6's

    # Lower section of card
    threeOfAKind = 0 # Three of a kind: Add total of all dice 
    fourOfAKind = 0 # Four of a kind: Add total of all dice 
    fullHouse = 0 # Two of 1 number; 3 of another; ADD 25 TO SCORE
    smallStraight = 0 # Sequence of 4; ADD 30 TO SCORE
    largeStraight = 0 # Sequence of 5; ADD 40 TO SCORE
    yahtzee = 0 # Five of a kind; ADD 50 TO SCORE
    chance = 0 # Total of all dice
    yahtzeeBonus = 0 #I don't remember :( 