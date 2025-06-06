# 연구 제안서 자동 생성기

이 프로젝트는 PDF로 된 딥리서치(Deep Research) 자료를 읽어, LaTeX 형식의 연구 제안서를 자동으로 생성하고 PDF로 렌더링하는 파이프라인을 제공합니다.

---

## 현재 기능 및 한계

- **딥리서치 내용 자동 생성은 현재 지원되지 않습니다.**
  - OpenAI의 딥리서치 API가 아직 제공되지 않아, 외부에서 생성된 `deep_research.pdf` 파일을 직접 준비해야 합니다.
  - 향후 OpenAI API가 제공되면, 단순 아이디어(naive idea)로부터 연구 제안서를 자동 생성하는 기능이 추가될 예정입니다.

---

## 주요 파일 설명

- [`main.py`](main.py:1): 전체 실행 진입점. 환경 변수 로드, 사용자 입력(강의명, 이름), PDF 읽기, LaTeX 생성, PDF 렌더링을 순차적으로 수행합니다.
- [`src/preprocess.py`](src/preprocess.py:1): 
  - `latex_gen()` 함수는 PDF 파일에서 텍스트를 추출하고, OpenAI API를 통해 LaTeX 형식의 연구 제안서를 생성합니다.
  - 현재는 OpenAI API 키가 필요하며, 실제 딥리서치 내용이 담긴 PDF(`assets/deep_research.pdf`)가 필요합니다.
- [`src/render.py`](src/render.py:1): 
  - `generate_pdf()` 함수는 생성된 LaTeX 파일을 XeLaTeX으로 컴파일하여 최종 PDF(`assets/rendered_output.pdf`)를 생성합니다.
- [`Dockerfile`](Dockerfile:1): 
  - XeLaTeX, LaTeX 한글 지원 패키지, 한글 폰트, uv 패키지 매니저 등 모든 실행에 필요한 환경을 자동으로 설치합니다.

---

## Docker 실행

1. **Docker Compose로 컨테이너 실행**
   - 아래 명령어로 Docker 컨테이너를 백그라운드에서 실행할 수 있습니다.
     ```bash
     docker compose up -d
     ```
   - 컨테이너 내부에는 XeLaTeX, LaTeX 한글 지원 패키지, 한글 폰트, uv 등 모든 실행 환경이 자동으로 설치됩니다.
   - [`Dockerfile`](Dockerfile:1)에서 설치 과정을 확인할 수 있습니다.

2. **컨테이너에 접속**
   - 실행 중인 컨테이너에 접속하려면 다음 명령어를 사용하세요.
     ```bash
     docker compose exec [서비스명] bash
     ```
   - `[서비스명]`은 `docker-compose.yml`에 정의된 서비스 이름입니다(예: `app`).

3. **컨테이너 내부에서 uv 명령 실행**
   - 컨테이너 내부에서 아래 명령어로 의존성을 설치하고 스크립트를 실행하세요.
     ```bash
     uv install
     uv run python main.py
     ```
   - 실행 시, 강의명과 이름을 입력하라는 메시지가 표시됩니다.

4. **입력 파일 준비**
   - `assets/deep_research.pdf` 파일을 미리 준비해 두어야 합니다.
   - 향후 OpenAI API가 지원되면, 아이디어만 입력해도 연구 제안서가 자동 생성될 예정입니다.

---

## 사용 예시

1. `assets/deep_research.pdf` 파일을 준비합니다.
2. 위의 설치 및 실행 방법을 따라 실행합니다.
3. 실행 후, `assets/proposal.tex`와 `assets/rendered_output.pdf` 파일이 생성됩니다.

---

## 향후 계획

- OpenAI의 딥리서치 API가 공개되면, 단순 아이디어 입력만으로 연구 제안서 초안을 자동 생성하는 기능을 추가할 예정입니다.
- 다양한 템플릿 및 맞춤형 연구 제안서 양식 지원 예정입니다.

---

## 참고 사항

- 모든 의존성은 uv로 관리됩니다.
- 환경 변수(`OPENAI_API_KEY`)가 필요합니다. `.env` 파일에 키를 저장하세요.