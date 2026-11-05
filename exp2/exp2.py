
# Player 1
runs1 = 148
balls1 = 50
wickets1 = 4
runs_conceded1 = 29
overs1 = 2
catches1 = 3

# Calculate Strike Rate and Economy Rate
strike1 = (runs1 / balls1) * 100
economy1 = runs_conceded1 / overs1

print("PLAYER 1")
print("Strike Rate:", strike1)
print("Economy Rate:", economy1)

# Batting Performance
if runs1 >= 50 and strike1 >= 120:
    batter1 = "Excellent Batter"
elif runs1 >= 30 and strike1 >= 100:
    batter1 = "Good Batter"
elif runs1 >= 20:
    batter1 = "Average Batter"
else:
    batter1 = "Poor Batter"

# Bowling Performance
if wickets1 >= 3 and economy1 <= 6:
    bowler1 = "Excellent Bowler"
elif wickets1 >= 2 and economy1 <= 8:
    bowler1 = "Good Bowler"
elif wickets1 >= 1:
    bowler1 = "Average Bowler"
else:
    bowler1 = "Poor Bowler"

# Fielding Performance
if catches1 >= 2:
    fielder1 = "Outstanding Fielder"
elif catches1 == 1:
    fielder1 = "Active Fielder"
else:
    fielder1 = "Needs Improvement"

# Overall Decision
if batter1 == "Excellent Batter" and bowler1 == "Excellent Bowler":
    overall1 = "Star All-Rounder"
elif batter1 == "Good Batter" and bowler1 == "Good Bowler":
    overall1 = "Strong All-Rounder"
elif batter1 == "Good Batter" or bowler1 == "Good Bowler":
    overall1 = "Supporting All-Rounder"
else:
    overall1 = "Needs Improvement"

print("Batting:", batter1)
print("Bowling:", bowler1)
print("Fielding:", fielder1)
print("Overall:", overall1)
print()


# Player 2
runs2 = 179
balls2 = 62
wickets2 = 8
runs_conceded2 = 32
overs2 = 3
catches2 = 2

strike2 = (runs2 / balls2) * 100
economy2 = runs_conceded2 / overs2

print("PLAYER 2")
print("Strike Rate:", strike2)
print("Economy Rate:", economy2)

if runs2 >= 50 and strike2 >= 120:
    batter2 = "Excellent Batter"
elif runs2 >= 30 and strike2 >= 100:
    batter2 = "Good Batter"
elif runs2 >= 20:
    batter2 = "Average Batter"
else:
    batter2 = "Poor Batter"

if wickets2 >= 3 and economy2 <= 6:
    bowler2 = "Excellent Bowler"
elif wickets2 >= 2 and economy2 <= 8:
    bowler2 = "Good Bowler"
elif wickets2 >= 1:
    bowler2 = "Average Bowler"
else:
    bowler2 = "Poor Bowler"

if catches2 >= 2:
    fielder2 = "Outstanding Fielder"
elif catches2 == 1:
    fielder2 = "Active Fielder"
else:
    fielder2 = "Needs Improvement"

if batter2 == "Excellent Batter" and bowler2 == "Excellent Bowler":
    overall2 = "Star All-Rounder"
elif batter2 == "Good Batter" and bowler2 == "Good Bowler":
    overall2 = "Strong All-Rounder"
elif batter2 == "Good Batter" or bowler2 == "Good Bowler":
    overall2 = "Supporting All-Rounder"
else:
    overall2 = "Needs Improvement"

print("Batting:", batter2)
print("Bowling:", bowler2)
print("Fielding:", fielder2)
print("Overall:", overall2)
print()


# Player 3
runs3 = 156
balls3 = 59
wickets3 = 6
runs_conceded3 = 29
overs3 = 4
catches3 = 2

strike3 = (runs3 / balls3) * 100
economy3 = runs_conceded3 / overs3

print("PLAYER 3")
print("Strike Rate:", strike3)
print("Economy Rate:", economy3)

if runs3 >= 50 and strike3 >= 120:
    batter3 = "Excellent Batter"
elif runs3 >= 30 and strike3 >= 100:
    batter3 = "Good Batter"
elif runs3 >= 20:
    batter3 = "Average Batter"
else:
    batter3 = "Poor Batter"

if wickets3 >= 3 and economy3 <= 6:
    bowler3 = "Excellent Bowler"
elif wickets3 >= 2 and economy3 <= 8:
    bowler3 = "Good Bowler"
elif wickets3 >= 1:
    bowler3 = "Average Bowler"
else:
    bowler3 = "Poor Bowler"

if catches3 >= 2:
    fielder3 = "Outstanding Fielder"
elif catches3 == 1:
    fielder3 = "Active Fielder"
else:
    fielder3 = "Needs Improvement"

if batter3 == "Excellent Batter" and bowler3 == "Excellent Bowler":
    overall3 = "Star All-Rounder"
elif batter3 == "Good Batter" and bowler3 == "Good Bowler":
    overall3 = "Strong All-Rounder"
elif batter3 == "Good Batter" or bowler3 == "Good Bowler":
    overall3 = "Supporting All-Rounder"
else:
    overall3 = "Needs Improvement"

print("Batting:", batter3)
print("Bowling:", bowler3)
print("Fielding:", fielder3)
print("Overall:", overall3)
print()


# Player 4
runs4 = 117
balls4 = 41
wickets4 = 5
runs_conceded4 = 31
overs4 = 3
catches4 = 2

strike4 = (runs4 / balls4) * 100
economy4 = runs_conceded4 / overs4

print("PLAYER 4")
print("Strike Rate:", strike4)
print("Economy Rate:", economy4)

if runs4 >= 50 and strike4 >= 120:
    batter4 = "Excellent Batter"
elif runs4 >= 30 and strike4 >= 100:
    batter4 = "Good Batter"
elif runs4 >= 20:
    batter4 = "Average Batter"
else:
    batter4 = "Poor Batter"

if wickets4 >= 3 and economy4 <= 6:
    bowler4 = "Excellent Bowler"
elif wickets4 >= 2 and economy4 <= 8:
    bowler4 = "Good Bowler"
elif wickets4 >= 1:
    bowler4 = "Average Bowler"
else:
    bowler4 = "Poor Bowler"

if catches4 >= 2:
    fielder4 = "Outstanding Fielder"
elif catches4 == 1:
    fielder4 = "Active Fielder"
else:
    fielder4 = "Needs Improvement"

if batter4 == "Excellent Batter" and bowler4 == "Excellent Bowler":
    overall4 = "Star All-Rounder"
elif batter4 == "Good Batter" and bowler4 == "Good Bowler":
    overall4 = "Strong All-Rounder"
elif batter4 == "Good Batter" or bowler4 == "Good Bowler":
    overall4 = "Supporting All-Rounder"
else:
    overall4 = "Needs Improvement"

print("Batting:", batter4)
print("Bowling:", bowler4)
print("Fielding:", fielder4)
print("Overall:", overall4)



