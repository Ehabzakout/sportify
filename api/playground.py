import json 
from flask import jsonify,request

# Get playgrounds compatible with search value
def get_playgrounds():
    try:
        category= request.args.get("search")or "".strip().lower()

        # open playgrounds file
        with open("json/playground.json","r") as file :
             playgrounds = json.load(file)
             
             if(category ==""):
               return jsonify({"message":"success","success":True,"data":playgrounds}),200
             
            #  get playgrounds depends on sport search
             playgrounds = [item for item in playgrounds if category in item.get("sport", "").lower()  ]
            
            # response
             if(not len(playgrounds)>0):  return jsonify({"message":"There are no sports to match","success":True,"data":[]}),200
             return jsonify({"message":"get playgrounds","success":True,"data":playgrounds}),200
    except :
      return jsonify({"message":"Can't get playgrounds" ,"success":False}),500

