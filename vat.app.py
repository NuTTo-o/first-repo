import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
vat = price * 0.07
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
net_price = price - vat
st.write("นายภูเก็ต ชมภูมิ่ง ม.4/5")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
