import streamlit as st
from factorial import fact

def main():
  st.title("Tinh giai thua")
  number = st.numner_inpurt("Tinh giai thua:", min_value=0, max_value = 900)
  if st.button("Calculate"):
    result = fact(number)
    st.write(f"Giai thua cua {number} la {result}")
  
if __name__ == "__main__":
    main()
