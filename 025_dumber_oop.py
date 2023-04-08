class App:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return "The name is " + self.name + "and the version is " + str(self.version)

class Apps:
    def __init__(self):
        self.apps = []
    
    def add_app(self, app):
        if(isinstance(app, App)):
            self.apps.append(app)
        else:
            print("app argument must be an App object")
    
    def print(self):
        for app in self.apps:
            print(app.name, "(", app.version, ")")
    
    def __str__(self):
        result = ""
        for app in self.apps:
            result = result + app.name + " "
        
        return result
    
    def __len__(self):
        return len(self.apps)

    def __contains__(self, name):
        for app in self.apps:
            if app.name == name:
                return True
        return False

# abc = App("Python", 1)
apps = Apps()
apps.add_app(App("ScreenFlow", 1))
apps.add_app(App("Snagit", 2))

print("Snagit``````````" in apps)

apps()
