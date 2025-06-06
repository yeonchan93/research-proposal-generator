import os
from dotenv import load_dotenv

from src.preprocess import latex_gen
from src.render import generate_pdf

load_dotenv()

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    dir = "assets"
    deep_research = "deep_research.pdf"
    class_name = input("강의명을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    num_pages = 5
    print(latex_gen(
        api_key=api_key,
        dir=dir,
        deep_research_filename=deep_research,
        class_name=class_name,
        name=name,
        num_pages=num_pages))
    print(generate_pdf(dir))

if __name__ == "__main__":
    main()
