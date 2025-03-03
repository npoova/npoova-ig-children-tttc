import subprocess
import platform


def visualization(config):
    output_dir = config['output_dir'].strip()
    with open(f"outputs/{output_dir}/result.json", encoding='utf-8') as f:
        result = f.read()

    cwd = "../next-app"
    if platform.system() == "Windows":
        command = f'set REPORT={output_dir}&& npm run build'
    else:
        command = f"REPORT={output_dir} npm run build"


    try:
        process = subprocess.Popen(
            command, shell=True, cwd=cwd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, universal_newlines=True, encoding='utf-8'
        )
        while True:
            output_line = process.stdout.readline()
            if output_line == '' and process.poll() is not None:
                break
            if output_line:
                print(output_line.strip())
        process.wait()
        errors = process.stderr.read()
        if errors:
            print("Errors:")
            print(errors)
    except subprocess.CalledProcessError as e:
        print("Error: ", e)