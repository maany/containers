# Rules:
# 1. Cup Spinning Algorithm has to be executed with a Python 3.6.8 interpreter (Installed on LXPLUS)
# 2. The winner of the day is the spin master on the next day
# 3. If the Spin Master does not show up, he/she gets a red dot! Classic red-dot rules apply to pick a replacement master.
# 4. If somebody changes their seed after posting it (editing it), it will considered as cheating. Classical spinning rules apply then.
# 5. The posted seed needs to be a copy&pastable string which needs to follow the regular expression "[A-Za-z0-9]*" - If the regular expression is not followed, this is considered a spin error! Regular cheating rules apply
# 6. Protests and appeals against a result can be raised until the start of the following spin.
# 7. Posting a seed from someone not from today's spinners list is willful sabotage and cause the saboteur to get selected as cheater.
 
# Procedure:
# 1) Spin-Master notifies the channel for the upcoming spin and declares/arranges todays Spinners and posts them to the Chat (Before calling for the seeds)
todays_spinners = ['Dimitrios', 'Martin', 'Mayank', 'Cedric']
 
# 2) Spin-Master opens a 15s window, signalling the start and end of the window (Tolerance: 14-18s) in chat; Afterwards he/she concatenate the seed and posts it to the channel
todays_seed = '''AlmostVacationHelloFromTheAirportIAmHungryAfterTheJeuneGenevoisweekend'''
 
# 3) Spin-Master announces Spin Result (Entire output of the script below) in Chat
import random
import hashlib
n = 0
while (n < 1E7):
    n = n + 1
    todays_seed = hashlib.sha512(todays_seed.encode('utf-8')).hexdigest()
 
random.seed(todays_seed)
if random.random() < 0.25:
    spin_off_partner1 = random.choice(todays_spinners)
    spin_off_partner2 = random.choice([x for x in todays_spinners if x != spin_off_partner1 ])
    print('The Cup points in between %s and %s' % (spin_off_partner1, spin_off_partner2))
    while random.random() < 0.1:
        print('The cup points in between %s and %s AGAIN!' % (spin_off_partner1, spin_off_partner2))
    print('The Spin-Off Winner is %s' % random.choice([spin_off_partner1, spin_off_partner2]))
else:
    print('The cup points to %s' % random.choice(todays_spinners))