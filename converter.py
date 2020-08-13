import subprocess


def convert_doc_to_pdf(filename):
    args = ["libreoffice", '--headless', '--convert-to', 'pdf', '--outdir', ".",
            f"{filename}"]
    converter = subprocess.run(args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE
                               )
    return converter.returncode
