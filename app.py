import streamlit as st
from factorial import fact

def main():
    st.title("Tính Giai Thừa")

    number = st.number_input("Nhập số để tính giai thừa:", min_value=0, max_value=900, step=1)

    if st.button("Tính toán"):
        result = fact(number)
        st.write(f"Giai thừa của {number} là {result}")

if __name__ == "__main__":
    main()
