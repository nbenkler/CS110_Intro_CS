#Program asks how much one wants to lift and the weight of the bar one is using, and tells them what weights to use and how many
#Noam Benkler
#1/20/18

def main():

    barText = input("what is the weight of your bar? ")
    bar = int(barText)
    weightText = input("how much do you want to lift in total? ")
    weight = int(weightText)
    
    lbadd = weight - bar
    bside = lbadd/2
    
    plates = (45,35,25,15,10,5,2.5,1,0.5)
    for i in plates:
        if i <= bside:
            print ("Place " + str(2*(bside/i)) + " " + str(i) + "lbs weights on the bar")
            bside = bside%i
    
main()