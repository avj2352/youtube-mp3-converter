#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path
import re

def to_camel_case(text):
    """
    Convert text to camelCase.
    Handles spaces, hyphens, underscores, apostrophes, and other special characters.
    
    Examples:
        "Assassin's Creed" -> "assassinsCreed"
        "Black Flag - Main Theme" -> "blackFlagMainTheme"
        "Track 01" -> "track01"
        "I'll Be with You" -> "illBeWithYou"
    """
    # Replace apostrophes with empty string (don't -> dont, I'll -> Ill)
    text = text.replace("'", "")
    text = text.replace("'", "")  # Handle fancy apostrophe
    text = text.replace("`", "")
    
    # Replace common separators with spaces for splitting
    # This includes: hyphens, underscores, dots (but not in numbers)
    text = re.sub(r'[-_]+', ' ', text)
    
    # Remove parentheses and their contents (optional - can be disabled)
    # text = re.sub(r'\([^)]*\)', '', text)
    
    # Remove other special characters except alphanumeric and spaces
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split on whitespace (handles multiple spaces)
    words = text.split()
    
    # Filter out empty strings
    words = [w for w in words if w]
    
    if not words:
        return text
    
    # First word lowercase, rest title case
    # Preserve numbers: "track01" not "track01" -> "Track01"
    camel_words = []
    for i, word in enumerate(words):
        if i == 0:
            camel_words.append(word.lower())
        else:
            # Capitalize first letter, keep rest as-is (preserves numbers)
            camel_words.append(word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper())
    
    return ''.join(camel_words)

def to_camel_case_preserve_extension(filename):
    """
    Convert filename to camelCase while preserving the file extension.
    """
    path = Path(filename)
    name = path.stem  # filename without extension
    ext = path.suffix  # extension with dot
    
    camel_name = to_camel_case(name)
    
    # Handle edge case where result is empty
    if not camel_name:
        camel_name = "unnamed"
    
    return camel_name + ext

def rename_files(files, dry_run=False, verbose=False, remove_parens=False):
    """
    Rename files to camelCase in the same location.
    
    Args:
        files: List of file paths
        dry_run: If True, only show what would be renamed without actually renaming
        verbose: If True, show detailed output
        remove_parens: If True, remove parenthetical content like (Track 01)
    """
    renamed_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in files:
        path = Path(file_path)
        
        if not path.exists():
            print(f"✗ File not found: {file_path}")
            error_count += 1
            continue
        
        # Get directory and new filename
        directory = path.parent
        old_name = path.name
        
        # Handle parentheses removal if requested
        name_to_convert = path.stem
        if remove_parens:
            name_to_convert = re.sub(r'\([^)]*\)', '', name_to_convert)
            name_to_convert = re.sub(r'\[[^\]]*\]', '', name_to_convert)
        
        # Convert to camelCase
        camel_name = to_camel_case(name_to_convert)
        new_name = camel_name + path.suffix
        new_path = directory / new_name
        
        # Skip if name doesn't change
        if old_name == new_name:
            if verbose:
                print(f"⊘ Skipping (already camelCase): {old_name}")
            skipped_count += 1
            continue
        
        # Check if target file already exists
        if new_path.exists() and new_path != path:
            print(f"✗ Target already exists: {old_name} -> {new_name}")
            error_count += 1
            continue
        
        # Show what will be done
        if dry_run:
            print(f"[DRY RUN] {old_name}")
            print(f"       -> {new_name}")
            renamed_count += 1
        else:
            try:
                path.rename(new_path)
                print(f"✓ {old_name}")
                print(f"  -> {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"✗ Error renaming {old_name}: {e}")
                error_count += 1
    
    # Summary
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Summary:")
    print(f"  Renamed: {renamed_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")
    
    return renamed_count, skipped_count, error_count

def test_conversions():
    """Test the camelCase conversion with various inputs."""
    test_cases = [
        "Assassin's Creed IV Black Flag - Main Theme (Track 01)",
        "I'll Be with You",
        "Pyrates Beware",
        "Under the Black Flag",
        "A Merry Life and a Short One",
        "Track 01",
        "file-name-with-hyphens",
        "file_name_with_underscores",
        "MixedCase FileName",
        "multiple   spaces   here",
    ]
    
    print("Test conversions:")
    for test in test_cases:
        result = to_camel_case(test)
        print(f"  '{test}' -> '{result}'")

def main():
    parser = argparse.ArgumentParser(
        description='Rename files to camelCase in the same location',
        epilog='''Examples:
  python rename_camelcase.py file1.txt "My File.mp3" "another-file.pdf"
  python rename_camelcase.py -d *.m4a
  python rename_camelcase.py -r "Track (01).m4a"  # removes (01)
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Files to rename'
    )
    parser.add_argument(
        '-d', '--dry-run',
        action='store_true',
        help='Show what would be renamed without actually renaming'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show verbose output including skipped files'
    )
    parser.add_argument(
        '-r', '--remove-parens',
        action='store_true',
        help='Remove parenthetical content like (Track 01) or [Bonus]'
    )
    parser.add_argument(
        '-t', '--test',
        action='store_true',
        help='Run test conversions and exit'
    )
    
    args = parser.parse_args()
    
    if args.test:
        test_conversions()
        sys.exit(0)
    
    if not args.files:
        parser.print_help()
        sys.exit(1)
    
    if args.dry_run:
        print("=== DRY RUN MODE - No files will be renamed ===\n")
    
    rename_files(args.files, dry_run=args.dry_run, verbose=args.verbose, remove_parens=args.remove_parens)

if __name__ == "__main__":
    main()

