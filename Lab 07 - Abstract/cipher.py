import abc

class Cipher(abc.ABC): 
  """An abstract class that defines the interface of any cipher subclass.
  Attribute: 
  _alphabet (str): a list of letters A-Z"""

  def __init__(self):
    """Initializes the alphabet."""
    self._alphabet = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'

  @property
  def get_alphabet(self):
    """Allows the subclasses to access the alphabet."""
    return self._alphabet                

  def encrypt_message(self, message): 
    """Encrypts a message"""
    encrypted_message = ""
    for char in message: 
        if char.isalpha():
            encrypted_letter = self._encrypt_letter(char.upper())
            if encrypted_letter is not None:
                encrypted_message += encrypted_letter
        else: 
            encrypted_message += char
    return encrypted_message

  def decrypt_message(self, message): 
    """Decrypts a message"""
    decrypted_message = ""
    for char in message: 
        if char.isalpha():
            decrypted_letter = self._decrypt_letter(char.upper())
            if decrypted_letter is not None:
                decrypted_message += decrypted_letter
        else: 
            decrypted_message += char
    return decrypted_message

  @abc.abstractmethod
  def _encrypt_letter(self, letter): 
    """Encrypts a single letter."""
    pass

  @abc.abstractmethod
  def _decrypt_letter(self, letter):
    """Decrypts a single letter."""
    pass
