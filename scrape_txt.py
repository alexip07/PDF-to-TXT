import re


def extract_information_from_txt(txt_path, criteria, output_file):
    with open(txt_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Combine lines to handle sentences spanning multiple lines -> this is a fail safe option, if this isn't here, the scraping will be done chaotically
    combined_text = ' '.join(lines)

    results = []
    sentences = re.split(r'(?<=[.!?])\s+', combined_text)

    for sentence in sentences:
        # Check each sentence against the criteria
        for crit in criteria:
            if re.search(crit, sentence, re.IGNORECASE):
                results.append(sentence.strip())
                break  # Stop searching for criteria once a match is found

    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')

txt_path = 'YOUR TXT PATH -> INPUT FILE'
output_file = 'OUTPUT FILE PATH'
criteria = ['INSEERT CRITERIA HERE, USE COMMA TO ADD MULTPLES', 'LIKE THIS']

extract_information_from_txt(txt_path, criteria, output_file)
