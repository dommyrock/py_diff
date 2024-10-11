import xml.etree.ElementTree as ET
import difflib

def read_xml_file(file_path):
    """Reads the XML file and returns a pretty-printed string version of it."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return ET.tostring(root, encoding='unicode', method='xml')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def compare_xml_files(file1, file2):
    """Compares two XML files and prints their differences."""
    # Read and parse the XML files
    xml1 = read_xml_file(file1)
    xml2 = read_xml_file(file2)
    
    if xml1 is None or xml2 is None:
        print("Error in reading one of the files. Cannot compare.")
        return
    
    # Split the XML strings into lines
    xml1_lines = xml1.splitlines(keepends=True)
    xml2_lines = xml2.splitlines(keepends=True)
    
    # Use difflib to compare the files and print the diff
    diff = difflib.unified_diff(xml1_lines, xml2_lines, fromfile=file1, tofile=file2)
    print("".join(diff))  # Print the diff to console

# Example usage
file1 = "1.xml"  # Path to the first XML file
file2 = "2.xml"  # Path to the second XML file

compare_xml_files(file1, file2)
