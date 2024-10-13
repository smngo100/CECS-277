class Contact: 
  """ Represents contact information 
  Attributes:
  first_name: first name
  last_name: last name 
  phone: phone number
  address: address 
  city: city 
  zip: zip code
  """
  
  def __init__(self, fn, ln, ph, addr, city, zip):
    """Assigns contact's information to corresponding attribute."""
    self.fn = fn 
    self.ln = ln
    self.ph = ph
    self.addr = addr
    self.city = city
    self.zip = zip

  def __lt__(self, other):
    """Compares two contacts."""
    if self.ln == other.ln:
      return self.fn < other.fn 
    return self.ln < other.ln
    
  
  def __str__(self):
    """Returns string used to display contact."""
    return f"{self.fn}, {self.ln}, {self.ph}, {self.addr},{self.city}, {self.zip}"

  def __repr__(self):
    """Returns string used to write contact."""
    return f"first_name = {self.fn}, last_name = {self.ln}, phone = {self.ph}, address = {self.addr}, city = {self.city}, zip = {self.zip}"