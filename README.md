# 🐍 WSL + pyenv + pyenv-virtualenv + Django 개발 환경 세팅

## ✅ 개념 정리

### 1. WSL (Windows Subsystem for Linux)
- **정의**: Windows에서 리눅스 배포판(Ubuntu 등)을 실행할 수 있게 해주는 환경
- **역할**: Windows에서도 리눅스처럼 개발 가능 (`pip`, `python`, `vim`, `gunicorn` 등 사용 가능)
- **활용 이유**: Django는 Linux 환경에서 배포되는 경우가 많기 때문에 개발도 Linux에서 진행하는 것이 유리함


### 2. pyenv
- **정의**: 다양한 Python 버전을 쉽게 설치하고 전환할 수 있도록 도와주는 도구
- **역할**: 원하는 Python 버전 설치 및 프로젝트별 버전 관리
- **예시**: Django 3.2는 Python 3.9를 요구 → pyenv로 Python 3.9 설치 및 사용


### 3. pyenv-virtualenv
- **정의**: pyenv와 연동되어 가상환경(virtualenv)을 쉽게 생성하고 관리할 수 있도록 하는 플러그인
- **역할**: 프로젝트 별 독립된 패키지 환경 제공
- **비교**:
  - `venv`는 Python 기본 제공 가상환경 → pyenv와 연동 불편
  - `pyenv-virtualenv`는 pyenv와 자연스럽게 연동됨



## 🧭 전체 구성 흐름도

```markdown
📦 Windows
└─ 💻 WSL (Ubuntu 등)
    └─ 🔧 pyenv
        └─ 🔌 pyenv-virtualenv
            └─ 🧪 Django 프로젝트 가상환경
                ├── django
                ├── djangorestframework
                └── 기타 패키지들
```


## 🛠️ 설치 및 세팅 절차

### 1️⃣ WSL 및 파이썬 기본 의존패키지 설치

```bash
wsl --install
# 기본 Ubuntu 설치됨 (설치 후 재부팅 필요)
```

### 2️⃣ pyenv 설치

```bash
# 필수 패키지 설치
sudo apt update && sudo apt install -y make build-essential libssl-dev \
zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```


| 패키지                  | 설명                                             |
| -------------------- | ---------------------------------------------- |
| **make**             | `Makefile`을 읽어 자동으로 소프트웨어를 빌드하는 도구             |
| **build-essential**  | C/C++ 컴파일을 위한 기본 개발 도구 (gcc, g++, make 포함)     |
| **libssl-dev**       | OpenSSL 관련 라이브러리 (암호화 기능 필수)                   |
| **zlib1g-dev**       | 압축 포맷(zlib) 처리용 라이브러리                          |
| **libbz2-dev**       | bzip2 압축 파일 처리용 라이브러리                          |
| **libreadline-dev**  | Python에서 터미널 입력을 더 편리하게 지원 (예: 화살표 키 이동 등)     |
| **libsqlite3-dev**   | SQLite 데이터베이스 연동을 위한 개발용 헤더                    |
| **curl**             | 웹 요청 전송 툴 (스크립트에서 URL 호출 시 자주 사용됨)             |
| **llvm**             | 컴파일러 백엔드로 사용되며, 일부 Python 빌드 환경에서 필요           |
| **libncursesw5-dev** | 터미널 UI 구성 (화면 이동 등) 라이브러리                      |
| **xz-utils**         | `.xz` 확장자 압축 해제용 도구                            |
| **tk-dev**           | GUI 라이브러리 (Tkinter용), `import tkinter`가 되려면 필요 |
| **libxml2-dev**      | XML 파싱 관련 라이브러리                                |
| **libxmlsec1-dev**   | 보안 기능 포함 XML 파싱 라이브러리 (디지털 서명 등)               |
| **libffi-dev**       | C 라이브러리 호출 인터페이스 제공 (`ctypes`, `cffi`와 연동)     |
| **liblzma-dev**      | `.xz`, `.lzma` 등 고압축 포맷 처리용 라이브러리              |

### 3️⃣ pyenv-virtualenv 설치

```bash
# pyenv 플러그인 설치
git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```

> [!TIP] </br>
>  `~/.pyenv/plugins/`: **pyenv가 플러그인으로 인식**하는 기본 디렉토리 </br>
> → 이 명령으로 pyenv가 pyenv-virtualenv 기능을 사용할 수 있게 됨

```bash
# 쉘 설정 추가
# .bashrc는 로그인할 때 자동으로 실행되는 설정파일입니다.
echo -e '\n
# pyenv 설정\n
export PYENV_ROOT="$HOME/.pyenv"\n
export PATH="$PYENV_ROOT/bin:$PATH"\n
eval "$(pyenv init --path)"\n
eval "$(pyenv init -)"\n
eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

> [!TIP] </br>
> pyenv가 시작될 때 virtualenv 플러그인도 자동으로 초기화하도록 설정


```bash
# 설정 적용
source ~/.bashrc
```
> [!TIP] </br>
> .bashrc를 즉시 반영해서 현재 터미널에서도 설정을 사용할 수 있도록 함
> 재부팅 없이 pyenv virtualenv 명령 등을 바로 사용 가능해짐

### 4️⃣ Python 버전 설치 및 가상환경 생성

```bash
# 예: Python 3.11 설치
pyenv install 3.11.9

# 가상환경 생성 pyenv virtualenv {파이썬 버전} {가상 환경 이름}
pyenv virtualenv 3.11.9 my_django_env

# 프로젝트 디렉토리에서 가상환경 자동 적용
pyenv local my_django_env
```

### 5️⃣ Django 설치 및 프로젝트 실행

```bash
pip install django
django-admin startproject project_name .
python manage.py runserver
```

# 🧙‍♂️ Zsh 개발 환경 구성 with Oh My Zsh & Powerlevel10k

## ✅ 전체 구성요소

### 1. **zsh**
- 강력하고 커스터마이징 가능한 셸
- bash보다 다양한 개발 기능과 플러그인 지원

### 2. **oh-my-zsh**
- zsh 설정을 편리하게 관리할 수 있는 프레임워크
- 플러그인과 테마 설치 및 유지가 쉬움

### 3. **powerlevel10k**
- 최고의 Zsh 프롬프트 테마
- Git 브랜치, Python 가상환경, 디렉토리 경로, 오류 상태 등 실시간 표시
- 설정 마법사: `p10k configure`

### 4. **zsh-autosuggestions**
- 과거 명령어 히스토리를 기반으로 자동 제안
- 회색 텍스트로 표시 → → 방향키로 수락 가능

### 5. **zsh-syntax-highlighting**
- 명령어 입력 중 실시간 문법 하이라이팅
- 잘못된 명령어는 빨간색, 올바른 명령어는 초록색 등으로 시각화

### 6. **autojump**
- 자주 방문한 디렉토리를 기억하여 `j` 명령으로 빠른 이동 가능
- 예: `j dev` → `~/projects/dev-folder` 등으로 이동

---

## 🛠 설치 및 설정 명령어 (한 번에 실행)

```bash
# 1. 필수 패키지 설치
sudo apt update && sudo apt install -y zsh git curl autojump

# 2. 기본 쉘을 zsh로 변경
chsh -s $(which zsh)

# 3. oh-my-zsh 설치
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# 4. 플러그인 설치
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions

# 5. powerlevel10k 테마 설치
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k

# 6. .zshrc에 테마 및 플러그인 설정 적용
sed -i 's/^ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc
sed -i '/^plugins=/c\plugins=(git autojump zsh-autosuggestions zsh-syntax-highlighting)' ~/.zshrc

# 7. .zshrc 하단에 설정 코드 추가 (powerlevel10k + autojump + pyenv)
echo -e '\n# powerlevel10k 설정\n[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> ~/.zshrc
echo -e '\n# autojump 활성화\n[ -f /usr/share/autojump/autojump.sh ] && . /usr/share/autojump/autojump.sh' >> ~/.zshrc
echo -e '\n# pyenv 설정\nexport PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# 8. 설정 적용
source ~/.zshrc
```