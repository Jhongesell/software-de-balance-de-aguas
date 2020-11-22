import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector

def onselect_function(min_value, max_value):
	print(min_value, max_value)
	return min_value, max_value

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [10, 50, 100])

span = SpanSelector(
		ax,
		onselect=onselect_function,
		direction='vertical',
		minspan=40,
		useblit=True,
		span_stays=True,
		button=1,
		rectprops={'facecolor': 'yellow', 'alpha': 0.3}
	)

plt.show()