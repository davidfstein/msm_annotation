import subprocess
import os

def generate_vep_command(**kwargs):
    command = ['vep']
    for k, v in kwargs.items():
        option = [str(k)]
        if isinstance(v, list):
            for arg in v:
                command.extend(option + [arg])
            continue
        elif v:
            option.append(str(v))
        command.extend(option)
    return command

def vep(vep_command, input_location, additional_bind_dirs=None, vep_image='ensemblorg/ensembl-vep:release_112.0'):
    singularity_image = f'docker://{vep_image}'
    bind_dirs = [
        f"{input_location}:/input",
        f"{os.getcwd()}:/vep_output",
        f"{os.environ.get('VEP_DATA')}:/data"
    ]
    if additional_bind_dirs:
        for d in additional_bind_dirs:
            bind_dirs.append(f"{d}:{d}")
    
    singularity_command = ['singularity', 'exec', '--containall']
    
    for bind in bind_dirs:
        singularity_command.extend(['--bind', bind])
    
    singularity_command.append(singularity_image)
    command = singularity_command + vep_command
    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
        raise  
