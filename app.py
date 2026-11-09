import streamlit as st

# ปรับตั้งค่าหน้าเว็บให้แสดงผลสวยงามและรองรับ Responsive
st.set_page_config(layout="centered")

# โค้ด HTML + CSS ของคุณ
html_code = """
<style>
   /* คุณสามารถใส่ CSS จากไฟล์ style.css มาไว้ตรงนี้ได้เลย */
   body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f0f2f5;
   }
   .card {
      background: white;
      padding: 24px;
      border-radius: 12px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      max-width: 500px;
      margin: 20px auto;
   }
   h1 { color: #1e293b; }
   h2 { color: #0f172a; margin-top: 20px; }
   b { color: #2563eb; }
   ul { padding-left: 20px; }
   li { margin-bottom: 8px; }
   img { border-radius: 8px; margin-top: 15px; display: block; }
   a { color: #2563eb; text-decoration: none; font-weight: bold; }
   a:hover { text-decoration: underline; }
</style>

<div class="card">
  <h1>hello ผมชื่อปาย เลขที่32</h1>
  <hr>
  <h2>เกี่ยวกับฉัน</h2>
  <!-- แก้แท็กปิดจาก <b> เป็น </b> -->
  <p>เรียนอยู่ชั้น ม.4/5 แผนการเรียน <b>Gifted Computer</b></p>
  <p>ชอบเล่นเกมและวิเคราะห์เกม</p>
  <h2>งานอดิเรก</h2>
  <ul>
    <li>เล่นเกม</li>
    <li>ดูหนังการ์ตูน</li>
    <li>ฟังเพลง</li>
  </ul>
  <img src="https://solver.yupparaj.ac.th/uploads/avatars/students/54808.webp?v=1791100162" alt="รูปของฉัน" width="200">
  <br>
  <a href="https://github.com/NuTTo-o" target="_blank">GitHub ของ me</a>
</div>
"""

# สั่งให้ Streamlit นำโค้ด HTML ไปแสดงผลบนหน้าเว็บ (กำหนดความสูงความกว้างตามต้องการ)
st.components.v1.html(html_code, height=650, scrolling=True)
