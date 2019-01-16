print('hey')

S1 = "Chinmay is the best person on earth"
S2 = "No chance, Siddharth is the best definitely"

from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt


v = TfidfVectorizer()

r = v.fit_transform([S1, S2])

print(r)



