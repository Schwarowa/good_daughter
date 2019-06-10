
answer = "no"
while answer != "y":
  answer = raw_input("Am I a perfect daughter?!(y/n)")
  if answer != "y":
    print "Sorry, you're wrong. Try again!"
else:
    print "You're absolutely right!"