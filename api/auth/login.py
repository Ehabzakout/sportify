from flask import request,jsonify;
import json



# Login function 
def login():
   
   try:

    # get data from request
    user_data= request.json
    if("email" not in user_data or"password" not in user_data ):
      raise ValueError("Missing Data")
    
    # Open users file and get the user if exist
    with open("json/users.json","r") as file:
      users = json.load(file)

    existed_user = None
    for user in users:
      if user["email"] == user_data["email"] and user["password"]== user_data["password"]:
        existed_user = user
        break

    # Return error if user doesn't exist
    if (existed_user is None):
       raise ValueError("Incorrect Credentials")
    
  # Response
    return jsonify({"message":"Logged in successfully","success":True,"data":existed_user}),201
   except ValueError as error:
     return jsonify({"message":str(error) or "Can't login","success":False}),400
   except:
      return jsonify({"message":"Can't login" ,"success":False}),500