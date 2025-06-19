from marshmallow import Schema, fields

class HeroSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    super_name = fields.Str()

class PowerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()

class HeroPowerSchema(Schema):
    id = fields.Int()
    hero_id = fields.Int()
    power_id = fields.Int()
    strength = fields.Str()
