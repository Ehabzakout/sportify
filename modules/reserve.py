import json
from datetime import datetime,timedelta
class Reserve:
   def __init__(self,courtId):
      self.courtId= courtId
      with open("json/playground.json")as file:
        playgrounds = json.load(file)
      self.playground =  [playground for playground in playgrounds if playground["id"] == self.courtId][0]
     
   def get_user_data(self,id):
       with open ("json/users.json") as f:
        users= json.load(f) 
        user = [user for user in users if user["id"] == id ][0]  

       return user
   
   def get_playground(self):
      return self.playground 
   
   def generate_dates(self):
       dates = []
       start = datetime.now().replace(hour=15,minute=0,second=0, microsecond=0)
       safe_time = datetime.now().replace(minute=0,second=0,microsecond=0) + timedelta(hours=2)
       for day in range(3):
         dic= {"day":"","hours":[],"date":""}
         current =start+ timedelta(days=day)
         dic["date"]= current.strftime("%Y-%m-%d")
         dic["day"]= current.strftime("%A")
         for hour in range(0,9,2):
           slot = current + timedelta(hours=hour)
           if (slot >safe_time):
            dic["hours"].append(slot.strftime("%H:%M"))
         dates.append(dic) 
      
       return dates

   
       

   def reserve_at(self,time):
       
      pass 

   def isReservable_at(self, time,userId,playgroundId):
     with open("json/reserved.json") as f:
        content = json.load(f)
     new_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
     if not len(content): return{"reserved":False,"user":False,"playground": False}
     for reserve in content:
        reserve_time = datetime.strptime(reserve["time"], "%Y-%m-%d %H:%M")
        user = True if reserve["userId"] == userId else False
        playground = True if reserve["playgroundId"] == playgroundId else False
        reserved = True if reserve_time == new_time and playground else False 
        if reserved:
         return {"reserved":reserved,"user":user,"playground": playground}
     return {"reserved":reserved,"user":user,"playground": playground}
     


           
           
      

   def cancel_reserve():
      pass

  
      