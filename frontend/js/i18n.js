const translations = {
    en: {
        nav_home: "Home",
        nav_courses: "Courses",
        nav_about: "About",
        nav_login: "Login",
        nav_signup: "Sign Up",
        hero_title: "Learn. Grow. Succeed.",
        hero_subtitle: "Quality education for students LKG to 12th grade. CBSE, ICSE, State Boards & Olympiad",
        hero_cta: "Explore Courses",
        featured_courses: "Featured Courses",
        why_choose: "Why Choose EduLearn?",
        feature1_title: "Expert Teachers",
        feature1_desc: "Learn from experienced educators with proven teaching methodologies",
        feature2_title: "Learn Anywhere",
        feature2_desc: "Access content on any device, anytime. Your learning, your pace.",
        feature3_title: "Certified Learning",
        feature3_desc: "Get certificates upon course completion to boost your profile",
        footer_text: "Empowering students to achieve their dreams",
        error_loading: "Error loading courses",
        view_details: "View Details",
        login_title: "Welcome Back",
        login_email: "Email",
        login_password: "Password",
        login_button: "Login",
        login_signup_link: "Don't have an account? Sign up",
        signup_title: "Create Account",
        signup_firstname: "First Name",
        signup_lastname: "Last Name",
        signup_phone: "Phone Number",
        signup_password: "Password",
        signup_confirm: "Confirm Password",
        signup_button: "Sign Up",
        signup_login_link: "Already have an account? Login",
        dashboard_title: "My Dashboard",
        dashboard_enrolled: "Enrolled Courses",
        dashboard_profile: "My Profile",
        dashboard_logout: "Logout",
        profile_firstname: "First Name",
        profile_lastname: "Last Name",
        profile_email: "Email",
        profile_phone: "Phone",
        profile_language: "Preferred Language",
        profile_update: "Update Profile",
        courses_all: "All Courses",
        courses_filter: "Filter",
        courses_subject: "Subject",
        courses_board: "Board",
        courses_grade: "Grade Level",
        courses_apply_filter: "Apply Filter",
        course_detail_title: "Course Details",
        course_content: "Course Content",
        course_duration: "Duration",
        course_price: "Price",
        course_enroll: "Enroll Now",
        checkout_title: "Checkout",
        checkout_course: "Course",
        checkout_amount: "Amount",
        checkout_pay: "Pay with Razorpay",
        error_message: "Error",
        success_message: "Success",
        loading: "Loading...",
    },
    hi: {
        nav_home: "होम",
        nav_courses: "कोर्स",
        nav_about: "परिचय",
        nav_login: "लॉगिन",
        nav_signup: "साइन अप",
        hero_title: "सीखें। बढ़ें। सफल हों।",
        hero_subtitle: "एलकेजी से 12वीं तक के छात्रों के लिए गुणवत्तापूर्ण शिक्षा। सीबीएसई, आईसीएसई, स्टेट बोर्ड और ओलंपियाड",
        hero_cta: "कोर्स खोजें",
        featured_courses: "विशेष कोर्स",
        why_choose: "EduLearn क्यों चुनें?",
        feature1_title: "विशेषज्ञ शिक्षक",
        feature1_desc: "अनुभवी शिक्षकों से सीखें जिनके पास सिद्ध शिक्षण पद्धतियां हैं",
        feature2_title: "कहीं भी सीखें",
        feature2_desc: "किसी भी डिवाइस पर कभी भी सामग्री तक पहुंचें। आपकी शिक्षा, आपकी गति।",
        feature3_title: "प्रमाणित शिक्षा",
        feature3_desc: "कोर्स पूरा करने पर प्रमाणपत्र प्राप्त करें",
        footer_text: "छात्रों को उनके सपनों को प्राप्त करने में सशक्त बनाना",
        error_loading: "कोर्स लोड करने में त्रुटि",
        view_details: "विवरण देखें",
        login_title: "स्वागत है",
        login_email: "ईमेल",
        login_password: "पासवर्ड",
        login_button: "लॉगिन",
        login_signup_link: "खाता नहीं है? साइन अप करें",
        signup_title: "खाता बनाएं",
        signup_firstname: "पहला नाम",
        signup_lastname: "अंतिम नाम",
        signup_phone: "फोन नंबर",
        signup_password: "पासवर्ड",
        signup_confirm: "पासवर्ड की पुष्टि करें",
        signup_button: "साइन अप",
        signup_login_link: "पहले से खाता है? लॉगिन करें",
        dashboard_title: "मेरा डैशबोर्ड",
        dashboard_enrolled: "नामांकित कोर्स",
        dashboard_profile: "मेरी प्रोफ़ाइल",
        dashboard_logout: "लॉगआउट",
        profile_firstname: "पहला नाम",
        profile_lastname: "अंतिम नाम",
        profile_email: "ईमेल",
        profile_phone: "फोन",
        profile_language: "पसंदीदा भाषा",
        profile_update: "प्रोफ़ाइल अपडेट करें",
        courses_all: "सभी कोर्स",
        courses_filter: "फ़िल्टर",
        courses_subject: "विषय",
        courses_board: "बोर्ड",
        courses_grade: "ग्रेड स्तर",
        courses_apply_filter: "फ़िल्टर लागू करें",
        course_detail_title: "कोर्स विवरण",
        course_content: "कोर्स सामग्री",
        course_duration: "अवधि",
        course_price: "कीमत",
        course_enroll: "अभी नामांकन करें",
        checkout_title: "चेकआउट",
        checkout_course: "कोर्स",
        checkout_amount: "राशि",
        checkout_pay: "Razorpay के साथ भुगतान करें",
        error_message: "त्रुटि",
        success_message: "सफल",
        loading: "लोड हो रहा है...",
    }
};

let currentLanguage = localStorage.getItem('language') || 'en';

function changeLanguage(lang) {
    currentLanguage = lang;
    localStorage.setItem('language', lang);
    translatePage();
}

function translatePage() {
    const elements = document.querySelectorAll('[data-i18n]');
    elements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[currentLanguage][key]) {
            if (el.tagName === 'INPUT' || el.tagName === 'BUTTON' || el.tagName === 'TEXTAREA') {
                if (el.tagName === 'INPUT' && el.type === 'text') {
                    el.placeholder = translations[currentLanguage][key];
                } else {
                    el.textContent = translations[currentLanguage][key];
                }
            } else {
                el.textContent = translations[currentLanguage][key];
            }
        }
    });
}

function t(key) {
    return translations[currentLanguage][key] || key;
}
