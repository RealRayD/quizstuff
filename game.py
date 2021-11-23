import logging
import sqlite3
#connect with the leaderboard database
conn=sqlite3.connect('leader.db')
#create a cursor, to be able to put data into the database
c=conn.cursor()
print("This is a quiz about CS:GO")
print("There are yes/no questions, and questions you have to answer with numbers/words")
#player name variable, used in the database
name=input("Enter your name:")
#catches the answer if the player wants to take the quiz
answer=input("Ready to start(yes/no)")
#empty point counters in the start, for every correct answer, the count increases by 1
score=0
monq=0
skinq=0
espq=0
#points are calculated but multiplying the total with this coeficient, and then rounded with 100
pointcoef=0.75
#uses the player input, to determine if to start the quiz or no
if answer.lower()=="yes":
    answer1=input("How much does an AK-47 cost? ")
    if answer1=="2700":        
        monq+=1
        score+=1
        print("You are correct!")
    else:
        print("AK-47 costs 2700$")
    answer1=input("How much will 2 flashes and a M4A1-S cost? ")
    if answer1=="3500":
        monq+=1
        score+=1
        print("You are correct!")
    else:
        print("It would cost a total of 3500$")
    answer1=input("How much does kevlar + helmet cost? ")
    if answer1=="1000":
        monq+=1
        score+=1
        print("You are correct!")
    else:
        print("It would cost 1000$")
    answer1=input("How much money will the terrorists gain if they plant the bomb, but fail to secure the round? ")
    if answer1=="800":
        monq+=1
        score+=1
        print("You are correct")
    else:
        print("They would gain 800$")
    answer1=input("How much will a deagle, kevlar + helmet and a smoke grenade cost? ")
    if answer1=="2000":
        monq+=1
        score+=1
        print("You are correct")
    else:
        print("It would cost a total of 2000$")
    answer1=input("How much does the MP9 cost? ")
    if answer1=="1250":
        monq+=1
        score+=1
        print("You are correct")
    else:
        print("It costs 1250$")
    answer1=input("Which of these is an AK-47 skin? Stoneskin, Howl, Bloodsport or Fade? ")
    if answer1.lower()=="bloodsport":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("AK-47 - Bloodsport")
    answer1=input("Which of these is an AWP skin? Gugnir, Cortex, Flashback or Hive? ")
    if answer1.lower()=="gugnir":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("AWP - Gugnir")
    answer1=input("Which of these is a Deagle skin? Cartel, Snapdragon, Snakebite or Blaze? ")
    if answer1.lower()=="blaze":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("Deagle - Blaze")
    answer1=input("Which of these is an M4A4 skin? Masterpiece, BOOM, Emerald or Howl? ")
    if answer1.lower()=="howl":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("M4A4 - Howl")
    answer1=input("Which of these is an USP-S skin? Flashback, Hellfire, Franklin or Arabesque? ")
    if answer1.lower()=="flashback":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("USP-S - Flashback")
    answer1=input("Which of these AWP skins is the most expensive? Graphite, Medusa, Coricera or Atheris? ")
    if answer1.lower()=="medusa":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("AWP - Medusa")
    answer1=input("Which of these cases is the most expensive? Gamma, Riptide, Bravo or Wildfire? ")
    if answer1.lower()=="bravo":
        skinq+=1
        score+=1
        print("You are correct")
    else:
        print("Bravo case")
    answer1=input("Which team has won the most major titles?")
    if answer1.lower()=="astralis":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("Astralis have won 4 titles")
    answer1=input("Which team won the last major?")
    if answer1.lower()=="navi":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("NAVI won the last major")
    answer1=input("Which team won the first major?")
    if answer1.lower()=="fnatic":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("Fnatic won the first major")
    answer1=input("Which of these players has been in every major so far? apEx, rain, Hobbit or olofmeister? ")
    if answer1.lower()=="olofmeister":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("olofmeister has attended every major so far")
    answer1=input("Which of these players was the HLTV mvp of 2020? ZywOo, dev1ce, blameF or s1mple? ")
    if answer1.lower()=="zywoo":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("ZywOo was the #1 ranked player of 2020")
    answer1=input("Who is the AWPer for NIP? oskar, REZ, dev1ce or sloWi? ")
    if answer1.lower()=="dev1ce":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("dev1ce is the AWPer for NIP")
    answer1=input("Who is the IGL for FaZe? ")
    if answer1.lower()=="karrigan":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("karrigan is the IGL for FaZe")
    answer1=input("Who was the runner up in the last major? ")
    if answer1.lower()=="G2":
        espq+=1
        score+=1
        print("You are correct")
    else:
        print("G2 were the runner up team")
#point calculations
monqp=monq*pointcoef
skinp=skinq*pointcoef
espp=espq*pointcoef
totalpoints=(monqp+skinp+espp)*100
#makes sure the player starts with a capital letter
capname=(name.lower()).capitalize()
print(capname,", your final score:",score," and your total points: ",totalpoints)
#creates the leaderboard table and passes data into it
c.execute('CREATE TABLE IF NOT EXISTS leaderboard ([name] VARCHAR[20], [score] INTEGER)')
c.execute('INSERT INTO leaderboard (name, score) VALUES (?, ?)', (capname, totalpoints))
#commits the changes and closes the connection
conn.commit()
conn.close()
#using the logging module to create a log file, which updates every time the quiz is taken
logging.basicConfig(
    level=logging.INFO,
    format='{asctime} {levelname:<8} {message}',
    style='{',
    filename='thelog.log',
    filemode='w'
)
logging.info('This user played the quiz and was added to the database: %s' %capname)
