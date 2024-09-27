import csv

def main():

    with open('HuRI.psi', 'r') as mitab_file:
        reader = csv.reader(mitab_file, delimiter='\t')
        
        # Read the first few rows and count the columns
        for i, row in enumerate(reader):
            print(f"Row {i+1} has {len(row)} columns")
            if i == 10:
                break

    # MITAB 2.5: 15 columns
    # MITAB 2.6: 42 columns
    # MITAB 2.7: 36 columns
    # MITAB 2.8: 48 columns

    # Open the MITAB 2.6 file and an output TSV file
    with open('HuRI.psi', 'r') as mitab_file, open('output.tsv', 'w', newline='') as tsvfile:
        reader = csv.reader(mitab_file, delimiter='\t')
        writer = csv.writer(tsvfile, delimiter='\t')
        
        # Write header for the TSV file (adjust based on desired columns)
        writer.writerow(['Interactor A', 'Interactor B', 'Interaction Type', 'Confidence Score', 'Publication'])

        # Define the column indices based on MITAB 2.6 format (these are just examples)
        interactor_a_col = 0  # Column 1: interactor A
        interactor_b_col = 1  # Column 2: interactor B
        interaction_type_col = 11  # Column 12: interaction type
        confidence_col = 14  # Column 15: confidence score
        publication_col = 8  # Column 9: publication identifier

        # Iterate through rows and extract relevant columns
        for row in reader:
            interactor_a = row[interactor_a_col]
            interactor_b = row[interactor_b_col]
            interaction_type = row[interaction_type_col]
            confidence = row[confidence_col] if len(row) > confidence_col else 'N/A'
            publication = row[publication_col]
            
            writer.writerow([interactor_a, interactor_b, interaction_type, confidence, publication])

if __name__ == "__main__":
    main()