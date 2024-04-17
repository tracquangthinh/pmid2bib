import pmid2bib.utils as utils
import argparse
import os
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
            prog = "pmid2bib",
            description = "Convert PMID to BIB for Latex",
            epilog = "Author: Thinh Trac")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
     
    parser.add_argument("-i", "--input", type = str,
                        metavar= "input", default = None,
                        help = "Latex input path")
    args = parser.parse_args()

    if args.input is not None:
        if os.path.isfile(args.input) is False:
            print("[Error] File does not exist")
            return 0

        input = args.input

        filename = Path(input).stem
        output_folder = os.path.join(os.path.dirname(input), "bib_out")

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_tex_path = os.path.join(output_folder, filename + "_new.tex")
        output_bib_path = os.path.join(output_folder, filename + "_new.bib")

        f = open(input, "r")
        lines = f.readlines()

        new_tex, new_bib = utils.convert(lines)

        out = open(output_tex_path, "w")
        for line in new_tex:
            out.write(line)
        out.close()

        out = open(output_bib_path, "w")
        for line in new_bib.values():
            out.write(line)
        out.close()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
