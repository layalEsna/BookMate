# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db, Book, User, Review

# if __name__ == '__main__':
#     fake = Faker()
#     with app.app_context():
#      print("Starting seed...")
#         # Seed code goes here!
#      for _ in range(10):
#         book = Book(
#            title = fake.sentence(nb_words=randint(3,5)),
#            author = fake.name(),
#            published_date = fake.date_this_century()
#         )
#         db.session.add(book)
#         db.session.commit()

#         user = User(
#             username = fake.user_name(),
#             password = fake.password(),
#             email = fake.email()
#         )

#         db.session.add(user)
#         db.session.commit()

#         review = Review(content = fake.text(100),
#                         book_id = book.id,
#                         user_id = user.id
#                         )
#         db.session.add(review)
#         db.session.commit()

    

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!


























# #!/usr/bin/env python3

# # Standard library imports
# from random import randint, choice as rc

# # Remote library imports
# from faker import Faker

# # Local imports
# from app import app
# from models import db

# if __name__ == '__main__':
#     fake = Faker()
#     with app.app_context():
#         print("Starting seed...")
#         # Seed code goes here!
