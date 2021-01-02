import ast

class loginData():
    def __init__(self):
        self.data = userdata()
        self.listusername = self.data.data
    def login(self,username,password):
        if username in self.listusername:
            logindata = self.data.get(username)
            if logindata['password'] == password:
                return 'Login successfully'
            else:
                return 'Wrong password'
        else:
            return 'Username not exist'
    def register(self,username,password):
        if username in self.listusername:
            return 'Username already existed'
        else:
            self.data.update(username,password,100000, {})
            data_history = open('data/' + username + '.txt', 'w')
            history = ['','','','','','']
            data_history.write(str(history))
            return 'Register successfully'

class userdata():
    def __init__(self):
        get = open("data/userdata.txt")
        self.data = ast.literal_eval(get.read())
        get.close()
    def update(self, username, password, money, items):
        self.data[username] = {'password': password, 'name': username, 'money': money, 'items': items}
        update = open('data/userdata.txt', 'w')
        update.write(str(self.data)) 
        update.close()
    def get(self, username):
        return self.data[username]
    def history(self, username):
        data = open('data/' + username + '.txt')
        return ast.literal_eval(data.read())
    def update_history(self, username, history_data):
        get = open('data/' + username + '.txt')
        data = ast.literal_eval(get.read())
        get.close
        for i in range(len(data)-1):
            data[-i-1] = data[-i-2]
        data[0] = history_data
        update = open('data/' + username + '.txt', 'w')
        update.write(str(data))
        update.close()
