#!/usr/bin/env python3
"""Apply the Haftomyar developer/contact card to the extracted Android project."""
from pathlib import Path
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else "grade7_companion")
assets = root / "app/src/main/assets"
java_file = root / "app/src/main/java/ir/hanifyar/grade7/MainActivity.java"
js_file = assets / "app.js"
css_file = assets / "style.css"

for path in (js_file, css_file, java_file):
    if not path.is_file():
        raise SystemExit(f"Required project file not found: {path}")

js = js_file.read_text(encoding="utf-8")

if "function renderAbout()" not in js:
    anchor = "  function renderUpdates(){\n"
    about_fn = """  function renderAbout(){
    root.innerHTML=`${pageTitle('درباره هفتم‌یار','معرفی برنامه و راه‌های ارتباط با سازنده','home')}<section class="creator-card"><div class="creator-icon">۷</div><div class="creator-kicker">همراه هوشمند دانش‌آموز پایه هفتم</div><h2>هفتم‌یار</h2><p class="creator-description">یک همراه آموزشی برای یادگیری فصل‌به‌فصل، تمرین، آزمون و مرور درس‌های پایه هفتم.</p><div class="creator-divider"></div><div class="creator-label">سازنده و توسعه‌دهنده</div><div class="creator-name">حنیف رزاق بهار</div><div class="creator-label">شماره تماس</div><div class="creator-phone" dir="ltr">09153032669</div><button class="primary-btn creator-call" data-dial="09153032669">تماس با سازنده</button></section><div class="notice">هفتم‌یار یک پروژه آموزشی مستقل است و وابستگی یا تأیید رسمی از سوی وزارت آموزش‌وپرورش ندارد. محتوای آموزشی باید با نسخه رسمی کتاب‌های درسی و نظر دبیران تطبیق داده شود.</div>`;
  }

"""
    if anchor not in js:
        raise SystemExit("Could not locate renderUpdates() insertion point in app.js")
    js = js.replace(anchor, about_fn + anchor, 1)

if "else if(state.page==='about') renderAbout();" not in js:
    anchor = "    else if(state.page==='updates') renderUpdates();\n"
    replacement = anchor + "    else if(state.page==='about') renderAbout();\n"
    if anchor not in js:
        raise SystemExit("Could not locate render() route insertion point in app.js")
    js = js.replace(anchor, replacement, 1)

if "data-dial" not in js:
    anchor = "    const pageBtn=e.target.closest('[data-page]'); if(pageBtn){go(pageBtn.dataset.page);return;}\n"
    replacement = """    const dialBtn=e.target.closest('[data-dial]'); if(dialBtn){const phone=dialBtn.dataset.dial;if(window.HaftomyarNative&&window.HaftomyarNative.dialPhone){window.HaftomyarNative.dialPhone(phone);}else{window.location.href='tel:'+phone;}return;}
""" + anchor
    if anchor not in js:
        raise SystemExit("Could not locate click handler insertion point in app.js")
    js = js.replace(anchor, replacement, 1)

shortcut = """      <button class="creator-shortcut" data-page="about"><span><strong>درباره هفتم‌یار</strong><small>سازنده برنامه و اطلاعات تماس</small></span><span class="chapter-arrow">←</span></button>"""
if "creator-shortcut" not in js:
    notice = """      <div class="notice">محتوای این نسخه تألیفی و آموزشی است. برای امتحان مدرسه، مطالب را با آخرین چاپ کتاب درسی و راهنمای دبیر تطبیق دهید.</div>`;"""
    if notice not in js:
        raise SystemExit("Could not locate home notice insertion point in app.js")
    js = js.replace(notice, notice.replace("</div>`;", "</div>\n" + shortcut + "`;"), 1)

js_file.write_text(js, encoding="utf-8")

java = java_file.read_text(encoding="utf-8")
if "import android.content.Intent;" not in java:
    java = java.replace("import android.app.Activity;\n", "import android.app.Activity;\nimport android.content.Intent;\nimport android.net.Uri;\n", 1)

if "public void dialPhone(String phoneNumber)" not in java:
    anchor = "    private class AppBridge {\n"
    method = """    private class AppBridge {
        @JavascriptInterface
        public void dialPhone(String phoneNumber) {
            String safeNumber = phoneNumber == null ? "" : phoneNumber.replaceAll("[^0-9+]", "");
            if (safeNumber.length() < 8 || safeNumber.length() > 16) return;
            runOnUiThread(() -> {
                try {
                    Intent dialIntent = new Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + safeNumber));
                    startActivity(dialIntent);
                } catch (Exception ignored) {
                    // Keep the app usable if the device has no dialer activity.
                }
            });
        }

"""
    if anchor not in java:
        raise SystemExit("Could not locate AppBridge insertion point in MainActivity.java")
    java = java.replace(anchor, method, 1)

java_file.write_text(java, encoding="utf-8")

css = css_file.read_text(encoding="utf-8")
if "/* About page and developer contact */" not in css:
    css += """
/* About page and developer contact */
.creator-shortcut { width:100%; display:flex; align-items:center; justify-content:space-between; gap:12px; margin-top:12px; padding:15px; text-align:right; color:var(--text); background:linear-gradient(135deg,rgba(79,209,179,.10),var(--surface)); border:1px solid rgba(79,209,179,.22); border-radius:16px; }
.creator-shortcut strong { display:block; font-size:12px; }
.creator-shortcut small { display:block; color:var(--muted); margin-top:5px; font-size:10px; }
.creator-card { max-width:560px; margin:12px auto; padding:24px 20px; text-align:center; border:1px solid rgba(79,209,179,.24); border-radius:22px; background:radial-gradient(circle at 50% 0,rgba(79,209,179,.12),transparent 50%),linear-gradient(150deg,var(--surface-2),var(--surface)); box-shadow:var(--shadow); }
.creator-icon { width:62px; height:62px; display:grid; place-items:center; margin:0 auto 12px; border-radius:18px; background:rgba(79,209,179,.13); border:1px solid rgba(79,209,179,.25); color:var(--accent-2); font-size:34px; font-weight:900; }
.creator-kicker { color:var(--accent-2); font-size:10px; }
.creator-card h2 { margin:6px 0; font-size:21px; }
.creator-description { max-width:390px; margin:0 auto; color:var(--muted); font-size:11px; line-height:2; }
.creator-divider { height:1px; background:var(--line); margin:18px 0; }
.creator-label { color:var(--muted); font-size:10px; margin-top:12px; }
.creator-name { color:var(--text); font-size:17px; font-weight:800; margin-top:5px; }
.creator-phone { color:var(--accent-2); font-size:20px; font-weight:800; letter-spacing:.5px; margin-top:5px; }
.creator-call { margin-top:18px; min-width:170px; }
"""
css_file.write_text(css, encoding="utf-8")

print("Developer identity and tap-to-dial contact section applied.")
