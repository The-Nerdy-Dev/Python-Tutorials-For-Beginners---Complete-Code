# Copying content of one file to another

def copy_content_from_input_to_output(inputFile, outputFile):

  with open(inputFile) as file_object:
    text = file_object.read()
  with open(outputFile,'w') as file_object:
    file_object.write(text)

copy_content_from_input_to_output("input.txt", "output.txt")

