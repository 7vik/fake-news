love = '''I suppose that only a single mountain-top,
the hideous monolith-crowned citadel
whereon great Cthulhu was buried,
actually emerged from the waters. When I
think of the extent of all that may be
brooding down there I almost wish to kill
myself forthwith. Johansen and his men
were awed by the cosmic majesty of this
dripping Babylon of elder daemons, and
must have guessed without guidance that
it was nothing of this or of any sane
planet.That was all. After that Johansen only
brooded over the idol in the cabin and
attended to a few matters of food for
himself and the laughing maniac by his
side. He did not try to navigate after the
first bold flight, for the reaction had taken
something out of his soul. Then came the
storm of April 2nd, and a gathering of the
clouds about his consciousness.Upon retiring, he had had an
unprecedented dream of great Cyclopean
cities of titan blocks and sky-flung
monoliths, all dripping with green ooze
and sinister with latent horror.
Hieroglyphics had covered the walls and
pillars, and from some undetermined point
below had come a voice that was not a
voice; a chaotic sensation which only
fancy could transmute into sound, but
which he attempted to render by the
almost unpronounceable jumble of letters,
“Cthulhu fhtagn”.'''

issac = '''For decades, Multivac had helped design
the ships and plot the trajectories that
enabled man to reach the Moon, Mars,
and Venus, but past that, Earth's poor
resources could not support the ships.
Too much energy was needed for the long
trips. Earth exploited its coal and uranium
with increasing efficiency, but there was
only so much of both.
Jerrodd, Jerrodine, and Jerrodette I and II
watched the starry picture in the visiplate
change as the passage through
hyperspace was completed in its non-time
lapse. At once, the even powdering of
stars gave way to the predominance of a
single bright shining disk, the size of a
marble, centered on the viewing-screen
"I'm still under two hundred. --But to get
back to my point. Population doubles
every ten years. Once this GaIaxy is filled,
we'll have filled another in ten years.
Another ten years and we'll have filled two
more. Another decade, four more. In a
hundred years, we'll have filled a
thousand Galaxies. In a thousand years,
a million Galaxies. In ten thousand years,
the entire known universe. Then what?"'''



love = '''On the occasion of the visit, ran the professor’s manuscript, the sculptor abruptly asked
for the benefit of his host’s archaeological knowledge in identifying the hieroglyphics on
the bas-relief. He spoke in a dreamy, stilted manner which suggested pose and alienated
sympathy; and my uncle shewed some sharpness in replying, for the conspicuous
freshness of the tablet implied kinship with anything but archaeology. Young Wilcox’s
rejoinder, which impressed my uncle enough to make him recall and record it verbatim,
was of a fantastically poetic cast which must have typified his whole conversation, and
which I have since found highly characteristic of him.'''

love_sum = 0
issac_sum = 0
love_words = 0
issac_words = 0

love_list = love.split(' ')
issac_list = issac.split(' ')


for word in love_list:
    love_sum += len(word)
    love_words += 1

for word in issac_list:
    issac_sum += len(word)
    issac_words += 1

love_f = love_sum/love_words
issac_f = issac_sum/issac_words

print("Love freq = "+str(love_f))
print("Issac freq = "+str(issac_f))


