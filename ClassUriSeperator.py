
class UriSeperator:
    def __init__(self):  # base values
        self.ErrorUri = ["Invalid", "Uri"]
        self.ErrorParameters = ["Invalid", "Parameters"]
        self.ErrorPath = ["Invalid", "Path"]
        self.ErrorScheme = ["Invalid", "Scheme"]
        self.hasParameters = [False, False, False]
        self.parameters = []
        self.CheckPath = ["login", "confirm", "sign"]

    def default(self):  # Return default setting
        self.hasParameters = [False, False, False]
        self.parameters = []

    def parse(self, string):  # Seperates uri to Scheme, Path and list of parameters.
        self.default()  # resets starting values
        stringparts = string.split(":")  # actual parsing
        try:
            scheme = stringparts[0]
            if scheme != "visma-identity":  # first check to uri, Scheme
                return self.ErrorScheme
            stringparts = stringparts[1].split("/")
            stringparts = stringparts[-1].split("?")
            path = stringparts[0]   # path
            if path not in self.CheckPath:  # second check to uri, path
                return self.ErrorPath
            stringparts = stringparts[-1].split("&")
            for index in stringparts:  # for any amount of parameters
                parameter = index.split("=")
                if parameter[0] == "source":  # checks that which required parameters are true.
                    self.hasParameters[0] = True
                    self.parameters.append(parameter[-1])
                elif parameter[0] == "paymentnumber":
                    self.parameters.append(int(parameter[-1]))
                    self.hasParameters[1] = True
                elif parameter[0] == "documentid":
                    self.hasParameters[2] = True
                    self.parameters.append(parameter[-1])
                else:
                    self.parameters.append(parameter[-1])
        except IndexError:
            return self.ErrorUri  # Error code
        if (path == self.CheckPath[0] or (path == self.CheckPath[1] and self.hasParameters[1]) or (path == self.CheckPath[2] and self.hasParameters[2])) and self.hasParameters[0]:
            return path, self.parameters  # return Scheme incase someone wants them all by using this function.
        return self.ErrorParameters  # Returns error incase uri doesn't go through
