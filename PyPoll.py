# Data needed for retrieval:
# 1. Total # of votes cast
# 2. Complete list of candidates who received votes
# 3. % of votes each candidate won
# 4. Total # of votes each candidate won
# 5. Winner of election based on popular vote.
# Assign a variable for the file to load and the path.
file_to_load = "Resources/election_results.csv"
election_data = open(file_to_load, 'r')
# To do: perform analysis.
# Close the file.
election_data.close()
# Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: perform analysis.
    print(election_data)
import csv    
import os 
# Assign a variable for the file to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt") 
# Using the with statement, open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\nArapahoe\n--------------------------------\nDenver\nJefferson")
with open(file_to_load) as election_data:
    # To do: read and analyze the data (read file object with reader function)
    file_reader = csv.reader(election_data)
    # Print header row only.
    headers = next(file_reader)
    print(headers)


   





