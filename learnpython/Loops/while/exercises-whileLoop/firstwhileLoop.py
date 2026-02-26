

def attemps(input):
    percobaan = 0
    while percobaan <= input:
        print("Attemps: " + str(percobaan))
        percobaan += 1
        # percobaan = percobaan + 1 (alternatif)
        
    # for last attemps prints, put it here. sejajar dengan garis w pada while
    print("Attemps: " + str(percobaan)) 
    print("Last attemps is: " + str(percobaan) + "(last)")
    
    
attemps(4)      