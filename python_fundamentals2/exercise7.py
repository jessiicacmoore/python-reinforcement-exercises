def wrap_text(message, wrapper):
  wrap = wrapper
  content = message
  reverse_wrap = wrapper[::-1]
  print(f"{wrap} {message} {str(reverse_wrap)}")

print("Welcome to the text wrapper, what message do you want to wrap?")
message_input = input()

print("Make your left wrapper and we'll reverse it!")
wrapper_input = input()

print()
print("Here's your message:")
print("-----------------------")
print()

wrap_text(message_input, wrapper_input)

print()
print("-----------------------")
print()
