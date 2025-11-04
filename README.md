# AICE Prep – GitHub Starter

AICE(Artificial Intelligence Certificate for Everyone) 시험 준비를 **깃허브에서 자동화/가시화**하기 위한 스타터 킷입니다.

## 빠른 시작
1. 이 레포를 생성하고 파일을 업로드합니다.
2. **Settings ▸ Pages**에서 GitHub Pages를 활성화하세요. (브랜치: `gh-pages`)
3. **Projects**(칸반)를 만들고, 템플릿 이슈로 학습 태스크를 쪼갭니다.
4. 매일 저녁(21:15 KST) 자동으로 생성되는 “오늘의 AICE 학습” 이슈로 체크인을 합니다.

## 추천 사용 흐름
- **Milestone**: `AICE Associate 2025-xx-xx` 처럼 시험일을 마일스톤으로 지정
- **Labels**: `core`, `python`, `ml`, `data`, `ethics`, `mock-test`, `review` 등
- **Projects**: `Backlog ▸ Studying ▸ Review ▸ Done` 칼럼 구성
- **Docs(노트)**: `docs/` 아래 마크다운으로 정리 → GitHub Pages로 자동 배포

## 리포 구조
```
.github/
  ISSUE_TEMPLATE/
    study-task.yml         # 학습 태스크 이슈 템플릿
  workflows/
    reminder.yml           # 매일 학습 이슈 자동 생성 (21:15 KST)
    pages.yml              # MkDocs 문서 자동 배포
    quiz.yml               # 퀴즈/연습문제 자동 채점(PyTest)
docs/
  index.md                 # 문서 사이트 홈
src/
  quizzes/
    test_sample.py         # 예시 퀴즈(파이썬/pytest)
.devcontainer/
  devcontainer.json        # Codespaces/Dev Container
requirements.txt           # 파이썬 의존성
mkdocs.yml                 # MkDocs 설정
README.md
```

## 시험 대비 체크리스트(예시)
- [ ] 파이썬 기초문법/데이터구조
- [ ] 데이터핸들링: Numpy/Pandas
- [ ] EDA/시각화: Matplotlib
- [ ] 기본 ML: 회귀/분류, 검증/평가
- [ ] AI 윤리/보안/개인정보보호 개념
- [ ] 기출/모의고사 풀이 및 오답노트

## 라이선스
MIT