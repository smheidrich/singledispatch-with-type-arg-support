from singledispatch_with_type_arg_support import singledispatch

@singledispatch
def describe(x) -> str:
  raise TypeError(f"no description for {repr(x)}")

@describe.register
def describe(x: type[int]) -> str:
  return "the integer type"

print(describe(int))  # should print: the integer type
