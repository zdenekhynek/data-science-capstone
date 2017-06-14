import re

def remove_punctuation(tokens):
  filtered_tokens = []
  for token in tokens:
      if re.search('[a-zA-Z]', token):
          filtered_tokens.append(token)

  return filtered_tokens
