# [Expert Standard] 홈페이지 제작 전문성 고도화 가이드
**작성자**: ChoiGPT Corp. 수석 전략가 (Agent)
**대상**: Alex Choi 및 프로젝트 수행 AI 에이전트
**목적**: Atomic Design 기반의 모듈화와 완벽한 SEO 적용을 통한 '전문가급' 결과물 도출 표준화

---

## 1. Atomic Design 표준 구조 (Architecture)
에이전트는 모든 웹 프로젝트 시작 시 다음의 디렉토리 구조를 강제하여 'Vendor Lock-in'을 방지하고 재사용성을 극대화한다.

### [Folder Structure]
- `src/components/atoms/`: 가장 작은 단위 (Button, Input, Icon, Typography)
- `src/components/molecules/`: 원자들의 조합 (SearchBar, FormField, NavItem)
- `src/components/organisms/`: 독립적 기능을 가진 복합체 (Header, Footer, CardGrid)
- `src/components/templates/`: 레이아웃 골격 (PageLayout, AuthLayout)
- `src/pages/`: 실제 경로와 매핑되는 최종 페이지

### [Implementation Rules]
1. **Purity**: 원자(Atoms) 단계의 컴포넌트는 외부 데이터에 의존하지 않고 오직 `props`로만 동작해야 한다.
2. **Modularity**: 모든 컴포넌트는 개별 CSS(또는 Module CSS)를 가져야 하며, 독립적으로 테스트 가능해야 한다.

---

## 2. SEO & Meta Tags 표준 명세 (Marketing)
모든 페이지의 `<head>` 영역에는 검색 엔진 최적화와 SNS 공유 최적화를 위해 다음 태그가 반드시 포함되어야 한다.

### [Essential Meta Tags]
- `title`: 핵심 키워드를 포함한 50~60자 이내의 제목
- `meta name="description"`: 페이지 내용을 요약한 150자 이내의 설명
- `meta name="keywords"`: 비즈니스 핵심 키워드 5~10개

### [Social Optimization (Open Graph)]
- `og:type`: 웹사이트 타입 (website, article 등)
- `og:title`: 공유 시 표시될 제목
- `og:description`: 공유 시 표시될 설명
- `og:image`: 권장 사이즈 1200x630px의 브랜드 이미지
- `og:url`: 페이지의 정규(Canonical) URL

### [Technical SEO]
- **Semantic HTML**: `<div>` 남발을 지양하고 `<header>`, `<main>`, `<footer>`, `<section>`, `<article>`을 적재적소에 사용한다.
- **Alt Text**: 모든 이미지에는 의미 있는 `alt` 속성을 부여한다.
- **Canonical Tag**: 중복 콘텐츠 방지를 위해 정규 URL 태그를 명시한다.

---

## 3. 에이전트 작업 프로세스 (Agent Workflow)
AI 에이전트는 프로젝트 요청 수신 시 다음 순서를 엄격히 준수한다.

1. **Phase 1: Architecture Design**
   - Atomic Design 기반의 컴포넌트 리스트를 먼저 정의하고 사용자 승인을 받는다.
2. **Phase 2: SEO Setup**
   - 프로젝트 초기 단계에서 `meta` 태그와 SEO 구조를 먼저 코딩한다.
3. **Phase 3: Development & Zero-Defect**
   - 개발 완료 후 `ESLint`, `Prettier`를 통해 코드 품질을 검수하고, 접근성(A11y) 테스트를 수행한다.
4. **Phase 4: Assetization**
   - 개발된 범용 모듈은 `Internal_Library`로 즉시 자산화하여 보고한다.

---

## 4. 체크리스트 (Final Audit)
- [ ] Atomic Design 5단계 계층 구조를 준수하였는가?
- [ ] 모든 페이지에 유니크한 Title과 Description이 있는가?
- [ ] Open Graph 태그가 SNS 미리보기를 완벽히 지원하는가?
- [ ] Semantic HTML을 사용하여 웹 접근성을 확보하였는가?
- [ ] 코드가 `Internal_Library`에 저장 가능한 수준으로 모듈화되었는가?
