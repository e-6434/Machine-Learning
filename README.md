
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>نردبان یادگیری هوش مصنوعی</title>
  <style>
    :root {
      --primary: #6366f1;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --dark: #1f2937;
      --light: #f9fafb;
      --gray: #6b7280;
    }

    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
      color: var(--dark);
      margin: 0;
      padding: 20px;
      line-height: 1.7;
    }

    .container {
      max-width: 1200px;
      margin: auto;
      background: white;
      border-radius: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.1);
      overflow: hidden;
    }

    header {
      background: linear-gradient(120deg, var(--primary), #4f46e5);
      color: white;
      padding: 2rem;
      text-align: center;
    }

    header h1 {
      margin: 0;
      font-size: 2.2rem;
      font-weight: 700;
    }

    header p {
      margin: 0.5rem 0 0;
      opacity: 0.9;
      font-size: 1.1rem;
    }

    .badge {
      display: inline-block;
      padding: 0.35rem 0.75rem;
      border-radius: 50px;
      font-size: 0.8rem;
      font-weight: 600;
      margin: 0.25rem;
    }

    .badge-junior { background: #dbeafe; color: #4338ca; }
    .badge-ml { background: #fef3c7; color: #d97706; }
    .badge-dl { background: #d1fae5; color: #059669; }
    .badge-nlp { background: #fde8e8; color: #b91c1c; }
    .badge-cv { background: #e0e7ff; color: #1d4ed8; }
    .badge-senior { background: #f3e8ff; color: #7c3aed; }

    .section {
      padding: 2rem;
    }

    h2 {
      color: var(--primary);
      border-bottom: 3px solid var(--primary);
      padding-bottom: 0.5rem;
      margin-top: 0;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.95rem;
    }

    th {
      background: var(--primary);
      color: white;
      padding: 1rem;
      text-align: center;
      font-weight: 600;
    }

    td {
      padding: 1rem;
      border-bottom: 1px solid #e5e7eb;
      vertical-align: top;
    }

    tr:hover {
      background: #f8fafc;
    }

    .skill {
      font-weight: 600;
      color: var(--dark);
    }

    .link {
      color: var(--primary);
      text-decoration: none;
      font-weight: 500;
    }

    .link:hover {
      text-decoration: underline;
    }

    .footer {
      text-align: center;
      padding: 2rem;
      background: #f8fafc;
      color: var(--gray);
      font-size: 0.9rem;
    }

    @media (max-width: 768px) {
      table, thead, tbody, th, td, tr {
        display: block;
      }
      thead tr { display: none; }
      tr { margin-bottom: 1rem; border: 1px solid #ddd; border-radius: 8px; }
      td { border: none; position: relative; padding-left: 50%; }
      td:before {
        content: attr(data-label);
        position: absolute;
        left: 1rem;
        width: 45%;
        font-weight: bold;
        color: var(--primary);
      }
    }
  </style>
</head>
<body>

<div class="container">
  <header>
    <h1>نردبان یادگیری هوش مصنوعی</h1>
    <p>از صفر تا حرفه‌ای — ۱۶ پروژه واقعی با مهارت‌های شغلی</p>
    <div style="margin-top: 1rem;">
      <span class="badge badge-junior">Junior</span>
      <span class="badge badge-ml">ML</span>
      <span class="badge badge-dl">DL</span>
      <span class="badge badge-nlp">NLP</span>
      <span class="badge badge-cv">CV</span>
      <span class="badge badge-senior">Senior</span>
    </div>
  </header>

  <div class="section">
    <h2>جدول ۱۶ پروژه — تقویت مهارت‌های شغلی</h2>
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>پروژه</th>
          <th>چی می‌سازی؟</th>
          <th>ورودی</th>
          <th>خروجی</th>
          <th>دیتاست</th>
          <th>کد اجرا</th>
          <th>مهارت قوی‌شده</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td data-label="#">۱</td>
          <td data-label="پروژه"><strong>ماشین‌حساب هوشمند</strong></td>
          <td data-label="چی می‌سازی؟">برنامه ورودی/خروجی</td>
          <td data-label="ورودی">دو عدد</td>
          <td data-label="خروجی">جمع، تفریق، تقسیم</td>
          <td data-label="دیتاست">—</td>
          <td data-label="کد اجرا"><code>python calc.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-junior">پایتون پایه + خطا</span></td>
        </tr>
        <tr>
          <td data-label="#">۲</td>
          <td data-label="پروژه"><strong>تحلیل فروش فروشگاه</strong></td>
          <td data-label="چی می‌سازی؟">گزارش فروش</td>
          <td data-label="ورودی"><code>sales.csv</code></td>
          <td data-label="خروجی">پرفروش‌ترین محصول</td>
          <td data-label="دیتاست"><a href="https://www.kaggle.com/datasets/kyanyoga/sample-sales-data" class="link">Kaggle</a></td>
          <td data-label="کد اجرا"><code>python sales.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-ml">Pandas + تحلیل</span></td>
        </tr>
        <tr>
          <td data-label="#">۳</td>
          <td data-label="پروژه"><strong>نمودار زنده تایتانیک</strong></td>
          <td data-label="چی می‌سازی؟">داشبورد بصری</td>
          <td data-label="ورودی"><code>titanic.csv</code></td>
          <td data-label="خروجی">نمودار + عکس</td>
          <td data-label="دیتاست"><a href="https://www.kaggle.com/c/titanic/data" class="link">Kaggle</a></td>
          <td data-label="کد اجرا"><code>python plot.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-ml">بصری‌سازی</span></td>
        </tr>
        <tr>
          <td data-label="#">۴</td>
          <td data-label="پروژه"><strong>پیش‌بینی قیمت خونه</strong></td>
          <td data-label="چی می‌سازی؟">ماشین پیش‌بینی</td>
          <td data-label="ورودی">متراژ، اتاق</td>
          <td data-label="خروجی">قیمت + دقت</td>
          <td data-label="دیتاست"><a href="https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv" class="link">Boston</a></td>
          <td data-label="کد اجرا"><code>python house.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-ml">رگرسیون</span></td>
        </tr>
        <tr>
          <td data-label="#">۵</td>
          <td data-label="پروژه"><strong>تشخیص نوع گل</strong></td>
          <td data-label="چی می‌سازی؟">دسته‌بند هوشمند</td>
          <td data-label="ورودی">طول کاسبرگ</td>
          <td data-label="خروجی">نوع گل + دقت</td>
          <td data-label="دیتاست"><code>sklearn</code></td>
          <td data-label="کد اجرا"><code>python iris.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-ml">KNN</span></td>
        </tr>
        <tr>
          <td data-label="#">۶</td>
          <td data-label="پروژه"><strong>پیش‌بینی استعفا</strong></td>
          <td data-label="چی می‌سازی؟">سیستم HR</td>
          <td data-label="ورودی">رضایت، حقوق</td>
          <td data-label="خروجی">احتمال خروج</td>
          <td data-label="دیتاست"><a href="https://www.kaggle.com/giripujar/hr-analytics" class="link">Kaggle</a></td>
          <td data-label="کد اجرا"><code>python hr.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-ml">Feature Eng</span></td>
        </tr>
        <tr>
          <td data-label="#">۷</td>
          <td data-label="پروژه"><strong>تشخیص عدد دست‌نویس</strong></td>
          <td data-label="چی می‌سازی؟">خواننده تصویر</td>
          <td data-label="ورودی">عکس ۲۸×۲۸</td>
          <td data-label="خروجی">عدد + دقت</td>
          <td data-label="دیتاست"><code>tensorflow</code></td>
          <td data-label="کد اجرا"><code>python mnist.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-dl">CNN</span></td>
        </tr>
        <tr>
          <td data-label="#">۸</td>
          <td data-label="پروژه"><strong>تحلیل احساسات</strong></td>
          <td data-label="چی می‌سازی؟">تشخیص نظر</td>
          <td data-label="ورودی">متن نظر</td>
          <td data-label="خروجی">مثبت/منفی</td>
          <td data-label="دیتاست"><a href="https://huggingface.co/datasets/imdb" class="link">IMDB</a></td>
          <td data-label="کد اجرا"><code>python sentiment.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-nlp">NLP + LSTM</span></td>
        </tr>
        <tr>
          <td data-label="#">۹</td>
          <td data-label="پروژه"><strong>گربه/سگ</strong></td>
          <td data-label="چی می‌سازی؟">شناسایی حیوان</td>
          <td data-label="ورودی">عکس</td>
          <td data-label="خروجی">گربه/سگ</td>
          <td data-label="دیتاست"><a href="https://www.kaggle.com/c/dogs-vs-cats" class="link">Kaggle</a></td>
          <td data-label="کد اجرا"><code>python catdog.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-cv">Transfer Learning</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۰</td>
          <td data-label="پروژه"><strong>چت‌بات فارسی</strong></td>
          <td data-label="چی می‌سازی؟">ربات گفتگو</td>
          <td data-label="ورودی">پیام</td>
          <td data-label="خروجی">پاسخ</td>
          <td data-label="دیتاست"><a href="https://huggingface.co/datasets/cornell_movie_dialogs" class="link">Cornell</a></td>
          <td data-label="کد اجرا"><code>python bot.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-nlp">Hugging Face</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۱</td>
          <td data-label="پروژه"><strong>تشخیص ذات‌الریه</strong></td>
          <td data-label="چی می‌سازی؟">دکتر AI</td>
          <td data-label="ورودی">عکس ریه</td>
          <td data-label="خروجی">سالم/بیمار</td>
          <td data-label="دیتاست"><a href="https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia" class="link">Kaggle</a></td>
          <td data-label="کد اجرا"><code>python lung.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-cv">FastAI</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۲</td>
          <td data-label="پروژه"><strong>پیش‌بینی سهام</strong></td>
          <td data-label="چی می‌سازی؟">بورس AI</td>
          <td data-label="ورودی">۶۰ روز</td>
          <td data-label="خروجی">قیمت فردا</td>
          <td data-label="دیتاست"><code>yfinance</code></td>
          <td data-label="کد اجرا"><code>python stock.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-dl">LSTM</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۳</td>
          <td data-label="پروژه"><strong>تولید متن</strong></td>
          <td data-label="چی می‌سازی؟">نویسنده AI</td>
          <td data-label="ورودی">شروع جمله</td>
          <td data-label="خروجی">ادامه</td>
          <td data-label="دیتاست"><a href="https://huggingface.co/datasets/wikitext" class="link">WikiText</a></td>
          <td data-label="کد اجرا"><code>python gpt.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-nlp">Transformer</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۴</td>
          <td data-label="پروژه"><strong>توصیه‌گر فیلم</strong></td>
          <td data-label="چی می‌سازی؟">نتفلیکس کوچولو</td>
          <td data-label="ورودی">فیلم</td>
          <td data-label="خروجی">۵ پیشنهاد</td>
          <td data-label="دیتاست"><a href="https://grouplens.org/datasets/movielens/" class="link">MovieLens</a></td>
          <td data-label="کد اجرا"><code>python rec.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-ml">Recommender</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۵</td>
          <td data-label="پروژه"><strong>تشخیص در ویدیو</strong></td>
          <td data-label="چی می‌سازی؟">دوربین هوشمند</td>
          <td data-label="ورودی">ویدیو</td>
          <td data-label="خروجی">کادر روی اشیا</td>
          <td data-label="دیتاست">ویدیو خودت</td>
          <td data-label="کد اجرا"><code>python detect.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-cv">YOLOv8</span></td>
        </tr>
        <tr>
          <td data-label="#">۱۶</td>
          <td data-label="پروژه"><strong>اپلیکیشن وب AI</strong></td>
          <td data-label="چی می‌سازی؟">وب‌سایت هوشمند</td>
          <td data-label="ورودی">آپلود عکس</td>
          <td data-label="خروجی">نتیجه زنده</td>
          <td data-label="دیتاست">دلخواه</td>
          <td data-label="کد اجرا"><code>python app.py</code></td>
          <td data-label="مهارت"><span class="skill badge badge-senior">Full Stack AI</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="footer">
    <p>ساخته شده با ❤️ توسط <strong>شما</strong> | مربی: <strong>Grok</strong> | تاریخ: ۱۴۰۴/۰۸/۱۱</p>
    <p>هر هفته یه پله — ۴ ماه بعد: <strong>متخصص هوش مصنوعی</strong></p>
  </div>
</div>

</body>
</html>
