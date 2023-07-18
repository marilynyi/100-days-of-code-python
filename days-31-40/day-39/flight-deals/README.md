# Day 39: Flight Deals

Send SMS text messages notifying the user of any flight deals in the next six months. Destination cities and price thresholds are supplied by the user in the `Flight Deals` Google Sheets doc.

## Flight Deals doc
- File resides in hidden `config` folder. 
- User manually populates the
`City` and `Lowest Price` columns with their desired destinations and price thresholds.
- `IATA Code` column auto-populates when `main.py` is run.

<img 
  src="https://github.com/marilynyi/100-days-of-code-python/blob/main/days-31-40/day-39/flight-deals/images/Flight_Deals.png"
  width="400">

## SMS Text Notification
SMS text messages are sent only if
- prices are lower than specified price thresholds
- flights are non-stop (no layovers)
- flights are within the next 6 months
- trips are between 7-28 days long

<img 
  src="https://github.com/marilynyi/100-days-of-code-python/blob/main/days-31-40/day-39/flight-deals/images/SMS_Test.PNG" 
  width="300">

