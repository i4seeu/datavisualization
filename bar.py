from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West side story']
num_oscars = [5,11,3,8,10]

#bars are by default with 0.8 , we ll add 0.1, to the left coordinates so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

#plot bars with left x-coordinates [xs] heights [num_oscars]
plt.bar(xs,num_oscars)
plt.ylabel("# of academy awards")
plt.title("My Favourite Movies")
# label x -axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.savefig("bargraph")