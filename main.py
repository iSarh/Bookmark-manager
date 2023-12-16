#Empity List To Fill Later
webs =[]

maxnumWebs = 5  # Maxmum Allowed Website

while maxnumWebs > 0:

    #Input The New Website
    web = input("Enter Wepsite Name Without https:// : ")

    #Add The New Website To The list (webs[])
    webs.append(f"https://{web.strip().lower()}")

    #Decrease 1 from Allowed Websits
    maxnumWebs-= 1 # maxmumWebs = maxmumWebs - 1

    #Print Add Message
    print(f"Website Add, {maxnumWebs} Places left")

    #Print List
    print(webs)

else:
    print()
    print("Bookmarks Is Full, You Can't Add More")

print("")

#Check If List Not Empty
if  len(web) > 0 :

    #Sort The List
    webs.sort()

    index = 0

    print("Tle list Of Website In your Bookmark:")

    while index < len(webs):

        print(f"{webs[index]}")

        index += 1

