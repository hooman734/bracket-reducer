def bracketReducer(s):
    def reducer(inputString):
      dictionary = {'(': ')', ')': '(', '{': '}', '}': '{', '[': ']', ']': '['}  # Bracket definition
      if len(inputString) == 0:
          return ""

      elif len(inputString) == 1:
          return inputString

      else:
          if inputString[0] == dictionary[inputString[1]]:
              return reducer(inputString[2:])
          else:
              iterated = reducer(inputString[1:])
              if iterated == dictionary[inputString[:1]]:
                  return ""
              return inputString[:1] + iterated

    while s != reducer(s):
        s = reducer(s)

    return s if len(s) != 0 else "Matched"

print(bracketReducer("([{}()])"))
