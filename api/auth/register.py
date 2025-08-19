from flask import request,jsonify;
import json
import os

# Register new user
def register():
   try:
    # Get users from users file

    with open("json/users.json","r") as file:
      users = json.load(file)
    user_data= request.json
    
    # Check if request has all data 
    if("email" not in user_data or "phone" not in user_data  or "password" not in user_data or "username" not in user_data):
      raise ValueError("Missing Data")
    
    # check if user exist before
    for user in users:
      if user["email"] == user_data["email"]:
        raise ValueError("User already exist")
      
    # generate user id
    id = users[len(users)-1]["id"] + 1 if len(users) > 0 else 1
    user_data["id"] = id
    
    # add id to user data
    users.append(user_data)
   
  # Create temp file and write new data
    with open("json/temp_users.json","w") as file:
      json.dump(users,file)
     
  # Delete temp file and replace old file with the new one 
    os.replace("json/temp_users.json","json/users.json")

  # response
    return jsonify({"message":"User Created successfully","success":True}),201
   except ValueError as error:
  
     return jsonify({"message":str(error) or "Can't add user","success":False}),400
   except:
      return jsonify({"message":"Can't Register" ,"success":False}),500