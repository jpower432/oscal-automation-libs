#!/usr/bin/env python3
# xml_to_json.py

"""
Convert OSCAL XML profiles to JSON

Author: Jenn Power <jpower@redhat.com>
"""

import argparse
import os
from saxonche import PySaxonProcessor
    
def main():
    p = argparse.ArgumentParser(
        description="Generates a markdown from high-level SSP data"
    )
    p.add_argument("input")
    p.add_argument("output")
    args = p.parse_args()

    # Load the XML input file
    xml_filename = args.input

    # Load the XSLT stylesheet
    xslt_filename = 'oscal_profile_xml-to-json-converter.xsl'
    xslt_path = os.path.join(os.path.dirname(__file__), xslt_filename)

    # Create a Saxon processor and compiler
    with PySaxonProcessor(license=False) as proc:
        xsltproc = proc.new_xslt30_processor()

        # Compile the XSLT stylesheet
        xslt_doc = xsltproc.compile_stylesheet(stylesheet_file=xslt_path)
        xslt_doc.set_initial_match_selection(file_name=xml_filename)

        # Apply the XSLT transformation to the XML input and write the result file
        xslt_doc.apply_templates_returning_file(output_file=args.output)
   
if __name__ == "__main__":
    main()
