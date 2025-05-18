import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

def init_session_state():
    """Initialize session state variables."""
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame()

def main():
    try:
        # Initialize session state
        init_session_state()

        # Page config
        st.set_page_config(
            page_title="${{ values.name }}",
            page_icon="🚀",
            layout="wide"
        )

        # Header
        st.title("${{ values.name }}")
        st.write("${{ values.description }}")

        # Sidebar
        with st.sidebar:
            st.header("Settings")
            theme = st.selectbox(
                "Choose Theme",
                ["Light", "Dark"],
                index=0
            )
            st.session_state.counter = st.number_input(
                "Counter",
                min_value=0,
                value=st.session_state.counter
            )

        # Main content
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Input Section")
            user_input = st.text_input("Enter your name")
            if user_input:
                st.success(f"Hello, {user_input}! 👋")
                st.session_state.counter += 1

        with col2:
            st.subheader("Data Visualization")
            # Generate sample data
            data = pd.DataFrame({
                'date': pd.date_range(start='2024-01-01', periods=20),
                'value': np.random.randn(20).cumsum()
            })
            st.line_chart(data.set_index('date'))

        # Footer
        st.markdown("---")
        st.markdown(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("Please try refreshing the page or contact support if the issue persists.")

if __name__ == "__main__":
    main()
