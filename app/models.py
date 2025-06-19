from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    hero_powers = db.relationship(
        'HeroPower',
        backref='hero',
        cascade="all, delete-orphan",
        lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }

    def to_dict_with_powers(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "hero_powers": [hp.to_dict_nested_power() for hp in self.hero_powers]
        }

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)

    @validates('description')
    def validate_description(self, key, description):
        if not description:
            raise ValueError("Description must be present.")
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    @validates('strength')
    def validate_strength(self, key, strength):
        valid_strengths = ['Strong', 'Weak', 'Average']
        if strength not in valid_strengths:
            raise ValueError(f"Strength must be one of {', '.join(valid_strengths)}")
        return strength

    __table_args__ = (
        db.UniqueConstraint('hero_id', 'power_id', name='_hero_power_uc'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id
        }

    def to_dict_nested_hero_power(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "hero": self.hero.to_dict(),
            "power": self.power.to_dict()
        }

    def to_dict_nested_power(self):
        return {
            "hero_id": self.hero_id,
            "id": self.id,
            "power": self.power.to_dict(),
            "power_id": self.power_id,
            "strength": self.strength
        }