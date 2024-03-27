class CommandBuilder:
  def __init__(self):
    self.reset()

  def reset(self):
    self.command = ["java", "-jar", "ili2pg-4.4.4.jar"]

  def setAction(self, action):
    self.command.append(action)
    return self

  def setDbCredentials(self, host, port, user, pwd, database, schema):
    self.command.extend(["--dbhost", host, "--dbport", port, "--dbusr", user, "--dbpwd", pwd, "--dbdatabase", database, "--dbschema", schema])
    return self

  def setModel(self, modeldir, models):
    self.command.extend(["--modeldir", modeldir, "--models", models])
    return self

  def addFlags(self, flags):
    for flag in flags:
      self.command.append(flag)
    return self

  def addKeyValuePairs(self, keyValuePairs):
    for key, value in keyValuePairs.items():
      self.command.extend([key, value])
    return self

  def build(self):
    command_to_execute = self.command
    self.reset()  
    return command_to_execute