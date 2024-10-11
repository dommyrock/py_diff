import xml.etree.ElementTree as ET
import difflib
import webbrowser

def read_xml_file(file_path):
    """Reads the XML file and returns a pretty-printed string version of it."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return ET.tostring(root, encoding='unicode', method='xml')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def generate_html_diff(file1, file2, output_html):
    """Generates an HTML diff of two XML files and writes it to an output HTML file."""
    # Read and parse the XML files
    xml1 = read_xml_file(file1)
    xml2 = read_xml_file(file2)
    
    if xml1 is None or xml2 is None:
        print("Error in reading one of the files. Cannot generate diff.")
        return
    
    # Split the XML content into lines
    xml1_lines = xml1.splitlines(keepends=True)
    xml2_lines = xml2.splitlines(keepends=True)
    
    # Generate an HTML diff
    diff = difflib.HtmlDiff()
    html_diff = diff.make_file(xml1_lines, xml2_lines, fromdesc=file1, todesc=file2)
    
    # Write the HTML diff to a file
    with open(output_html, 'w') as f:
        f.write(html_diff)
    
    print(f"Diff has been written to {output_html}")
    
    webbrowser.open(output_html)

# Example usage
file1 = "1.xml"  # Path to the first XML file
file2 = "2.xml"  # Path to the second XML file
output_html = "diff_output.html"  # Path to save the output HTML file

generate_html_diff(file2, file1, output_html)
