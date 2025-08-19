from flask import request,jsonify,json
from modules.reserve import Reserve
from datetime import datetime,timedelta
import os

# Get user and court data to create book details table  
def addBookingDetails(court,user):
  
 # open booking component and add book details in table from court and user parameters 
 with open ("templates/components/booking.html","r") as file:
         content = file.read()
         for i in court:
            if i == "name" or i == "sport" or i=="img" or i =="address" or i=="price":

              # replace key in html file i by its value
              content = content.replace(f"$${i}$$", str(court[i]))

         for j in user:
            if   j == "email" or j == "username" or j=="phone" :  

              content = content.replace(f"$${j}$$", user[j])
         return content
 
# Create reserve button element
def reserve_element(dic,time,date):
    #  check if the element created for logged user or this element is used by another user
     is_user = dic["user"]
     is_court = dic["playground"]

    #  check if this time is available for the court 
     is_reserved = dic["reserved"]

     start_time = datetime.strptime(time,"%H:%M")

    # end time = start + 2 hours 
     end_time =  datetime.strftime (start_time+timedelta(hours=2),"%H:%M")

    #  button html element
     button =''
  
     if not is_reserved:
        button= f'<button data-time={time} data-day={date} class="book">Book</button>'
     elif is_reserved and is_user and is_court:
          button= f'<button data-time={time} data-day={date} class="cancel">Cancel</button>'
     else :
        button ="<p class= 'text-red-500 text-sm'>Unavailable</p>"

    # return html element have the time and the court status
     return f"<div class ='flex px-3 rounded-lg items-center justify-between gap-5 py-2  border-b border-zinc-300'><p>{time} - {end_time}</p>{button}</div>"
 
# Generate dates and create tables 
def addDates (book,userId,courtId):
      
      # use generate_dates method from book class 
      generate_dates = book.generate_dates()
      table= '' 

      # create html component depends on day
      for day in generate_dates:
         with open ("templates/components/day.html") as file:
          content= file.read()

          # create day and date first colmun
          day_element = f"<div class= 'h-fit my-auto'><p>{day["day"]}</p> <p>{day["date"]}</p></div>"
          content = content.replace("$$day$$",day_element)
          
          # create available hours for each day
          hours_in_html= ''
         for time in day["hours"]:
           datetime_str = f"{day['date']} {time}"

          #  use method isReservable_at from book class it returns reserve data if court reserved and reserved by user or not
           is_reversable=book.isReservable_at(datetime_str,userId,courtId)

          #  generate html element and add it hours table
           hours_in_html += reserve_element(is_reversable,time,day["date"])
          
          # add hours table to html component
         content = content.replace("$$hours$$",hours_in_html)
         table+=content
      return table

# Function to build booking page dynamically and return it 
def booking():
     try:
      # get user and court ids from request 
      courtId = int(request.args.get("courtId"))
      userId = int(request.args.get("userId"))
     
      # construct reserve class
      book= Reserve(courtId)
      
      # method to get court data
      court = book.get_playground()

      # method to get user data
      user= book.get_user_data(userId)
      
      # function to add booking details table
      addBookingData =  addBookingDetails(court,user)

      # add hours and days table
      table = addDates(book,userId,courtId)

      addBookingData = addBookingData.replace("$$dates$$",table)

      return addBookingData
    
     except:
        return "<p class= 'text-red-500 font-semibold mt-20 h-fit w-fit mx-auto' >Can't found playground</p>"
     
# function to book court 
def create_book():
  
   try:
    # get reserve data from request(time,user id,court id)
    reserve = request.json

    # add reserve to reserve file 
    with open ("json/reserved.json","r") as f:
      content = json.load(f)
      content.append(reserve)

    with open("json/temp_reserved.json","w") as file:
      json.dump(content,file)

    os.replace("json/temp_reserved.json","json/reserved.json")
   
  #  response
    return jsonify({"message":"booked" , "success":True})
   except:
      return jsonify({"message":"Can't make booking" , "success":False})
   

# function to Cancel reserve 
def cancel_book():
     try:
      cancel = request.json

      with open ("json/reserved.json","r") as f:
       content = json.load(f)
       content = [item for item in content if not (item["time"] == cancel["time"] and item["playgroundId"] == cancel["playgroundId"] and item["userId"]== cancel["userId"])]
     
      with open("json/temp_reserved.json","w") as file:
        json.dump(content,file)
      
      os.replace("json/temp_reserved.json","json/reserved.json")
   
      return jsonify({"message":"Book has been canceled" , "success":True})
     except:
       return jsonify({"message":"Can't cancel booking" , "success":False})
   
