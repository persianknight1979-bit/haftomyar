# هفتم‌یار — راه‌اندازی مخزن و انتشار خودکار

این مخزن شامل آرشیو منبع اندروید و گردش‌کار انتشار است.

## فایل‌ها
- `source-parts/part-00.b64` تا `part-16.b64`: قطعات آرشیو فشرده منبع Android Studio؛ workflow آن‌ها را خودکار به فایل xz تبدیل می‌کند.
- `.github/workflows/publish.yml`: گردش‌کار ساخت APK و انتشار بسته‌های محتوا در GitHub Pages.

## انتشار خودکار
با هر push به شاخه `main` یا اجرای دستی workflow:
1. پروژه استخراج می‌شود.
2. فایل‌های محتوایی آفلاین با Python تولید می‌شوند.
3. بسته محتوای نسخه‌دار و manifest دارای SHA-256 ساخته می‌شود.
4. APK دیباگ با Java 17 و Android SDK 35 ساخته می‌شود.
5. APK و سرویس به‌روزرسانی محتوا در GitHub Pages منتشر می‌شوند.

آدرس سرویس محتوا:
`https://persianknight1979-bit.github.io/haftomyar/haftomyar/manifest.json`

صفحه دانلود و وضعیت انتشار:
`https://persianknight1979-bit.github.io/haftomyar/`

## ساخت محلی APK
برای بازیابی منبع از مخزن، در محیط Bash اجرا کنید: `cat source-parts/part-*.b64 | base64 -d > Haftomyar_Source.tar.xz && tar -xJf Haftomyar_Source.tar.xz`. سپس Android Studio، JDK 17، Android SDK Platform 35 و Python 3 را نصب کنید، پوشه `grade7_companion` را در Android Studio باز کنید و `build-debug.bat` را اجرا کنید.

## نکته درباره محتوا
محتوای همراه، تألیفی و نمونه اولیه است و پیش از استفاده آموزشی عمومی باید توسط دبیران، با چاپ رسمی کتاب‌های همان سال تطبیق داده شود. این پروژه ادعای تأیید رسمی آموزش‌وپرورش ندارد.

## نوع APK
Workflow فعلی APK از نوع debug می‌سازد که برای نصب و آزمایش مناسب است. انتشار عمومی و به‌روزرسانی خودکار خود برنامه (نه محتوای آموزشی) مستلزم کلید امضای release و فرایند توزیع جداگانه است.
