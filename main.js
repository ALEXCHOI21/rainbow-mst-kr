document.addEventListener('DOMContentLoaded', () => {
    // Lucide Icons 초기화
    lucide.createIcons();

    // AOS 애니메이션 초기화
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: false,
        mirror: true
    });

    // 스크롤 시 헤더 스타일 변경
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // 모바일 메뉴 토글 (간단한 알림으로 대체하거나 추후 구현)
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            alert('모바일 메뉴 기능은 현재 준비 중입니다.');
        });
    }

    // 문의하기 폼 제출 처리
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('문의가 성공적으로 접수되었습니다. 곧 담당자가 연락드리겠습니다.');
            contactForm.reset();
        });
    }

    // 부드러운 스크롤 (이미 html { scroll-behavior: smooth; } 적용됨)
    // 추가적인 인터랙션이 필요할 경우 여기에 작성
});
