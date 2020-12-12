import ast

class loginData():
    def __init__(self):
        self.Read = open("loginData.txt")
        self.data = ast.literal_eval(self.Read.read())
        self.Read.close()
        
    def login(self,username,password):
        if username in self.data:
            if self.data[username] == password:
                return '(login successfully)'
            else:
                return '(wrong password)'
        else:
            return '(username not exist)'
    def register(self,username,password):
        if username in self.data:
            return '(name must be unique)'
        else:
            self.data[username] = password
            index = open("loginData.txt",'w')
            index.write(str(self.data))
            index.close()
            return '(register successfully)'
