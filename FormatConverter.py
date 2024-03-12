def convert_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Splitting each line at spaces and taking the second element, which is the adjective
            parts = line.strip().split(' ')
            if len(parts) >= 2:  # Ensure there are at least two parts to avoid IndexError
                adjective = parts[1]  # The adjective is the second element
                # Write the formatted string to the output file
                outfile.write(", '{}' ".format(adjective) + "\n")

# Example usage
input_file = 'unconverted_adj.txt'
output_file = 'converted_output_file.txt'

convert_lines(input_file, output_file)
