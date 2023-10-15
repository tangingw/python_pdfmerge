import glob
import os
import argparse
from pypdf import PdfMerger


def merge(working_directory, output_file="results.pdf"):
    previous_directory = os.getcwd()
    os.chdir(r"" + working_directory)

    merger = PdfMerger()

    for pdf_file in [
        os.path.join(f"{os.getcwd()}", item) for item in glob.glob("*.pdf")
    ]:
        merger.append(pdf_file)

    merger.write(os.path.join(previous_directory, output_file))
    merger.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=str, help="add path of pdfs")
    parser.add_argument("-o", "--output", type=str, help="name of output merged pdf")

    arguments = parser.parse_args()

    if not arguments.path:
        print("No path found")
        exit(2)
    
    if arguments.output:
        merge(arguments.path, arguments.output)
    
    else:
        merge(arguments.path)



if __name__ == "__main__":
    main()
    

