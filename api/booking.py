from flask import request,jsonify,json
from modules.reserve import Reserve
from datetime import datetime,timedelta
import os

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
 
def reserve_element(dic,time,date):
     is_user = dic["user"]
     is_court = dic["playground"]
     is_reserved = dic["reserved"]
     button =''
    
     if not is_reserved:
        button= f'<button data-time={time} data-day={date} class="book">Book</button>'
     elif is_reserved and is_user and is_court:
          button= f'<button data-time={time} data-day={date} class="cancel">Cancel</button>'
     else :
        button ="<p class= 'text-red-500 text-sm'>Unavailable</p>"
     return f"<div class ='flex px-3 rounded-lg items-center justify-between gap-5 py-2  border-b border-zinc-300'><p>{time} - { datetime.strftime (datetime.strptime(time,"%H:%M")+timedelta(hours=2),"%H:%M")}</p>{button}</div>"
 

def addDates (book,userId,courtId):
      generate_dates = book.generate_dates()
      table= '' 
      for day in generate_dates:
         with open ("templates/components/day.html") as file:
          content= file.read()
          day_element = f"<div class= 'h-fit my-auto'><p>{day["day"]}</p> <p>{day["date"]}</p></div>"
          content = content.replace("$$day$$",day_element)
          hours_in_html= ''
         for time in day["hours"]:
           datetime_str = f"{day['date']} {time}"
           is_reversable=book.isReservable_at(datetime_str,userId,courtId)
           hours_in_html += reserve_element(is_reversable,time,day["date"])
         content = content.replace("$$hours$$",hours_in_html)
         table+=content
      return table

def booking():
     try:
      courtId = int(request.args.get("courtId"))
      userId = int(request.args.get("userId"))
      book= Reserve(courtId)
      court = book.get_playground()
      user= book.get_user_data(userId)
      addBookingData =  addBookingDetails(court,user)
      table = addDates(book,userId,courtId)
      addBookingData = addBookingData.replace("$$dates$$",table)
      return addBookingData
     except:
        return "<p class= 'text-red-500 font-semibold mt-20 h-fit w-fit mx-auto' >Can't found playground</p>"
     

def create_book():
  
   try:
    reserve = request.json
    with open ("json/reserved.json","r") as f:
      content = json.load(f)
      content.append(reserve)
    with open("json/temp_reserved.json","w") as file:
      json.dump(content,file)
    os.replace("json/temp_reserved.json","json/reserved.json")
   
    return jsonify({"message":"booked" , "success":True})
   except:
      return jsonify({"message":"Can't make booking" , "success":False})
   

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
   
