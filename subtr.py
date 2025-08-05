#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subtitle Translator Tool
This script translates subtitle files (.srt/.vtt) while preserving timestamps and formatting.
Uses Google Translate via the deep_translator library.
"""

import re
import argparse
from deep_translator import GoogleTranslator

def tr_sub_file(format, file_in, file_out, lang_in, lang_out):
    """
    Translates a subtitle file while preserving structure and timestamps.
    
    Args:
        format (str): Subtitle format - 'srt' or 'vtt'
        file_in (str): Input file path
        file_out (str): Output file path
        lang_in (str): Source language code (e.g. 'en')
        lang_out (str): Target language code (e.g. 'es')
    """
    # Validate supported subtitle formats
    if format not in ["vtt", "srt"]:
        raise ValueError("Format not supported. Use 'vtt' or 'srt'.")

    # Read all lines from input file
    with open(file_in, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Initialize Google Translator instance
    translator = GoogleTranslator(source=lang_in, target=lang_out)

    # Compile regex patterns based on subtitle format
    if format == "vtt":
        # VTT time format: 00:00:00.000 --> 00:00:00.000
        time_pattern = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}$")
    else:  # srt
        # SRT time format: 00:00:00,000 --> 00:00:00,000
        time_pattern = re.compile(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$")

    translated_lines = []
    for line in lines:
        stripped_line = line.strip()
        
        # Preserve non-text elements:
        # 1. Empty lines
        # 2. Subtitle sequence numbers
        # 3. Timestamp lines
        if stripped_line == "" or stripped_line.isdigit() or time_pattern.match(stripped_line):
            translated_lines.append(line)
        else:
            # Translate actual subtitle text
            try:
                translated = translator.translate(stripped_line)
                # Maintain original line structure with newline
                translated_lines.append(translated + "\n")
            except Exception as e:
                print(f"Error translating line: {stripped_line}")
                # Fallback to original text on error
                translated_lines.append(line)

    # Write translated content to output file
    with open(file_out, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

    print(f"Successfully translated: {file_in} -> {file_out}")

if __name__ == "__main__":
    # Configure command-line argument parser
    parser = argparse.ArgumentParser(
        description="Translate subtitle files (.srt/.vtt) while preserving timestamps and formatting"
    )
    parser.add_argument("--format", required=True, choices=["vtt", "srt"], 
                        help="Subtitle format: 'vtt' or 'srt'")
    parser.add_argument("--in", dest="file_in", required=True, 
                        help="Input subtitle file path")
    parser.add_argument("--out", dest="file_out", required=True, 
                        help="Output file path for translated subtitles")
    parser.add_argument("--lang-in", default="en", 
                        help="Source language code (default: 'en')")
    parser.add_argument("--lang-out", default="es", 
                        help="Target language code (default: 'es')")

    # Parse arguments and execute translation
    args = parser.parse_args()
    tr_sub_file(
        args.format, 
        args.file_in, 
        args.file_out, 
        args.lang_in, 
        args.lang_out
    )