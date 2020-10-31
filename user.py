class User():
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def set_selected_secret_santa(self, name):
    self.selected_secret_santa = name
