import os


def replace_special_characters_in_files(input_folder, output_folder):
    # Iterates through all the files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)

            # Names the new file, you can add or modify it, i choose to add a "new" part to the end of the name
            output_filename = os.path.splitext(filename)[0] + '.new' + '.txt'
            output_path = os.path.join(output_folder, output_filename)

            replace_special_characters(input_path, output_path)


def replace_special_characters(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # create the dictionary with the characters that need to be modified, this is just an example, made you have other characters or letters to be modified after the conversion
    replacement_dict = {
        '$': 'ț',
        'ç': 'ș',
    }

    # Takes the symbols from the dic and replaces them with the letters or symbols given
    for old_char, new_char in replacement_dict.items():
        content = content.replace(old_char, new_char)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)
      
# Same as before, add the path to the input and output folder
replace_special_characters_in_files(r'path_folder_pdf', r'path_folder_txt')
