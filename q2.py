def create_function(a: int) -> callable:
  ...


f = create_function(3)
assert f(5) == 8
