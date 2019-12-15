#Exercise 1. Create a REST API routing map for grants
# Just to point out a few features:
#    the application should accept POST data to add to the grants variable,
#    set routes to get the data about grants by id via GET method,
#    set routes to get the list of grants via GET method,
#    set routes to delete a grant by id via DELETE method.

from flask import Flask, request, make_response

app = Flask(__name__)

#dodanie tablicy grantsow
grants = []

#POST - dodanie nowego grantsa do listy
@app.route('/add_g', methods=['POST'])
def add_grant():
    grant = {"name": request.values["name"],
             "description": request.values["description"],
             "price": request.values["price"],
             "grant_id": request.values["grant_id"]}
    try:
        grants.append(grant)
        response = 'Grant ' + str(grant["name"]) + " zostal dodany"
    except:
        response = 'Grant ' + str(grant["name"]) + " nie zostal dodany"
        return make_response(response)
    return make_response(response)

#DELETE - usuwanie wybranego grantsa
@app.route('/delete_g', methods=["DELETE"])
def delete_grant():
    grant_id = int(request.values["grant_id"])
    try:
        del grants[grant_id]
        response = 'Grant ' + str(grant_id) + " zostal usuniety"
    except:
        response = 'Grant ' + str(grant_id) + " nie istnieje"
        return make_response(response)
    return make_response(response)

#GET wyswietlajacy wszystkie grantsy
@app.route('/all_g', methods=["GET"])
def grants_list():
    return make_response(str(grants))

if __name__ == '__main__':
    app.run(port=7001)