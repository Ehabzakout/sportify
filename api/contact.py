
from flask import request,jsonify,json
import os


def contact ():

    try:
     data = request.json
     with open("json/contact.json") as f:
         content= json.load(f)
         data["id"] = content[len(content) -1]["id"] +1 if len(content)  else 1
         content.append(data)
     with open("temp_contact.json","w") as file :
         json.dump(content,file)

     os.replace("temp_contact.json","json/contact.json")   
     return jsonify({"message":"Thank you for contacting with us","success":True})       
    except:
       return jsonify({"message":"Can't receive your message","success":False}) 

