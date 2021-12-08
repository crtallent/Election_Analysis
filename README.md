# Election_Analysis

## Overview of Election Audit
For this project, I was contacted by an employee of the Colorado Board of Elections to help with an election audit to tabulate the election results for a US Congressional Precinct in Colorado.  While normally completed in Excel, the Colorado Board of Elections was interested in seeing if this audit could be completed via an automated process in Python instead.  If successful, this code could be used to complete election audits for congressional precincts, senatorial audits, and local elections.  The types of votes compiled from the election were as follows:

1. Mail-in ballots
2. Punch cards
3. Direct Recording Electronic Machines

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:  
    - Diana Degette, who received 73.8% of the vote and 272,892 number of votes.
- The counties participating in the election were:
    - Jefferson County, counting for 10.5% of the total votes and 38,855 number of votes.
    - Denver County, counting for 82.8% of the total votes and 306,055 number of votes.
    - Arapahoe County, counting for 6.7% of the total votes and 24,801 number of votes.
- The county with the largest number of votes was Denver County, with 306,055 votes cast.

[![Results](https://github.com/crtallent/Election_Analysis/blob/main/Resources/Results.png)

The first step in the process was to import the election results from the [election_results.csv](https://github.com/crtallent/Election_Analysis/commit/431f233d4389a336a87f667c47894caf6f8d0de2) to Visual Studio Code.  The data was then inspected to determine that there were 
3 columns and 369,712 rows of data in the csv file, including the headers.![csv file](https://github.com/crtallent/Election_Analysis/blob/main/Resources/CSV.png "csv").

That is a lot of data!  The data included the ballot ID for each voter and the county name, as well as the candidate that was selected by the voter.  To process the data for analysis, a text file was created to hold the data in a readable format, after the votes were tallied in Visual Studio Code.  Here is a sample of the coding process to determine the number of candidates and begin calculating their votes:  ![coding process - candidate vote count](https://github.com/crtallent/Election_Analysis/blob/main/Resources/Code%20in%20VS.png)

Once all votes were tallied, we were able to see how many votes each candidate received, their percentage of votes won in comparison to the total votes cast, as well as the winner of the election. The text file summarizing these results can be found in the [text_file](https://github.com/crtallent/Election_Analysis/tree/main/analysis).


## Election - Audit Summary

As outlined above, we were able to complete an audit of the election results using Visual Studio Code and Python.  We were also able to see these results in a user-friendly format, via the text file we created to store our results.  This process allowed us to calculate the results in an efficient, automated manner.  This script can be used for any election going forward, with just a few modifications to the code:

```
'candidate_name = row[2]
```
- 'county_name = row[1]()' can be modified for the row number containing the counties, town, or cities where the voters cast their votes


