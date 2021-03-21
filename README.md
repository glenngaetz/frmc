# frmc
Fundraising metrics calculation class

This module defines the FRMCalc class used for doing the actual calculations of each of 11 metrics. 

## Usage
```
calc = FRMCalc()
second_gift_conversion_rate = calc.second_gift_conversion_rate(acquired, second_gift)
```

## The Metrics

### Net Annual Growth in Donors
The number of donors who gave this year compared to last year.

### Second Gift Conversion Rate
The number of donors who have given a second gift in a given time period.

### Net Cost/Revenue per Donor Acquired
How much it costs to aquire a donor. This metric is generally most
useful when evaluating acquisition campaigns.

### Attrition Rate
The percentage of donors from last year who did not give this year.
Essentially the inverse of Renewal Rate.

### Renewal Rate
The percentage of donors who gave last year and again this year.

### Average Gift
The average gift in a year or campaign. You probably already track this one.

### Median Gift
The middle gift from a given set of gifts. Useful to see in tandem with average
gift, as average gift can sometimes be skewed by a large gift.

### Cost to Raise a Dollar
How much it cost to earn a dollar in revenue. A number less than a dollar
would indicate profitibility, and a number more than a dollar would indicate loss.

### Net Income
The revenue from a campaign or time period less the cost.
This is another one you probably already track.

### Return on Investment
Another way of looking at income vs. cost, this time looking at the revenue
earned for every dollar spent.

### Long-Term Value
This one is fun. The average value of a donor acquired in one year over a given time period.

## Credits
The list of metrics calculated, along with the formulas, is derived from the booklet
"Know Your Top 10: 10 Commonly Used Fundraising Metrics Explained]" by
[Harvey McKinnon Associates][].

[Harvey McKinnon Associates]: http://harveymckinnon.com
