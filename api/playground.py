import json 
from flask import jsonify,request

def get_playgrounds():
   
    try:
        category= request.args.get("search")or "".strip().lower()
        with open("json/playground.json","r") as file :
             playgrounds = json.load(file)
             if(category ==""):
               return jsonify({"message":"success","success":True,"data":playgrounds}),200
             playgrounds = [item for item in playgrounds if category in item.get("sport", "").lower()  ]
             if(not len(playgrounds)>0):  return jsonify({"message":"There are no sports to match","success":True,"data":[]}),200
             return jsonify({"message":"get playgrounds","success":True,"data":playgrounds}),200
        

   
    except :
      return jsonify({"message":"Can't get playgrounds" ,"success":False}),500

