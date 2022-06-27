import requests
from http import HTTPStatus
from os import access
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource