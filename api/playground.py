import json 
from flask import jsonify,Flask,request

def get_all_playgrounds():
    try:
        category= request.args.get("search").strip().lower()
        with open("json/playground.json","r") as file :
             playgrounds = json.load(file)
             if(category !=""):
               playgrounds = [item for item in playgrounds if item.type == category ]
             if(not len(playgrounds)>0): raise ValueError ("There no sports to show")
             return jsonify({"message":"get playgrounds","success":True,"data":playgrounds}),200
    except ValueError as  error : 
     return jsonify({"message": error or"Can't get playgrounds" ,"success":False}),404
    except :
      return jsonify({"message":"Can't get playgrounds" ,"success":False}),500
