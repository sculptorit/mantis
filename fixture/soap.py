from suds import WebFault
from suds.client import Client


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def iloginp(self, username, password):
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        result = self.client.service.mc_projects_get_user_accessible(username, password)
        projects = list(map(lambda x: x.id, result))
        return projects
