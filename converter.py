import subprocess

def convert_doc_to_pdf(file_path,filename):
    args = ["libreoffice", '--headless', '--convert-to', 'pdf', '--outdir', ".",
            f"{file_path}"]
    converter = subprocess.run(args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
    return converter.returncode
