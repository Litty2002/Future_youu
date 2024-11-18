import json

class Users:
    def __init__(self) -> None:
        self._mem = {}
        self._file = 'login_info.json'

    def __enter__(self):
        users = Users()
        with open(self._file) as f:
            users._mem = json.load(f)
        return users
    
    def __exit__(self, type, value, traceback):
        pass

    def add_user(self, username, password):
        self._mem[username] = password

        with open(self._file, 'w') as f:
            json.dump(self._mem, f)

    def check_user(self, username, password):
        if username not in self._mem:
            return False
        if self._mem[username] != password:
            return False
        return True
