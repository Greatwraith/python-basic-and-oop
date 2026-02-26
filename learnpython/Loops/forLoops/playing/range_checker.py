def lets_play(start, EndBefore):
    if not isinstance(start, int) or not isinstance(EndBefore, int):
        print("put numbers vro 🥀")
    else:
        puthere = range(start, EndBefore)  # safe now
        if start >= 0 and EndBefore <= 21:
            for do_it in puthere:
                print(do_it)
        else:
            print("Cannot process")
            
            
            
  # U MUST CHECK THE NUMBERS data type FIRST
    # THEN IF IT'S ACTUAL NUMBERS DO ELSE
    # in else, if the start number is greater than or equal 0 and
    # not greater or atleast equal 21
    # DO the iterate process
    
    # if start less than or not equal 0 AND EndBefore not greater than or equal 21
    # show warning! 
            
            
lets_play(1, 6)       # works normally
lets_play(1, "damn") 
lets_play(-3, 50)


