#Exercise 2. Convert previous exercise and add JSON responses and requests
# The goal is to response with a JSON to any GET request. Interpret a JSON POST request
# and interpret the payload. Please keep in mind to set the content type for each GET and POST request.
# It should be set to application/json. Each POST should return with an error_code response:
#     202 accepted,
#     403 forbidden.

from flask import Flask, request, make_response
import json
app = Flask(__name__)

#dodanie tablicy grantsow
grants = []

#POST - dodanie nowego grantsa do listy
@app.route('/add_g', methods=['POST'])
def add_grant():
    grant_json = json.loads(request.get_json())
    try:
        grants.append(grant_json)
        response = {"message":'Grant ' + str(grant_json["name"]) + " zostal dodany", "error_code" : 200}
    except:
        response = {"message": 'Grant ' + str(grant_json["name"]) + " nie zostal dodany", "error_code": 500}
        return make_response(json.dumps(response))
    return make_response(json.dumps(response))

# DELETE - usuniecie wybranego grantsa
@app.route('/delete_g', methods=["DELETE"])
def delete_grant():
    grant_json = request.get_json()
    grant_id = int(grant_json["grant_id"])
    try:
        del grants[grant_id]
        response = {"message":'Grant ' + str(grant_id) + " zostal usuniety", "error_code" : 200}
    except:
        response = {"message": 'Grant ' + str(grant_id) + " nie istnieje", "error_code": 500}
        return make_response(json.dumps(response))
    return make_response(json.dumps(response))

#GET - wyswietlenie listy grantsow
@app.route('/all_g', methods=["GET"])
def grants_list():
    return make_response(json.dumps(grants))

if __name__ == '__main__':
    app.run(port=7001)