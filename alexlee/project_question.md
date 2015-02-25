## Data Science - Project Question
### Alex Lee
#### 1/6/2015

### Project Question

Can I predict future price movements in a market index (or for a specific security) with consistent, statistically significant accuracy improvements over a coin flip (assuming price movements are an even random walk, a coin flip would be the baseline measure of accuracy)?  

#### Corollary questions:
* Can predictions be achieved through "machine technical analysis" (translation of data into a visual rather than numerical format try to get a computer vision algorithm to "learn" what price movements certain patterns might imply, using standardized and simple image formats)?
* If the latter is unpromising / too difficult, can the introduction of additional features from non-price datasets (e.g. news items, social media sentiment, macro statistical data releases, security fundamental data releases, etc.) significantly improve predictive performance vs. pattern analysis of just the prices themselves?
* Is an even random walk a good baseline for performance evaluation?  If not, how to judge the performance of the model?

### Data

Minute-tick data can be obtained from Google Finance for a given ticker for a specified historical range using the following URL format to scrape for data:

`http://www.google.com/finance/getprices?i=[PERIOD]&p=[DAYS]d&f=d,o,h,l,c,v&df=cpct&q=[TICKER]`

* [PERIOD]: Interval/frequency in seconds (60 is the most granular that the data are available for)
* [DAYS]: Integer number of days back in time to fetch data for
* [TICKER]: A valid ticker symbol that you could search for on Google Finance

#### Notes on the data

* Data timestamps are in an unintelligible format to me (e.g. today is "a1420554660").  Data come sequentially, though, so this is a minor issue.
* On a per-minute level, the fields available are: Close, High, Low, Open, and Volume.  The data are not patchy, as far as these fields are concerned.  I expect that the Volume field may have a significant impact on the change in price values of subsequent ticks.
* [Quandl](https://www.quandl.com) appears to be a good source of corollary economic and financial data, though figuring out how to integrate it / whether or not it would provide much added benefit in answering the question posed above (if there is a large mismatch in time scales, e.g.) is something I have not looked into as yet.

### Why this topic?

I am interested in financial markets, and particularly given the incredible volume of (very granular) data that they generate, am very interested in exploring ways that those data can be exploited to generate returns that a human analyst, unaided by algorithms, might be unable to capture.

The "point" of trying to answer the question, as it has been posed, is to be able to have a sense, in advance, of which direction the price of a security (or if only evaluating a market index, securities in that market, generally) is heading.  If you have a relatively accurate prediction of this, you can determine which side of a trade to take in a short term situation (theoretically, if modeling at the minute level worked, you could expand the model to cover sub-second trades), and/or you can use the model's output to help determine how to set your bid/ask spread for a security on a rapidly evolving basis.  This would primarily have application in automated, high-frequency trade matching systems, and (if the model were accurate enough to generate returns overall, vs. some benchmark rate of return for the company utilizing it) could allow for the algorithm to "decide" how and when to trade, faster than a human could reasonably comprehend.

Given the above, the exercise of predicting price movement is mostly an academic one -- without a connection to additional logic of a trading system on how to use the output of the model to either trade directly and/or set a bid/ask spread, plus a full backtesting suite to compare that usage of the model's output to some other benchmark trading strategy, the prediction alone doesn't tell us if it could be used to "make money."  However, given some basic knowledge about the operation of financial markets, it does at least suggest the possibility of real-world performance as measured by returns, and presumably if you DID have access to a more robust apparatus for testing, such a predictive model could be tweaked/integrated with other models to improve performance in some manner, if not directly.
