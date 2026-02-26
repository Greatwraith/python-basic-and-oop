# with the Continue statement,
# we can stop the currenct iteration of the loop, and Continue with the next. 





ShopChart = ["apple", "banana", "grape", "orange"]

for iterates_it in ShopChart:
    if iterates_it == "grape":
        continue
    print(iterates_it)

    
# it tells, when it meets "grape". ignore the "grape" and iterate next elements after "grape"


