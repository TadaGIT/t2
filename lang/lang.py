from lang.lexer  import VinteumLexer
from lang.parser import VinteumParser

class Lang:
  def __init__(self):
    self.lexer   = VinteumLexer()
    self.parser  = VinteumParser()
    self.version = "0.0.1"