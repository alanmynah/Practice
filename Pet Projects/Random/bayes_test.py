"""This is a Bayes test calculator. Just trying to wrap my head around it
"""

# The disease affects 1 in 1000 sick people.
deseaseDestribution = 0.001
amountOfHealthy = 1 - deseaseDestribution
# The test success rate is 99%
testAccuracy = 0.99

#If we test 1000 people and I an tested positive, what is the chance I have the desease?

myChances = (testAccuracy * deseaseDestribution) / ((deseaseDestribution * testAccuracy) + (amountOfHealthy * (1 - testAccuracy)))
print (myChances)
