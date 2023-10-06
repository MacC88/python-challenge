import csv

# Files to load
file_to_load = "C:/Users/purot/Desktop/Boot_Camp/python-challenge/PyPoll/Resources/election_data.csv"

# Files to save
file_to_save = ("C:/Users/purot/Desktop/Boot_Camp/python-challenge/PyPoll/analysis/election_data.txt")
 
total_votes = 0

# creating variables to store my information for the analysis
candidate_options = []
candidate_votes = {}

# reseting data points
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data: 
    reader = csv.reader(election_data)

    # use of next to skip first title row in csv file 
    next(reader)
    
    # we count the votes and store it in a variable
    for row in reader:
      
        total_votes += 1
        candidate_name = row[2]

        #  we identify counts to names
        if candidate_name not in candidate_options: 

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

# write and store the data in a text file  
with open(file_to_save, "w") as txt_file:

    # we foramt and print the results 
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------------------\n")
    print(election_results, end="")

    # write and store the data in a text file 
    txt_file.write(election_results)

    # we loop through the names and the votes and calculate the percentage each candidate recieved
    for candidate_name in candidate_votes: 
 
        votes = candidate_votes[candidate_name]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")
 
        print(candidate_results)

        # write and store the data in a text file 
        txt_file.write(candidate_results)
     
        # we identify the winning candidate and the percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage): 

            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # we format and print the results
    winning_candidate_summary = (
        f"-----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------------------\n")
    print(winning_candidate_summary)
    
    # write and store the data in a text file 
    txt_file.write(winning_candidate_summary)