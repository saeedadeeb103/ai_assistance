import pprint
import google.generativeai as palm

palm.configure(api_key="AIzaSyAs1JIoVUnlc6vIwXfF7JJdLzsd_leo9Do")
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
breakpoint()
model = models[0].name
print(model)
prompt = "Act like Jarvis from ironman"
# Start the while loop
while True:
  # Get input from the user
  # If the user enters a quit command, break out of the loop
  if prompt == "quit":
    break

  # Generate a response
  completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
  )

  print(completion.result)
  prompt = input("Enter a command: ")

  # Replace any special characters in the response
  
  #completion.result = completion.result.replace("*", "").replace("/", "").replace("-", "")

  # Print the response
  