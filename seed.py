from app import create_app
from app.models import db, Hero, Power, HeroPower

app = create_app()

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        h1 = Hero(name='Kamala Khan', super_name='Ms. Marvel')
        h2 = Hero(name='Doreen Green', super_name='Squirrel Girl')
        h3 = Hero(name='Gwen Stacy', super_name='Spider-Gwen')
        h4 = Hero(name='Janet Van Dyne', super_name='The Wasp')
        h5 = Hero(name='Wanda Maximoff', super_name='Scarlet Witch')
        h6 = Hero(name='Carol Danvers', super_name='Captain Marvel')
        h7 = Hero(name='Jean Grey', super_name='Dark Phoenix')
        h8 = Hero(name='Ororo Munroe', super_name='Storm')
        h9 = Hero(name='Kitty Pryde', super_name='Shadowcat')
        h10 = Hero(name='Elektra Natchios', super_name='Elektra')
        
        heroes_list = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]
        db.session.add_all(heroes_list)
        db.session.commit()

        p1 = Power(name='super strength', description='gives the wielder super-human strengths')
        p2 = Power(name='flight', description='gives the wielder the ability to fly through the skies at supersonic speed')
        p3 = Power(name='super human senses', description='allows the wielder to use her senses at a super-human level')
        p4 = Power(name='elasticity', description='can stretch the human body to extreme lengths')

        powers_list = [p1, p2, p3, p4]
        db.session.add_all(powers_list)
        db.session.commit()

        hero_powers_data = [
            HeroPower(hero=h1, power=p2, strength='Strong'),
            HeroPower(hero=h3, power=p1, strength='Average'),
            HeroPower(hero=h2, power=p1, strength='Strong'),
            HeroPower(hero=h2, power=p3, strength='Weak'),
            HeroPower(hero=h4, power=p2, strength='Average'),
            HeroPower(hero=h5, power=p1, strength='Strong'),
            HeroPower(hero=h6, power=p2, strength='Strong'),
            HeroPower(hero=h7, power=p3, strength='Strong'),
            HeroPower(hero=h8, power=p4, strength='Average'),
            HeroPower(hero=h9, power=p1, strength='Weak'),
            HeroPower(hero=h10, power=p3, strength='Strong')
        ]

        db.session.add_all(hero_powers_data)
        db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
     seed_database()