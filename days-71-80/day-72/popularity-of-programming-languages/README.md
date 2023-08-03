# Day 72: Popularity of Programming Languages

Analyze the popularity of different programming languages over time using post tags in Stack Overflow.

>In addition to the basic instructions, I adapted the charts by implementing a drop-down box widget to dynamically create the number of posts over time for a selected programming language. Every time the drop-down box is used, an image of the chart is saved as a file to capture the current language.

## Project Steps
- Use `.groupby()` to explore the number of posts and entries per programming language
- Convert strings to Datetime objects with `to_datetime()` for easier plotting
- Reshape our DataFrame by converting categories to columns using `.pivot()`
- Use `.count()` and `isna().values.any()` to look for NaN values in our DataFrame, which we then replaced using `.fillna()`
- Create (multiple) line charts using `.plot()` with a for-loop
- Style our charts by changing the size, labels, and upper and lower bounds of our axis
- Add a legend to tell apart which line is which by color
- Smooth out our time-series observations with `.rolling()` and `.mean()` and plotted them to better identify trends over time