import matplotlib.pyplot as plt

fig, ax = plt.subplots()

guess = ['1', '2', '3', '4', '5', '6']
guesses = [10, 20, 30, 60, 50, 100]

ax.barh(guess, guesses)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis=u'both', which=u'both',length=0)
# ax.get_xaxis().set_ticks([])
plt.show()