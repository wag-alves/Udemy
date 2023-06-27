class Connection():
    def __init__(self, host='Localhost'):
        self.host = host
        self.name = None
        self.password = None

    def set_user(self, name):
        self.name = name
    
    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


y = Connection()
y.set_user('Wagner')
print(y.name)


x = Connection.create_with_auth('wagner', '1234')
print(x.user)
print(x.password)