from flask import Blueprint, jsonify, request
from src.main.factories.calculator4_factory import calculator4_factory
from src.errors.error_controler import handle_errors

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        calc = calculator4_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except Exception as  exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]