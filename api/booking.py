from flask import request
from modules.reserve import Reserve


def addBookingDetails(court,user):
    
 with open ("templates/components/booking.html","r") as file:
         content = file.read()
         for i in court:
            if i == "name" or i == "sport" or i=="img" or i =="address" or i=="price":
              content = content.replace(f"$${i}$$", str(court[i]))

         for j in user:
            if   j == "email" or j == "username" or j=="phone" :  

              content = content.replace(f"$${j}$$", user[j])
         return content
def booking():
     try: 
      courtId = int(request.args.get("courtId"))
      userId = int(request.args.get("userId"))
      book= Reserve(courtId)
      court = book.get_playground()
      user= book.get_user_data(userId)
   
      addBookingData =  addBookingDetails(court,user)
      
      return addBookingData
     except:
        return "<p>Can't found playground</p>"