def remove_spaces_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Remove spaces in each line
        modified_lines = [line.replace(' ', '') for line in lines]

        with open(output_file, 'w') as file:
            file.writelines(modified_lines)

        print(f"Spaces removed from '{input_file}' and saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_file_path = "bl.txt"  # Replace this with the path to your input file
    output_file_path = "bl_N.txt"  # Replace this with the path where you want to save the output file
    remove_spaces_in_file(input_file_path, output_file_path)
