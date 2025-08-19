from flask import jsonify;
import json

# Get sports data
def get_sports():
   try:
    with open("json/sports.json","r") as file:
      sports = json.load(file)

    if(not len(sports)>0): raise ValueError ("There no sports to show")
   
  #  Response
    return jsonify({"message":"get sports","success":True,"data":sports}),200
  
   except ValueError as  error : 
     return jsonify({"message": error or"Can't get sports" ,"success":False}),404
  
   except :
      return jsonify({"message":"Can't get sports" ,"success":False}),500