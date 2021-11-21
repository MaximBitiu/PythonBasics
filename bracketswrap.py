def wrap_brackets (text):
     return "(" + text + ")"
def wrap_squarebrackets (text):
    return "[" + text + "]"
def wrap_arrow (text):
    return "<" + text + ">"

a = wrap_brackets("12345")
a = wrap_squarebrackets
a = wrap_arrow
print(a)
 