
from app.database import DB

class SampleTable(DB.Model):
    id = DB.Column( DB.Integer, primary_key=True)
    inserted_at = DB.Column(DB.DateTime)
    message = DB.Column(DB.String(250))

    def __init__(self, id, val):
        self.id = id
        self.value = val
        self.inserted_at = "now()"

    def __repr__(self):
        return '<Search id={},  inserted_at={}, value={}'.format(self.id, self.inserted_at, self.value)
