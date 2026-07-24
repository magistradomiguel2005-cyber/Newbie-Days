t1 = 0
t2 = 0
t3 = 0
t4 = 0 

a1 = int(input("Q1) Do you like Dawn or Dusk?" + "\n" + "1) Dawn " + "2) Dusk" + "\n"))

if a1 == 1:
  t1 += 1
  t2 += 1
elif a1 == 2:
  t3 += 1
  t4 += 1
else:
  print("Wrong input")



a2 = int(input("Q2) When I’m dead, I want people to remember me as:" + "\n" + "1) The Good " + "2) The Great " + "3) The Wise " + "4) The Bold" + "\n" ))

if a2 == 1:
  t3 += 2
elif a2 == 2:
  t4 += 2
elif a2 == 3:
  t2 += 2
elif a2 == 4:
  t1 += 2
else:
  print("Wrong input")


a3 = int(input("Q3) Which kind of instrument most pleases your ear?" + "\n"+ "1) The violin " + "2) The trumpet " + "3) The piano " + "4) The drum" + "\n" ))

if a3 == 1:
  t4 += 4
elif a3 == 2:
  t3 += 4
elif a3 == 3:
  t2 += 4
elif a3 == 4:
  t1 += 4
else:
  print("Wrong input")




print("🦁 Gryffindor: " + str(t1) + " pts")
print("🦅 Ravenclaw: " + str(t2) + " pts")
print("🦡 Hufflepuff: " + str(t3) + " pts")
print("🐍 Slytherin: " + str(t4) + " pts")

if t1 > t2 and t1 > t3 and t1 > t4:
  print("🦁 Gryffindor Wins!")
elif t2 > t1 and t2 > t3 and t2 > t4:
  print("🦅 Ravenclaw Wins!")
elif t3 > t1 and t3 > t2 and t3 > t4:
  print("🦡 Hufflepuff Wins!")
elif t4 > t1 and t4 > t2 and t4 > t3:
  print("🐍 Slytherin Wins!")


