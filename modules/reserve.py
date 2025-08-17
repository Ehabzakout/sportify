import json
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
   
   def generate_dates():
      pass

   def reserve_at(time):
      pass 

   def isReservable_at(time):
      pass

   def cancel_reserve():
      pass

  
      