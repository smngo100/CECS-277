import cipher

class AtbashCipher(cipher.Cipher): 
  """A substitution cipher where the encrypted message is obtained by looking up each letter and finding the corresponding letter in a reversed alphabet."""

  def _encrypt_letter(self, letter):
      """Looks up letter in alphabet, returns encrypted letter in the cipherbet."""
      location = self._alphabet.index(letter.upper())
      return self._alphabet[::-1][location]

  def _decrypt_letter(self, letter):
      """Looks up letter in cipherbet, returns decrypted letter in the alphabet."""
      location = self._alphabet[::-1].index(letter.upper())
      return self._alphabet[location]
