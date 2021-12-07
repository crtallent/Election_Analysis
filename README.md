# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code, 1.38.1

## Summary
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

## Challenge Overview
For this project, I was contacted by an employee of the Colorado Board of Elections to help with an election audit to tabulate the election results for a US Congressional Precinct in Colorado.  While normally completed in Excel, the Colorado Board of Elections was interested in seeing if this audit could be completed via an automated process in Python instead.  If successful, this code could be used to complete election audits for congressional precincts, senatorial audits, and local elections.  The types of votes compiled from the election were as follows:
1. Mail-in ballots
2. Punch cards
3. Direct Recording Electronic Machines

The first step in the process was to import the election results from the [election_results.csv](https://github.com/crtallent/Election_Analysis/commit/431f233d4389a336a87f667c47894caf6f8d0de2) to Visual Studio Code.  The data was then inspected to determine that there were 
3 columns and 369,712 rows of data in the csv file, including the headers.![csv file](https://github.com/crtallent/Election_Analysis/blob/main/Resources/CSV.png "csv").

That is a lot of data!  The data included the ballot ID for each voter and the county name, as well as the candidate that was selected by the voter.  To process the data for analysis, a text file was created to hold the data in a readable format, after the votes were tallied in Visual Studio Code.  Here is a sample of the coding process to determine the number of candidates and begin calculating their votes:  ![coding process - candidate vote count](https://github.com/crtallent/Election_Analysis/blob/main/Resources/Code%20in%20VS.png)

