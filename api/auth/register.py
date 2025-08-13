from flask import request,jsonify;
import json



def register():
   try:
    with open("json/users.json","r") as file:
      users = json.load(file)
    user_data= request.json
    
    if("email" not in user_data or "phone" not in user_data  or "password" not in user_data or "username" not in user_data):
      raise ValueError("Missing Data")
    for user in users:
      if user["email"] == user_data["email"]:
        raise ValueError("User already exist")
    id = users[len(users)-1]["id"] + 1 if len(users) > 0 else 1
    user_data["id"] = id
    users.append(user_data)

   
    with open("json/users.json","w") as file:
      json.dump(users,file)
      return jsonify({"message":"User Created successfully","success":True}),201
   except ValueError as error:
  
     return jsonify({"message":str(error) or "Can't add user","success":False}),400
   except:
      return jsonify({"message":"Can't Register" ,"success":False}),500