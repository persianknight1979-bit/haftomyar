# هفتم‌یار — پروژه اندرویدی پایه هفتم

این مخزن شامل منبع Android Studio، بانک محتوای تألیفی اولیه، و گردش‌کار ساخت و انتشار خودکار است.

## سازنده و راه ارتباط\nنام سازنده در بخش «درباره هفتم‌یار» داخل برنامه درج شده است: **حنیف رزاق بهار**. شماره تماس: **09153032669**. دکمه تماس در اپلیکیشن شماره‌گیر گوشی را باز می‌کند و بدون اجازه کاربر تماس برقرار نمی‌کند.\n\n## دریافت نسخه آزمایشی
- [دانلود APK از آخرین Release](https://github.com/persianknight1979-bit/haftomyar/releases/latest)
- [مشاهده اجرای GitHub Actions](https://github.com/persianknight1979-bit/haftomyar/actions)

## به‌روزرسانی خودکار محتوای درون برنامه
محتوای جدید از شاخه `gh-pages` و از طریق HTTPS خام GitHub دریافت می‌شود؛ فعال‌سازی GitHub Pages لازم نیست.

نشانی manifest:
`https://raw.githubusercontent.com/persianknight1979-bit/haftomyar/gh-pages/haftomyar/manifest.json`

هر بسته محتوا فایل نسخه‌دار JSON و SHA-256 دارد. اپ باید هش بسته را پیش از جایگزین‌کردن محتوای قبلی بررسی کند. workflow پیش از انتشار نیز هش را اعتبارسنجی می‌کند.

## گردش‌کار انتشار
با هر push به شاخه `main` یا اجرای دستی workflow:
1. آرشیو منبع Android Studio از قطعات داخل `source-parts` بازسازی می‌شود.
2. بانک محتوای اولیه با Python تولید می‌شود.
3. manifest و بسته نسخه‌دار همراه SHA-256 ساخته و اعتبارسنجی می‌شوند.
4. APK دیباگ با Java 17 و Android SDK 35 ساخته می‌شود.
5. بسته محتوا در شاخه `gh-pages` منتشر می‌شود.
6. APK به‌عنوان GitHub Actions artifact و نیز Release آزمایشی منتشر می‌شود.

فایل workflow:
`.github/workflows/publish.yml`

## ساخت محلی APK
برای بازیابی منبع در محیط Bash اجرا کنید:

```bash
cat source-parts/part-*.b64 | base64 -d > Haftomyar_Source.tar.xz
tar -xJf Haftomyar_Source.tar.xz
```

سپس Android Studio، JDK 17، Android SDK Platform 35 و Python 3 را نصب کنید، پوشه `grade7_companion` را باز کنید و `build-debug.bat` را اجرا کنید.

## وضعیت و محدودیت‌ها
APK فعلی از نوع **debug** و برای نصب و آزمایش است؛ نسخه انتشار عمومی با امضای release و کلید اختصاصی هنوز ساخته نشده است. محتوای موجود تألیفی و نمونه اولیه است و پیش از استفاده آموزشی عمومی باید توسط دبیران و با چاپ رسمی کتاب‌های همان سال بازبینی شود. این پروژه وابسته به آموزش‌وپرورش نیست و تأیید رسمی ندارد.
