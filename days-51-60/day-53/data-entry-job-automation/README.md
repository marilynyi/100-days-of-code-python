# Day 53: Data Entry Job Automation

## Capstone Project 

Create a bot using Beautiful Soup and Selenium to pull Zillow rental property information and submit it via individual Google Forms responses into a Google Sheets file

## Project Requirements
1. Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address.
2. Create a list of links for all the listings you scraped.
3. Create a list of prices for all the listings you scraped.
4. Create a list of addresses for all the listings you scraped.
5. Use Selenium to fill in the form you created. Each listing should have its price/address/link added to the form. You will need to fill in a new form for each listing.


## Custom Zillow page to scrape

We use `Denver, CO` and additional search filters to create our custom URL.

<img src="demos/zillow_results.png" width=600>

## Console output

Output of property details is printed in the terminal before running the Google Forms automation part of the project.

<img src="demos/output_console.png" width=400>

## Auto fill and submit each response on Google Forms

The number of seconds `n` in the `time.sleep(n)` function can be changed to accommodate slower or faster browser loading time.

The `address`, `price`, and `link` for each property is filled in before submitting the form and refreshing the page to start a new response form.

<img src="demos/form_submit_full.gif" width=600>

## Information populates in Google Sheets file

Demo below has been sped up to quickly show results.

<img src="demos/form_populate_sped_up.gif" width=600>
