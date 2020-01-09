#Players get first card
for n in range(int(players)):
	if playerData["Hit"][n][0]=="y":
		playerData["GamesPlayed"][n]+=1
	#Draws card and increases ace count if Ace
		playerCard = drawCard()
		playerData["Ace"][n][0]+=playerCard[2]

		#Adds cards to players hand
		playerData["Cards"][n][0].append(playerCard[0])

		#adds to total value of cards in hand
		playerData["HandValue"][n][0]+=playerCard[1]

#If player wins
if playerData["HandValue"][n][h]>dealerX and playerData["HandValue"][n][h]<=21:
	print("\n\n\nYou Win!  +" + str(playerData["Bidamount"][n][h])+"!!!!\n\n\n")
	if playerData["Bonus"][n][h]>0:
		print("\tRisk taker bonus +" + str(playerData["Bonus"][n][h])+"!!!!!!!\n\n\n")
	playerData["Cash"][n]+=playerData["Bidamount"][n][h]+playerData["Bonus"][n][h]
	playerData["MoneyDiff"][n][h]+=playerData["Bidamount"][n][h]+playerData["Bonus"][n][h]
	input("Press enter...")
	playerData["Won"][n] +=1

#Prints game results
for n in range(int(players)):
	for h in range(playerData["Hands"][n]):
		if playerData["MoneyDiff"][n][h]>0:
			print("\n"+str(playerData["Name"][n]) +"  "+ str(playerData["Cards"][n][h]) +"  "+ str(playerData["HandValue"][n][h])+"  Money made: "+str(playerData["MoneyDiff"][n][h])+"  --Cash left: "+str(playerData["Cash"][n]))
		else:
			print("\n"+str(playerData["Name"][n]) +"  "+ str(playerData["Cards"][n][h]) +"  "+ str(playerData["HandValue"][n][h])+"  Money lost: "+str(playerData["MoneyDiff"][n][h])+"  --Cash left: "+str(playerData["Cash"][n]))

		if playerData["Cash"][n]<=0:
			print(str(playerData["Name"][n]) +", you are out of money, thanks for playing!\n")
			if playerData["HandValue"][n][0]>0:
				brokePlayers+=1
