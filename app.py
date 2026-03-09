import streamlit as st
import pandas as pd


st.set_page_config(page_title="Đọc Excel đơn giản", layout="wide")

st.title("📊 Ứng dụng đọc file Excel đơn giản")
st.write("Tải lên một file Excel để xem dữ liệu.")

uploaded_file = st.file_uploader("Chọn file Excel (.xlsx, .xls)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Đọc toàn bộ file để lấy danh sách sheet
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Chọn sheet
        sheet_name = st.selectbox("Chọn sheet", sheet_names)

        # Đọc dữ liệu sheet đã chọn
        df = pd.read_excel(excel_file, sheet_name=sheet_name)

        st.subheader(f"Dữ liệu trong sheet: {sheet_name}")
        st.dataframe(df, use_container_width=True)

        # Tùy chọn hiển thị thông tin cơ bản
        with st.expander("Thông tin dữ liệu"):
            st.write("**Số dòng:**", df.shape[0])
            st.write("**Số cột:**", df.shape[1])
            st.write("**Tên cột:**", list(df.columns))

    except Exception as e:
        st.error(f"Không thể đọc file Excel: {e}")
else:
    st.info("Vui lòng tải lên một file Excel để bắt đầu.")

