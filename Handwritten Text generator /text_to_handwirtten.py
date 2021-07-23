import pywhatkit as pw
# the text to be written
text  = str(input("Enter the text which you want to be wirriten down: "))
# the destination folder path 
destination = str(input('Enter the path to destination folder: '))
file_name = input("Enter the file name: ")
final = str(destination+'/'+file_name+'.png')

# .text_to_handwriting(string,save_to,rgb)
pw.text_to_handwriting(text,save_to=final)

print("----done writing your text----")