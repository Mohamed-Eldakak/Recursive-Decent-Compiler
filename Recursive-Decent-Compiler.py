import re
class Compiler:
  def __init__(self):
    self.tokens = []
    self.current_token = None
    self.index = 0
    self.output = []

  def tokenize(self, input_string):
    self.tokens = re.findall(r'\w+|[^\s\w]', input_string)
    self.current_token = self.tokens[self.index]


  def match(self, expected_token):
    if self.current_token == expected_token:
      self.index += 1
      if self.index < len(self.tokens):
        self.current_token = self.tokens[self.index]
      else:
        self.current_token = None
    else:
      raise Exception(f'Error: Expected {expected_token}, got{self.current_token}')

  def V(self):
    self.output.append(f'LIT {self.current_token}')
    self.match(self.current_token)

  def C(self):
    self.output.append(f'LIT {self.current_token}')
    self.match(self.current_token)

  def F(self):
    if self.current_token == '(':
      self.match(self.current_token)
      self.E()
      self.match(self.current_token)
    elif re.match(r'\d+', self.current_token):
      self.C()
    elif re.match(r'\w+', self.current_token):
      self.V()
      self.output.append('LOAD')

  def T(self):
      self.F()
      while self.current_token == '*' or self.current_token == '/':
          if self.current_token == '*':
              self.match(self.current_token)
              self.F()
              self.output.append('MUL')
          else:
              self.match(self.current_token)
              self.F()
              self.output.append('DIV')

  def E(self):
      if self.current_token == '-':
        self.match(self.current_token)
        self.T()
        self.output.append('NEG')
      else:
        self.T()
      while self.current_token == '-' or self.current_token == '+':
          if self.current_token == '+':
              self.match(self.current_token)
              self.T()
              self.output.append('ADD')
          else:
              self.match(self.current_token)
              self.T()
              self.output.append('SUB')


  def A(self):
        self.V()
        if self.current_token == '=':
          self.match(self.current_token)
        else:
          print("error")
          return
        self.E()
        self.output.append('STORE')

  def compile(self,string):
      self.tokenize(string)
      self.A()

def main():
  compiler = Compiler()
  input_string = input()
  compiler.compile(input_string)
  output_string = " ".join(compiler.output)
  print(output_string)

if __name__ == '__main__':
  main()
