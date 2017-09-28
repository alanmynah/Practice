from hands import YatzyHand
from dice import D6
from scoresheets import YatzyScoresheet
hand = YatzyHand()
three = D6(value=3)
four = D6(value=4)
one = D6(value=1)
hand[:] = [one, three, three, four, four ]
pr = YatzyScoresheet().score_one_pair(hand)
print (pr)