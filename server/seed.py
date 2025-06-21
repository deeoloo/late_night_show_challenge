from faker import Faker
from server.app import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import create_app
from werkzeug.security import generate_password_hash
import random

fake = Faker()
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Users
    for _ in range(5):
        user = User(
            username=fake.user_name(),
            password_hash=generate_password_hash("test123")
        )
        db.session.add(user)

    # Seed Guests
    guests = []
    for _ in range(10):
        guest = Guest(name=fake.name(), occupation=fake.job())
        guests.append(guest)
        db.session.add(guest)

    # Seed Episodes
    episodes = []
    for _ in range(5):
        episode = Episode(date=fake.date_this_decade(), number=fake.random_int(min=1, max=100))
        episodes.append(episode)
        db.session.add(episode)

    db.session.commit()

    # Seed Appearances
    for _ in range(15):
        appearance = Appearance(
            guest_id=random.choice(guests).id,
            episode_id=random.choice(episodes).id,
            rating=random.randint(1, 5)
        )
        db.session.add(appearance)

    db.session.commit()
    print("Database seeded successfully.")
