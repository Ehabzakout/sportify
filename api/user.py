from flask import request,jsonify,json
import os


# get user data
def get_user_info (id):
    try:
     with open("json/users.json","r") as f:
        users = json.load(f)
        [user] = [user for user in users if user["id"] == id]
     return jsonify({"message":"get user data","success": True,"user":user}),200
 
    except:
       return jsonify({"message":"Can't get user data","success": False}),404
    
# Update user password
def update_user_password():

   try: 
     data = request.json
     with open("json/users.json","r") as f:
        users = json.load(f)
        found= False

      # find user and update password
        for user in users:
           if user["id"] == data["id"]:
              user["password"]= data["password"]
              found =True

        if not found: raise ValueError( "User not found")
   
   #  update users file after update
     with open("json/temp_users.json","w") as f:
        json.dump(users,f)

     os.replace("json/temp_users.json","json/users.json")
     
   #   response
     return jsonify({"message":"password updated successfully","success": True,"user":data}),200
   except ValueError as err:
    return jsonify({"message":str(err) or"Can't update password" ,"success": False}),404
   
   except :
       return jsonify({"message":"Can't update password" ,"success": False}),409
    
# Delete user 
def delete_user_account(id):
    try:
     with open("json/users.json","r") as f:
        users = json.load(f)
        users = [user for user in users if user["id"] != id]
     with open ("json/temp_users.json","w") as f:
         json.dump(users,f)
     os.replace("json/temp_users.json","json/users.json")  
     return jsonify({"message":"user deleted","success": True}),200
 
    except:
       return jsonify({"message":"Can't delete user","success": False}),404
    