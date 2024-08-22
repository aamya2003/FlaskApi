from flask import Flask, request

api_server = Flask(__name__)

users = {
    '1233':{
         "name": "Ahmed",
         "age": 21,
         "live": "iraq",
         "skills": ['py']},

     "121":{
         "name": "ALi",
         "age": 19,
         "live": "iraq",
         "skills": ['js', "css"]
   },
     "4321":{
         "name": "blab",
         "age": 30,
         "skilss": ['php', "html"]
   }
}


@api_server.route("/get_users")
def getUsers():
    user_id = request.args.get("user_id")
    return users.get(user_id, {"error" : "We don't 've This user_id"})





api_server.run(host='0.0.0.0')

