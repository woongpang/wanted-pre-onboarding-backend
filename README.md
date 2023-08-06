## 원티드 프리온보딩 백엔드 인턴십 - 선발 과제
<br>

## 지원자의 성명 : 이기웅
<br>

## ⚙️ 개발 환경 (Tech Stack)

- **Language** : `Python 3.11`
- **IDE** : `Visual Studio Code`
- **Framework** : `Django-Rest-Framework 3.14.0`
- **Database** : `mysql  Ver 8.0.33`
- **Packaging-tool** : `Poetry 1.5.0`

<br>

## 애플리케이션의 실행 방법 (엔드포인트 호출 방법 포함)

###  프로젝트 설치 및 실행 방법

#### 깃허브 클론하기

```bash
$ git init
$ git clone https://github.com/woongpang/wanted-pre-onboarding-backend
```

#### 패키지 밎 라이브러리 설치 | https://python-poetry.org/docs/

```bash
$ poetry shell
$ poetry install
```

#### DB 연동 | MYSQL | https://dev.mysql.com/doc/

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
##### 참고: 위의 명령어를 실행하기 전에, 로컬 머신에 MySQL이 설치되어 있어야 하고 사용자 본인이 데이터베이스 이름, 사용자 이름, 비밀번호, 그리고 기타 관련 설정을 직접 설정하셔야 합니다. 

#### 백엔드 서버 실행

```bash
$ python manage.py runserver
```

### 엔드포인트 호출 방법
#### 사용자 엔드포인트 (users)
- /signup/: 회원가입 엔드포인트입니다.
- /login/: 로그인 엔드포인트입니다.

#### 게시글 엔드포인트 (articles)
- /: 게시글 목록 조회
- /create/: 새로운 게시글 작성
- /<int:pk>/: 특정 게시글 상세정보 조회
- /<int:pk>/edit/: 특정 게시글 수정
- /<int:pk>/delete/: 특정 게시글 삭제

<br>

## 데이터베이스 테이블 구조
### User 테이블
- email: 사용자의 이메일 주소를 저장합니다. 이메일은 고유해야 하며, 이메일 형식을 검증합니다.
- password: 사용자의 비밀번호를 저장합니다.
- is_staff: 스태프 여부를 나타내는 필드입니다. 관리자 권한을 체크하는 데 사용됩니다.
- is_superuser: 슈퍼유저 여부를 나타내는 필드입니다. 관리자 권한을 체크하는 데 사용됩니다.
### Article 테이블
- author: 게시글 작성자를 참조합니다. User 테이블과 외래 키 관계를 맺고 있으며, 사용자가 삭제되면 관련 게시글도 삭제됩니다.
- title: 게시글 제목을 저장합니다. 최대 길이는 255자입니다.
- content: 게시글의 본문 내용을 저장하는 텍스트 필드입니다.
- created_at: 게시글이 생성된 시간을 저장합니다. 게시글 생성 시 자동으로 현재 시각이 설정됩니다.
- updated_at: 게시글이 수정된 시간을 저장합니다. 게시글 수정 시 자동으로 현재 시각이 설정됩니다.

<br>

## 구현한 API의 동작을 촬영한 데모 영상 링크
[데모 영상 링크](https://youtu.be/uPokqOlJSJE)


<br>

## 구현 방법 및 이유에 대한 간략한 설명

- 회원가입
    - 구현 방법: 사용자로부터 이메일, 비밀번호, 비밀번호 확인을 받고, 유효성 검사를 진행한 후 회원가입을 처리합니다.
    - 이유: 이메일 형식의 유효성과 비밀번호 일치 여부를 체크함으로써, 유저의 실수를 줄이고 시스템의 안정성을 높이기 위해 해당 코드를 사용했습니다.

- 로그인

    - 구현 방법: 사용자의 이메일과 비밀번호를 확인하고, 올바른 경우 토큰을 생성합니다.
    - 이유: 토큰 기반 인증은 stateless 이므로 서버 부하를 줄이며, 보안도 강화시키기 때문에 해당 방법을 사용했습니다.
- 게시글 리스트 조회
    - 구현 방법: 쿼리 파라미터를 통해 다양한 필터링 옵션을 제공합니다.
    - 이유: 쿼리 파라미터를 사용하면 URL을 깔끔하게 유지하면서도 사용자에게 유연한 조회 옵션을 제공할 수 있기 때문에 이 방식을 선택했습니다.
- 게시글 생성
    - 구현 방법: 제목, 내용 등 클라이언트로 부터 정보를 받아 게시글을 생성합니다.
    - 이유: 사용자의 입력을 직접 게시글 모델에 매핑함으로써, 코드의 복잡성을 줄이고 유지보수를 쉽게하기 위해 해당 코드를 사용했습니다.
- 게시글 수정하기
    - 구현 방법: 작성자 본인의 요청만 게시글을 수정할 수 있게 하였습니다.
    - 이유: 객체 권한 체크를 사용하면 보안을 강화하면서도 코드의 중복을 줄일 수 있어, 이 방법을 사용했습니다.
- 게시글 삭제하기
    - 구현 방법: 작성자 본인만 게시글을 삭제할 수 있으며, 삭제 성공 메시지를 반환합니다.
    - 이유: 작성자만 삭제 권한을 부여함으로써 데이터 무결성을 보호하고, 삭제 성공 메시지를 통해 사용자 경험을 향상시키기 위해 해당 코드를 선택했습니다.

<br>

## API 명세(request/response 포함)

[API 명세 링크](https://woongpang.notion.site/56e0b174982e405aad7d193f33d3242b?v=05cf3fc37de7435980aa509232b5e8c2&pvs=4)
또는 ("localhost/swagger/") 경로 접속 후 테스트 가능

<br>

## ERD

<img src = "https://i.postimg.cc/RVphYG6j/Untitled-1.png">



## 프로젝트 구조
```markdown
wanted
├── articles
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── wanted
│   └── settings.py
├── manage.py
├── poetry.lock
├── pyproject.toml
└── users
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    ├── models.py
    ├── serializers.py
    └── views.py
```