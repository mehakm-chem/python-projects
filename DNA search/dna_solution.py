'''
dna_solution.py -- Mehak Mittal -- November 3, 2023
A python program that identifies the text file containing dna information
and returns who that dna text file correspond to
'''
def read_unk_sequence(user_file):
    '''
    reads the user inputted DNA sequence and
    returns it as a single string
    '''
    fo_seq = open(user_file, 'r') #open the file and read it
    l_file = fo_seq.read() #since file has a single line

    return(l_file) #returns a string

def line_modifications(any_line):
    '''
    modifies any given list by adding
    '''
    mod_line = any_line.split(",")
    mod_line = any_line.strip()

    return(mod_line)

#converting csv file into a python friendly database
def read_csv(csv_file):
    '''
    reads the csv file, modifies it and returns it in
    the form of a list of lists.  
 
    '''
    fo_data = open(csv_file, mode = 'r')
    csv_list = [] #empty list to store the csv values

    csv_line = fo_data.readline()
    s_line = line_modifications(csv_line)

    csv_list.append(s_line.split(',')) #adding the first (modified) line
                                       #to empty list


    for csv_line in fo_data: #rest of the lines in csv file
        s_line = line_modifications(csv_line)
        csv_list.append(s_line.split(','))
    
    fo_data.close

    for row in csv_list:
        for item in row:
            if item == 'name': #not necessary for the databse
                row.remove(item)

    #[['AGAT', 'AATG', 'TATC'], ['Alice', '5', '2', '8'], 
    #['Bob', '3', '7', '4'], ['Charlie', '6', '1', '5']]
    
    return(csv_list)

def count_repetitions(unk_seq, seq_list, j):
    #j is the postion in seq_list
    '''
    counts the maximum number of times given DNA sequence is
    repeated in the given DNA sequence.
    '''
    i = 0
    max_count = 0
    current_count = 0

    while i < len(unk_seq): #iterating through the entire seq
        if unk_seq[i:i+len(seq_list[j])] == seq_list[j]:
            current_count += 1
            i += len(seq_list[j]) #go to the end of str

        else:
            max_count = max(max_count, current_count)
            current_count = 0
            i += 1 #move just one step

    max_count = max(max_count, current_count) #gives max repetitions
    return(max_count)

def modify_data_base(data_base):
    '''
    modifies the csv database by removing the names and making
    a new list that contains only names.
    data_base is further modified to contain numbers in the form
    of integers in place of strings.
    '''
    #making a new database with only integers
    data_base.remove(data_base[0]) #removing the first row

    names = [] #new list that contains only names

    for row in data_base:
        for item in row:
            if item.isalpha(): 
                names.append(item) #adding names to new list
                row.remove(item) #removing names from the original db
    
    #names = ['Alice', 'Bob', 'Charlie']
    #data_base = [['5', '2', '8'], ['3', '7', '4'], ['6', '1', '5']]

    int_database = [] #database with only integers
    for list in data_base:
        int_list = [int(x) for x in list] #each str converted to int
        int_database.append(int_list)

    #int_database - [[5, 2, 8], [3, 7, 4], [6, 1, 5]]
 
    return(data_base, names, int_database)


def sq_in_database(data_base, unk_seq):
    '''

    '''
    seq_list = [] #making a new list containing the STRs only
    for str_seq in data_base[0]:
        seq_list.append(str_seq)

    max_list = []
    for str in range(len(seq_list)):
        str_count = count_repetitions(unk_seq, seq_list, str)
    #calling the function until the full database is checked

        max_list.append(str_count) #a list with the max occurences of STRs

    mod_db, s_names, int_db = modify_data_base(data_base)

    #names - a separate database with all the names
    #data_base - the data base only contains numbers as strings
    
    match_found = False

    for row in range(len(int_db)):
        if max_list == int_db[row]:
            print(f"Found match: {s_names[row]}")
            match_found = True
    
    if match_found == False:
        print("No Match")
    
    
    return()



def main():
    sq_file = input("Sequence file: ")
    
    #once the file is retreived, time to read the file
    l_sq_file = read_unk_sequence(sq_file)
    #print(l_sq_file) #test to see that file is retrieved

    dna_db = read_csv("dna_db.csv")
    #print(dna_db) 

    match = sq_in_database(dna_db, l_sq_file)



if __name__ == "__main__":
    main()

    