from typing import Tuple

GOOD_PRIME = 1 + 407 * ( 1 << 119 )

def xgcd( x: int, y: int ) -> Tuple[int, int, int]:
    """
    Extendend Euclidean Algorithm 
    Returns: `(a,b,g) => a * x + b * y = g` `g` is greates common divisor
    """
    old_r, r = (x, y)
    old_s, s = (1, 0)
    old_t, t = (0, 1)

    while r != 0:
        quotient = old_r // r
        old_r, r = (r, old_r - quotient * r)
        old_s, s = (s, old_s - quotient * s)
        old_t, t = (t, old_t - quotient * t)

    return old_s, old_t, old_r # a, b, g

class F:

  @staticmethod
  def WithPrime(p: int = GOOD_PRIME):
      return lambda x: F(p,x)

  def __init__(self, p: int, value: int):
    """ `p` - prime number"""
    self.p = p
    self.value = value
  
  def zero(self):
    return F(self.p, 0)

  def one(self):
    return F(self.p, 0)
  
  def __add__(self, right):
    return F(self.p, (self.value + right.value) % self.p)

  def __mul__( self, right ):
      return F(self.p, (self.value * right.value) % self.p)

  def __sub__( self, right ):
      return F(self.p, (self.p + self.value - right.value) % self.p)

  def __truediv__( self, right ):
      return self * right.inverse()

  def __neg__( self ):
      return F(self.p, (self.p - self.value) % self.p)

  def inverse( self ):
      (a,b,g) = xgcd(self.value, self.p)
      return F(self.p, a)

  # modular exponentiation -- be sure to encapsulate in parentheses!
  def __xor__( self, exponent ):
      acc = F(self.p, 1)
      val = self
      for i in reversed(range(len(bin(exponent)[2:]))):
          acc = acc * acc
          if (1 << i) & exponent != 0:
              acc = acc * val
      return acc

  def __eq__( self, other ):
      return self.value == other.value

  def __neq__( self, other ):
      return self.value != other.value

  def __str__( self ):
      return str(self.value)

  def __bytes__( self ):
      return bytes(str(self).encode())

  def is_zero( self ):
      if self.value == 0:
          return True
      else:
          return False

  def sub_group_generator(self, n):
      assert(self.p == GOOD_PRIME), f"Only prime {GOOD_PRIME} supported"
      assert(n <= 1 << 119 and (n & (n-1)) == 0), "Field does not have generator for subgroup where n > 2^119 or not power of two."

      root = F(self.p, 85408008396924667383611388730472331217)
      order = 1 << 119
      while order != n:
          root = root^2
          order = order/2
      return root
   
  def generator(self):
    assert(self.p == GOOD_PRIME), "Do not know generator for other fields beyond 1+407*2^119"
    return F(self.p,85408008396924667383611388730472331217)

  def sample():
      acc = 0
      for b in byte_array:
          acc = (acc << 8) ^ int(b)
      return F(self.p, acc % self.p)

