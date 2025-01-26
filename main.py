import sys
import re
from typing import Optional


class Tag:
    def __init__(self, name: str, content: str) -> None:
        self.name = name
        self.html = f"<{name}>{content}</{name}>\n"


def parseInput() -> Optional[tuple[str]]:
    # Input should be in format: python main.py input.md output.html
    if len(sys.argv) != 3:
        print("Error: incorrect number of arguments")
    elif sys.argv[1][-3:] != ".md":
        print("Error: incorrect filetype for input file")
    elif sys.argv[2][-5:] != ".html":
        print("Error: incorrect filetype for output file")
    else:
        return (sys.argv[1], sys.argv[2])
    
    print("Usage: python main.py input.md output.html\n")
    sys.exit(1)


def addStyling() -> str:
    with open("style.css", 'r') as file:
        return "<style>" + file.read() + "</style>"


def parseLine(line: str) -> Optional[Tag]:
    # Headers
    if re.search("^# ", line):
        return Tag("h1", line[2:].strip())
    if re.search("^## ", line):
        return Tag("h2", line[3:].strip())
    if re.search("^### ", line):
        return Tag("h3", line[4:].strip())
    if re.search("^#### ", line):
        return Tag("h4", line[5:].strip())


def main() -> None:
    input, output = parseInput()
    in_file = open(input, 'r')
    out_file = open(output, 'a')
    out_file.write(f"<html><head>{addStyling()}</head><body>")

    line = in_file.readline()
    while line:
        try:
            out_file.write(parseLine(line).html)
        except AttributeError:
            out_file.write(line.strip())
        
        line = in_file.readline()

    out_file.write("</body></html>")
    out_file.close()
    in_file.close()


if __name__ == "__main__":
    main()
