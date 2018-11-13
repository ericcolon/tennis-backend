# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    index.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pleroux <pleroux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/13 10:40:23 by pleroux           #+#    #+#              #
#    Updated: 2018/11/13 15:57:03 by pleroux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from src.predict import predict
import sys

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api.add_resource(predict, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)
