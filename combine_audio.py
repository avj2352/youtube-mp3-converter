#!/usr/bin/env python3
import subprocess
import sys
import os
import argparse
from pathlib import Path

def combine_m4a_to_mp3(input_files, output_file, bitrate="192k", verbose=False):
    """Combine multiple m4a files into a single mp3 file using ffmpeg."""
    
    # Check if ffmpeg is available
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: ffmpeg not found. Please install ffmpeg.")
        sys.exit(1)
    
    # Verify all input files exist
    for file in input_files:
        if not os.path.exists(file):
            print(f"Error: File not found: {file}")
            sys.exit(1)
    
    # Create temporary playlist file
    playlist_file = "temp_playlist.txt"
    
    try:
        # Write playlist file
        with open(playlist_file, 'w', encoding='utf-8') as f:
            for file in input_files:
                abs_path = os.path.abspath(file)
                f.write(f"file '{abs_path}'\n")
        
        # Build ffmpeg command
        cmd = [
            "ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", playlist_file,
            "-codec:a", "libmp3lame",
            "-b:a", bitrate,
            "-y",
            output_file
        ]
        
        if not verbose:
            cmd.extend(["-loglevel", "error", "-stats"])
        
        print(f"Combining {len(input_files)} files into {output_file}...")
        
        # Run ffmpeg
        result = subprocess.run(cmd, text=True)
        
        if result.returncode == 0:
            print(f"✓ Successfully created {output_file}")
            size_mb = os.path.getsize(output_file) / (1024 * 1024)
            print(f"  Output file size: {size_mb:.2f} MB")
        else:
            print("Error running ffmpeg")
            sys.exit(1)
            
    finally:
        if os.path.exists(playlist_file):
            os.remove(playlist_file)

def main():
    parser = argparse.ArgumentParser(
        description='Combine multiple m4a files into a single mp3 file'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Input m4a files (if none specified, uses all *.m4a in current directory)'
    )
    parser.add_argument(
        '-o', '--output',
        default='combined_output.mp3',
        help='Output mp3 file (default: combined_output.mp3)'
    )
    parser.add_argument(
        '-b', '--bitrate',
        default='192k',
        help='Audio bitrate (default: 192k). Options: 128k, 192k, 256k, 320k'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Verbose ffmpeg output'
    )
    
    args = parser.parse_args()
    
    # Get input files
    if args.files:
        input_files = args.files
    else:
        # Use all m4a files in current directory
        input_files = sorted([str(f) for f in Path('.').glob('*.m4a')])
    
    if not input_files:
        print("Error: No input files specified or found")
        sys.exit(1)
    
    print(f"Found {len(input_files)} m4a files:")
    for i, file in enumerate(input_files, 1):
        print(f"  {i}. {Path(file).name}")
    
    combine_m4a_to_mp3(input_files, args.output, args.bitrate, args.verbose)

if __name__ == "__main__":
    main()
