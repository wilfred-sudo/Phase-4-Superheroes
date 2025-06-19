from flask import Blueprint, jsonify, request, make_response
from app.models import db, Hero, Power, HeroPower
from sqlalchemy.exc import IntegrityError # Imports IntegrityError for unique constraint violations

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return make_response(jsonify({'error': 'Hero not found'}), 404)
    
    return make_response(jsonify(hero.to_dict_with_powers()), 200)

@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return make_response(jsonify([power.to_dict() for power in powers]), 200)

@api.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response(jsonify({'error': 'Power not found'}), 404)
    return make_response(jsonify(power.to_dict()), 200)

@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return make_response(jsonify({'error': 'Power not found'}), 404)

    data = request.get_json()
    
    if not data or 'description' not in data:
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

    try:
        power.description = data['description']
        db.session.add(power)
        db.session.commit()
        return make_response(jsonify(power.to_dict()), 200)
    except ValueError as e:
        db.session.rollback()
        return make_response(jsonify({"errors": ["validation errors"]}), 400)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"errors": ["validation errors"]}), 400)


@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    if not data:
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if not all([strength, power_id, hero_id]):
        return make_response(jsonify({"errors": ["validation errors"]}), 400)

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero:
        return make_response(jsonify({"error": "Hero not found"}), 404)
    if not power:
        return make_response(jsonify({"error": "Power not found"}), 404)

    try:
        hero_power = HeroPower(
            strength=strength,
            hero_id=hero_id,
            power_id=power_id
        )
        db.session.add(hero_power)
        db.session.commit()
        
        return make_response(jsonify(hero_power.to_dict_nested_hero_power()), 201)

    except ValueError as e:
        db.session.rollback()
        return make_response(jsonify({"errors": ["validation errors"]}), 400)
    except IntegrityError: # Catch unique constraint violation
        db.session.rollback()
        return make_response(jsonify({"errors": ["validation errors"]}), 400)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({"errors": ["validation errors"]}), 400)