from openai import OpenAI
import PyPDF2
import os

def latex_gen(api_key, dir, deep_research_filename, class_name, name, num_pages=None):
    client = OpenAI(api_key=api_key)
    deep_path = os.path.join(dir, deep_research_filename)

    with open(deep_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        deep_text = ""
        for i, page in enumerate(reader.pages):
            deep_text += page.extract_text() or ""

    latex_response = client.responses.create(
        model="gpt-4.1",
        input=[
            {"role": "system", "content": (
                "You are an expert at writing research proposals in LaTeX. "
                "You will be given a openai's deep research content. "
                "Generate a research proposal in valid LaTeX format, suitable for direct compilation with xelatex. "
                "Use LaTeX math syntax for equations, avoid HTML or markdown. "
                "Respond only with the LaTeX document, no explanations, no code fences. "
                f"The proposal must cover {num_pages} pages. "
                f"The proposal would follow title, {class_name} (class name on the right), {name} (name on the right), 연구과제의 필요성, 연구과제의 목표 및 내용, 연구과제의 활용방안 및 기대효과, 참고문헌. "
                "Do not add summary, end the document with reference (참고문헌 above). "
                "Respond only in Korean."
            )},
            {"role": "user", "content": deep_text}
        ]
    )
    latex = latex_response.output_text

    tex_filename = "proposal.tex"
    tex_path = os.path.join(dir, tex_filename)
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(latex)
    return "proposal.tex Generated"
