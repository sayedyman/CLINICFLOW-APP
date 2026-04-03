import codecs

src = 'c:\\Users\\Sayed\\.gemini\\antigravity\\scratch\\health-security-screen\\security.html'
with codecs.open(src, 'r', 'utf-8') as f:
    text = f.read()

replacements = {
    '<h1 class="title">Security & Privacy</h1>': '<h1 class="title" data-i18n="sec_privacy">Security & Privacy</h1>',
    '<h2 class="section-title">Security</h2>': '<h2 class="section-title" data-i18n="section_security">Security</h2>',
    '<div class="item-title">Change Password</div>': '<div class="item-title" data-i18n="change_password">Change Password</div>',
    '<div class="item-desc">Secure your account credentials</div>': '<div class="item-desc" data-i18n="change_password_desc">Secure your account credentials</div>',
    '<label class="form-label">Current Password</label>': '<label class="form-label" data-i18n="current_password">Current Password</label>',
    '<label class="form-label">New Password</label>': '<label class="form-label" data-i18n="new_password">New Password</label>',
    '<label class="form-label">Confirm New Password</label>': '<label class="form-label" data-i18n="confirm_password">Confirm New Password</label>',
    'placeholder="Enter current password"': 'placeholder="Enter current password" data-i18n-placeholder="enter_current"',
    'placeholder="Min. 8 characters"': 'placeholder="Min. 8 characters" data-i18n-placeholder="min_8"',
    'placeholder="Re-enter new password"': 'placeholder="Re-enter new password" data-i18n-placeholder="re_enter"',
    '<a href="#" class="forgot-password-txt">Forgot Password?</a>': '<a href="#" class="forgot-password-txt" data-i18n="forgot_password">Forgot Password?</a>',
    '<button class="primary-btn">Confirm Password Change</button>': '<button class="primary-btn" data-i18n="confirm_password_change">Confirm Password Change</button>',
    '<h2 class="section-title">Permissions</h2>': '<h2 class="section-title" data-i18n="section_permissions">Permissions</h2>',
    '<div class="item-title">Camera Access</div>': '<div class="item-title" data-i18n="camera_access">Camera Access</div>',
    '<div class="item-desc">Used to upload medical reports</div>': '<div class="item-desc" data-i18n="camera_desc">Used to upload medical reports</div>',
    '<div class="item-title">Photo Library Access</div>': '<div class="item-title" data-i18n="photo_access">Photo Library Access</div>',
    '<div class="item-desc">Access your gallery to attach images</div>': '<div class="item-desc" data-i18n="photo_desc">Access your gallery to attach images</div>',
    '<h2 class="section-title">Medical Privacy</h2>': '<h2 class="section-title" data-i18n="section_med_privacy">Medical Privacy</h2>',
    '<div class="item-title">Doctor Access to Records</div>': '<div class="item-title" data-i18n="doctor_access">Doctor Access to Records</div>',
    '<div class="item-desc">Manage who can view your health data</div>': '<div class="item-desc" data-i18n="doctor_desc">Manage who can view your health data</div>',
    '<h2 class="section-title">Legal</h2>': '<h2 class="section-title" data-i18n="section_legal">Legal</h2>',
    '<div class="item-title">Privacy Policy</div>': '<div class="item-title" data-i18n="privacy_policy">Privacy Policy</div>',
    '<div class="item-desc">Read our external legal agreements</div>': '<div class="item-desc" data-i18n="privacy_desc">Read our external legal agreements</div>',
    '</body>': '<script src="translations.js"></script>\n</body>'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with codecs.open(src, 'w', 'utf-8') as f:
    f.write(text)

print("done security")

src2 = 'c:\\Users\\Sayed\\.gemini\\antigravity\\scratch\\health-security-screen\\privacy-policy.html'
with codecs.open(src2, 'r', 'utf-8') as f:
    t2 = f.read()

rep2 = {
    '<h1 class="title">Privacy Policy</h1>': '<h1 class="title" data-i18n="privacy_policy">Privacy Policy</h1>',
    '<span class="date-updated">Last Updated: October 2026</span>': '<span class="date-updated" data-i18n="last_updated">Last Updated: October 2026</span>',
    '<h3 class="privacy-section-title">1. Introduction</h3>': '<h3 class="privacy-section-title" data-i18n="intro_title">1. Introduction</h3>',
    '<h3 class="privacy-section-title">2. Information We Collect</h3>': '<h3 class="privacy-section-title" data-i18n="info_collect">2. Information We Collect</h3>',
    '<h3 class="privacy-section-title">3. How We Use Your Information</h3>': '<h3 class="privacy-section-title" data-i18n="how_use">3. How We Use Your Information</h3>',
    '<h3 class="privacy-section-title">4. Will Your Information Be Shared?</h3>': '<h3 class="privacy-section-title" data-i18n="shared_info">4. Will Your Information Be Shared?</h3>',
    '<h3 class="privacy-section-title">5. Data Retention</h3>': '<h3 class="privacy-section-title" data-i18n="data_retention">5. Data Retention</h3>',
    '<h3 class="privacy-section-title">6. Medical Data Security</h3>': '<h3 class="privacy-section-title" data-i18n="med_data_sec">6. Medical Data Security</h3>',
    '>\n                    Welcome to our Healthcare App. We are committed to protecting your personal information and your right to privacy. If you have any questions or concerns about our policy, or our practices with regards to your personal information, please contact us.\n                </p>': ' data-i18n="intro_text">\n                    Welcome to our Healthcare App. We are committed to protecting your personal information and your right to privacy. If you have any questions or concerns about our policy, or our practices with regards to your personal information, please contact us.\n                </p>',
    '>\n                    We collect personal information that you voluntarily provide to us when registering at the Services, expressing an interest in obtaining information about us or our products and services, when participating in activities on the Services or otherwise contacting us.\n                </p>': ' data-i18n="collect_text">\n                    We collect personal information that you voluntarily provide to us when registering at the Services, expressing an interest in obtaining information about us or our products and services, when participating in activities on the Services or otherwise contacting us.\n                </p>',
    '>\n                    We use personal information collected via our Services for a variety of business purposes described below. We process your personal information for these purposes in reliance on our legitimate business interests, in order to enter into or perform a contract with you, with your consent, and/or for compliance with our legal obligations.\n                </p>': ' data-i18n="use_text">\n                    We use personal information collected via our Services for a variety of business purposes described below. We process your personal information for these purposes in reliance on our legitimate business interests, in order to enter into or perform a contract with you, with your consent, and/or for compliance with our legal obligations.\n                </p>',
    '>\n                    We only share information with your consent, to comply with laws, to provide you with services, to protect your rights, or to fulfill business obligations.\n                </p>': ' data-i18n="share_text">\n                    We only share information with your consent, to comply with laws, to provide you with services, to protect your rights, or to fulfill business obligations.\n                </p>',
    '>\n                    We will only keep your personal information for as long as it is necessary for the purposes set out in this privacy policy, unless a longer retention period is required or permitted by law.\n                </p>': ' data-i18n="retention_text">\n                    We will only keep your personal information for as long as it is necessary for the purposes set out in this privacy policy, unless a longer retention period is required or permitted by law.\n                </p>',
    '>\n                    We implement appropriate technical and organizational security measures designed to protect the security of any personal and medical information we process. However, please also remember that we cannot guarantee that the internet itself is 100% secure.\n                </p>': ' data-i18n="med_sec_text">\n                    We implement appropriate technical and organizational security measures designed to protect the security of any personal and medical information we process. However, please also remember that we cannot guarantee that the internet itself is 100% secure.\n                </p>',
    '</body>': '<script src="translations.js"></script>\n</body>'
}

for k, v in rep2.items():
    t2 = t2.replace(k, v)

with codecs.open(src2, 'w', 'utf-8') as f:
    f.write(t2)

print("done privacy")
