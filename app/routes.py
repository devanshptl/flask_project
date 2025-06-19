from flask import Blueprint, jsonify
from flask_pydantic import validate
from bson.objectid import ObjectId
from app.database import mongo
from app.schemas import UserInput
from app.models import usermodel

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def get_all_users():
    users = mongo.db.users.find()
    return jsonify([usermodel(user) for user in users]), 200

@user_bp.route("/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(usermodel(user)), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/", methods=["POST"])
@validate()
def create_user(body: UserInput):
    user_id = mongo.db.users.insert_one(body.model_dump()).inserted_id
    user = mongo.db.users.find_one({"_id": user_id})
    return jsonify(usermodel(user)), 201

@user_bp.route("/<id>", methods=["PUT"])
@validate()
def update_user(id, body: UserInput):
    result = mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": body.dict()})
    if result.matched_count:
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        return jsonify(usermodel(user)), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/<id>", methods=["DELETE"])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
