import cipher

class CaesarCipher(cipher.Cipher):
  """Another substitution cipher where the encrypted message is found by looking up each letter and finding the corresponding letter in a shifted alphabet."""

  def __init__(self, shift):
      """Initializes the alphabet and sets the shift value."""
      super().__init__()
      if shift < 0 or shift > 25:
          raise ValueError("Shift value must be between 0 and 25.")
      self._shift = shift
  
  def _encrypt_letter(self, letter): 
      """Looks up letter in alphabet, returns encrypted letter in the shifted alphabet."""
      location = self._alphabet.index(letter.upper())
      encrypted_location = (location + self._shift) % 26 
      return self._alphabet[encrypted_location]
  
  def _decrypt_letter(self, letter): 
      """Looks up letter in shifted alphabet, returns decrypted letter in the alphabet."""
      location = self._alphabet.index(letter.upper())
      decrypted_location = (location - self._shift + 26) % 26  
      return self._alphabet[decrypted_location]
  