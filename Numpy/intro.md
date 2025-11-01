<h1 align="center">🌎 توابع مهم </h1>

 <h2 align="center">🧮 دستورات پرکاربرد NumPy</h2>

<table align="center" style="border-collapse: collapse; width: 90%; text-align: center;">
  <thead>
    <tr style="background-color: #1f2937; color: #f9fafb;">
      <th style="border: 1px solid #ddd; padding: 8px;">دستور</th>
      <th style="border: 1px solid #ddd; padding: 8px;">توضیح</th>
      <th style="border: 1px solid #ddd; padding: 8px;">مثال</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.array()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">ساخت آرایه از لیست یا تاپل</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>a = np.array([1, 2, 3])</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.zeros()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">آرایه‌ای از صفرها</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.zeros(5) → [0. 0. 0. 0. 0.]</code></td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.ones()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">آرایه‌ای از یک‌ها</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.ones((2,3)) → ماتریس ۲×۳ از ۱</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.full()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">آرایه با مقدار ثابت</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.full((2,2), 7) → [[7 7][7 7]]</code></td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.arange()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">مشابه range ولی خروجی آرایه</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.arange(0, 10, 2) → [0 2 4 6 8]</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.linspace()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">تولید اعداد با فاصله مساوی</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.linspace(0, 1, 5) → [0. 0.25 0.5 0.75 1.]</code></td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.random.rand()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">اعداد تصادفی بین [0,1)</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.random.rand(3)</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.random.randint()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">اعداد صحیح تصادفی</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.random.randint(1, 10, size=5)</code></td>
    </tr>
  </tbody>
</table>

<h2 align="center">📐 ویژگی‌ها و مشخصات آرایه در NumPy</h2>

<table align="center" style="border-collapse: collapse; width: 70%; text-align: center;">
  <thead>
    <tr style="background-color: #1f2937; color: #f9fafb;">
      <th style="border: 1px solid #ddd; padding: 8px;">دستور</th>
      <th style="border: 1px solid #ddd; padding: 8px;">توضیح</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>arr.shape</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">ابعاد آرایه (تعداد سطر و ستون)</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>arr.ndim</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">تعداد بعدهای آرایه</td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>arr.size</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">تعداد کل عناصر موجود در آرایه</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>arr.dtype</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">نوع داده‌ای عناصر آرایه (مثل int32، float64 و...)</td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>arr.reshape()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">تغییر شکل آرایه بدون تغییر محتوای داده‌ها</td>
    </tr>
  </tbody>
</table>
<h2 align="center">🧮 عملیات و توابع عددی در NumPy</h2>

<table align="center" style="border-collapse: collapse; width: 70%; text-align: center;">
  <thead>
    <tr style="background-color: #1f2937; color: #f9fafb;">
      <th style="border: 1px solid #ddd; padding: 8px;">عملیات</th>
      <th style="border: 1px solid #ddd; padding: 8px;">مثال</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;">جمع</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>a + b</code>, <code>a + 5</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;">تفریق</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>a - b</code></td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;">ضرب</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>a * b</code>, <code>a * 2</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;">تقسیم</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>a / b</code></td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;">توان</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>a ** 2</code></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;">توابع</td>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.sqrt(a)</code>, <code>np.exp(a)</code>, <code>np.log(a)</code></td>
    </tr>
  </tbody>
</table>

<h2 align="center">📊 توابع آماری در NumPy</h2>

<table align="center" style="border-collapse: collapse; width: 75%; text-align: center;">
  <thead>
    <tr style="background-color: #1f2937; color: #f9fafb;">
      <th style="border: 1px solid #ddd; padding: 8px;">دستور</th>
      <th style="border: 1px solid #ddd; padding: 8px;">توضیح</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.sum(arr)</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">جمع تمام عناصر آرایه</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.mean(arr)</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">میانگین عناصر</td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.median(arr)</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">میانه داده‌ها</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.std(arr)</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">انحراف معیار داده‌ها</td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.min()</code>, <code>np.max()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">به ترتیب کمینه و بیشینه مقدار در آرایه</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.argmax()</code>, <code>np.argmin()</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">اندیس (موقعیت) بیشینه و کمینه مقدار</td>
    </tr>
  </tbody>
</table>

<h2 align="center">🧠 عملیات ماتریسی در NumPy</h2>

<table align="center" style="border-collapse: collapse; width: 75%; text-align: center;">
  <thead>
    <tr style="background-color: #1f2937; color: #f9fafb;">
      <th style="border: 1px solid #ddd; padding: 8px;">دستور</th>
      <th style="border: 1px solid #ddd; padding: 8px;">توضیح</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.dot(a, b)</code> یا <code>a @ b</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">ضرب ماتریسی بین دو آرایه</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.transpose(a)</code> یا <code>a.T</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">ترانهاده (جابجایی سطر و ستون‌ها)</td>
    </tr>
    <tr style="background-color: #f3f4f6;">
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.linalg.inv(A)</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">معکوس ماتریس (در صورت وجود)</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><code>np.linalg.det(A)</code></td>
      <td style="border: 1px solid #ddd; padding: 8px;">محاسبه دترمینان ماتریس</td>
    </tr>
  </tbody>
</table>





 

