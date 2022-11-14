def create_function(a: int) -> callable:
  ...


f1 = create_function(3)
assert f1(5) == 8
assert f1(5) == 8
assert f1(10) == 13

f2 = create_function(100)
assert f2(13) == 113
