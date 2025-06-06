import os
import subprocess
import tempfile
import shutil

def generate_pdf(dir):
    tex_path = os.path.join(dir, "proposal.tex")
    pdf_path = os.path.join(dir, "rendered_output.pdf")

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_tex_path = os.path.join(tmpdir, "proposal.tex")
        shutil.copy2(tex_path, tmp_tex_path)

        subprocess.run([
            "xelatex",
            "-output-directory", tmpdir,
            tmp_tex_path
        ], check=True)

        generated_pdf = os.path.join(tmpdir, "proposal.pdf")
        if os.path.exists(generated_pdf):
            shutil.move(generated_pdf, pdf_path)

    return "PDF Generated"
