
# coding: utf-8

# In[ ]:

# There should be a description here.

# ZodiacSetup will do all the opening, loading, and closing of files/data
# It will return ZodiacListTemp
def ZodiacSetup():
    # Open the zodiac descriptions file
    ZodiacText = open('zodiacDescriptions.txt','r')

    # Read the file. We are going to make a list with each line of the file
    # as a list item
    ZodiacListTemp = []
    for animal in ZodiacText: 
        if animal != '\n':
            ZodiacListTemp.append(line)
        
    # Close the file as soon as we are done with it
    ZodiacText.close()
    
    return ZodiacListTemp

# ZodiacCalculation will collect a birth year and determine the Chinese zodiac animal and then display it. With error trapping.
# It will return the birthYear
def ZodiacCalculation():
    # Ask the user for input
    # We're Just going to assign a variable for moment. Come back later.

    try: 
        birthYear = int(input("What year were you born? "))
        # Do some fancy figuring stuff out (little bit of math)
        zodiacIndex = (birthYear-4) % 12
        # Tell user the result
        print("Your Chinese Zodiac Animal is a ", ZodiacList[zodiacIndex])

    except ValueError:
        print("You did not provide a year in the form of an integer")
        
    return birthYear

# Repeat
ZodiacList = ZodiacSetup()

birthYear = 0
while type(birthYear) is int:
    birthYear = ZodiacCalculation()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



