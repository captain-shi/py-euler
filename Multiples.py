''' ####################################
#################@Captain##############
###################################'''

#Adding multiples of 3 and 5 in a list

Total = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        Total += x
        
print(Total)