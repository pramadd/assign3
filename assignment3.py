sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']




#sI = 45
#mI = 100


for i in range(45,100):
    if(i >= 100):
        print "that a big number!"
    if(i < 100):
        print "that a small number"

#Integer        


#mL = [3,5,7,34,3,2,113,65,8,89]

for x in mL:
    if(x >= 100):
        print "bigger than 100"
    else :
        print "lesser than 100"    
# prints the given value is bigger or lesser than 100 

#--------------------------------------------------------------------------

#string
#bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."

for length in bS:
    if(len(bS)>5):
        print "Long sentence."
    else:
        print "short sentence."  

#-------------------------------------------------------------------------------

#list
#spL = ['name','address','phone number','social security number']


for length in spL:
    if(len(spL)>=10):
        print "Big List"
    else:
        print "short list"    
