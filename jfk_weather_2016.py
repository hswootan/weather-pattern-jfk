import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/jfk_weather_2016_C.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Max temp in 8 and Min temp in 10
    # Date in 5
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get high temperatures form this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = float(row[8])
            low = float(row[10])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    # Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Daily high and low temperatures for JFK (2016)", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (C)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    

