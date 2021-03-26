from flask import Flask, jsonify, request
import json

app = Flask(__name__)
#acá agrego variable global
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])

def hello_world():
    return (jsonify(todos))

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data #request es lo que recibo; .data es lo que tengo en el body y accedo a la propiedad donde esta la info
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request.data) #loads convierte json a formato que python entiende (a un diccionario)
    todos.append(decoded_object)#agregar la tarea nueva usando append
    return (jsonify(todos)) 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return (jsonify(todos))#llamo a mi variable global como lista para eliminar el índice que el usuario indique
    
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 3245, debug =  True)