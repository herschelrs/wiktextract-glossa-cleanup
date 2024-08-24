import json
import argparse

from process_dictionary import process_from_file

def main():
  parser = argparse.ArgumentParser(description='Copy contents from an input file to an output file.')

  parser.add_argument('--input', type=str, required=True, help='The path of the input file')
  parser.add_argument('--output', type=str, required=True, help='The path of the output file')
  parser.add_argument('--no-post-process', type=bool, required=False, help='Just parse entries')

  args = parser.parse_args()

  all_entries_matching_word = process_from_file(args.input, args.no_post_process)

  try:
    with open(args.output, 'w') as outfile:
      for entry in all_entries_matching_word:
        outfile.write(json.dumps([entry, all_entries_matching_word[entry]]) + "\n")

  except IOError as e:
    print(f"An error occurred while writing to the file {args.output}: {e}")
    exit(1)

  print(f"wrote output to {args.output}")

main()

