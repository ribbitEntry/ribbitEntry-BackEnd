from flask_restful import Resource
from flask import request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from server.docs.myPage.color import COLOR_POST
from server.extensions import db
from server.model.user import User


class Color(Resource):

    @swag_from(COLOR_POST)
    @jwt_required
    def post(self, userId):
        color = request.json['color']

        if color:
            user = User.query.filter(User.id == userId).first()
            user.theme_color = color
            db.session.commit()
            return {'color': user.theme_color}, 200
        else:
            return jsonify({'status': 'JWT 인증에 실패하였거나 색상코드가 없습니다.'}, 400)
