from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class PetOwner(db.Model, SerializerMixin):

    __tablename__ = 'pet_owners'

    id = db.Column(db.Integer, primary_key=True)
    owner_name = db.Column(db.String, nullable=False)
    pet_name = db.Column(db.String, nullable=False)
    pet_type = db.Column(db.String, nullable=False)
    zip_code = db.Column(db.String, nullable=False)  


    pet_sitters = db.relationship('PetSitter', secondary='appointments', back_populates='pet_owners')
    appointments = db.relationship('Appointment', back_populates='pet_owner', cascade='all, delete-orphan')

    serialize_only = ('id', 'owner_name', 'pet_name', 'pet_type')

    @validates('owner_name')
    def owner_name_validate(self, key, owner_name):

        if not owner_name or not isinstance(owner_name, str):
            raise ValueError('Owner name is required and must be type of string.')
        return owner_name
    
    @validates('pet_name')
    def pet_name_validate(self, key, pet_name):

        if not pet_name or not isinstance(pet_name, str):
            raise ValueError('Pet name is required and must be type of string.')
        return pet_name
    
    @validates('pet_type')
    def pet_type_validate(self, key, pet_type):

        if not pet_type or not isinstance(pet_type, str):
            raise ValueError('Pet type is required and must be type of string.')
        return pet_type
    
    @validates('zip_code')
    def zip_code_validate(self, key,zip_code):

        
    
        



    


class PetSitter(db.Model, SerializerMixin):
    # from sqlalchemy import func

    __tablename__ = 'pet_sitters'

    id = db.Column(db.Integer, primary_key=True)
    sitter_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    

    def avg_rating(self):
        from sqlalchemy import func

        rating = db.session.query(func.avg(Appointment.rating)).filter(

            Appointment.pet_sitter_id == self.id).filter(
                Appointment.rating != None).scalar()
        return round(rating, 2) if rating else None
    
    pet_owners = db.relationship('PetOwner', secondary='appointments', back_populates='pet_sitters')
    appointments = db.relationship('Appointment', back_populates='pet_sitter', cascade='all, delete-orphan')
    
    serialize_only = ('id', 'sitter_name', 'location', 'price')

    @validates('sitter_name')
    def sitter_name_validat(self, key, sitter_name):
        if not sitter_name or not isinstance(sitter_name, str):
            raise ValueError('Pet sitter name is required and must be type of string.')
        return sitter_name



        



class Appointment(db.Model, SerializerMixin):

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=True, default=None)

    pet_owner_id = db.Column(db.Integer, db.ForeignKey('pet_owners.id'), nullable=False)
    pet_sitter_id = db.Column(db.Integer, db.ForeignKey('pet_sitters.id'), nullable=False)

    status = db.Column(db.String, nullable=False)


    pet_owner = db.relationship('PetOwner', back_populates='appointments')
    pet_sitter = db.relationship('PetSitter', back_populates='appointments')


    serialize_only = ('id', 'date', 'duration', 'rating', 'status', 'pet_owner_id', 'pet_sitter_id')



# Stop the Server: Press CTRL+C to quit the running Flask server.

# Enable Debug Mode:

# Run:
# bash
# Copy code
# export FLASK_ENV=development
# flask run




 

     
 










# from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy

# from config import db

# # Models go here!
# 