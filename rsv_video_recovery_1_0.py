import os

os.system("pip install ffmpeg-python")

import subprocess

# Create the 'out' folder if it doesn't exist
output_folder = os.path.join(os.getcwd(), 'out')
os.makedirs(output_folder, exist_ok=True)

# Iterate over files in the current directory

# Check for RSV video files
for file in os.listdir():
    if file.endswith('.rsv'):
        input_file = os.path.join(os.getcwd(), file)
        output_file = os.path.join(output_folder, os.path.splitext(file)[0])
        
        # Convert RSV to MP4
        output_mp4 = output_file + '.mp4'
        subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-crf', '23', output_mp4])

        # Convert RSV to MXF
        output_mxf = output_file + '.mxf'
        subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'mxf_opatom', output_mxf])

# softy_plug