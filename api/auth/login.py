from flask import request,jsonify;
import json



def login():
   try:
    user_data= request.json
    if("email" not in user_data or"password" not in user_data ):
      raise ValueError("Missing Data")
    
    with open("json/users.json","r") as file:
      users = json.load(file)

    existed_user = None
    for user in users:
      if user["email"] == user_data["email"] and user["password"]== user_data["password"]:
        existed_user = user
        break
    if (existed_user is None):
       raise ValueError("Incorrect Credentials")
    

    return jsonify({"message":"Logged in successfully","success":True,"data":existed_user}),201
   except ValueError as error:
  
     return jsonify({"message":str(error) or "Can't login","success":False}),400
   except:
      return jsonify({"message":"Can't login" ,"success":False}),500