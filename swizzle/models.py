from swizzle import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    match_played = db.Column(db.Integer)
    match_won = db.Column(db.Integer)
    elo = db.Column(db.Integer, default = '1500')

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.elo}','{self.image_file}')"


