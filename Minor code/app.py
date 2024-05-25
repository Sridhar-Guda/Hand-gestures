import streamlit as st
import subprocess

def main():
    st.title("Hand Gesture Recognition using OpenCV, TensorFlow, and MediaPipe")

    # Add a selector for the app mode on the sidebar
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["","About the project", "Run the project"])
    if app_mode == "About the project":
        st.write("""
        This project is about recognizing hand gestures using OpenCV, TensorFlow, and MediaPipe.
        The system captures video input, processes each frame to detect hand landmarks,
        and then uses a trained model to predict the gesture being made.
        """)
    elif app_mode == "Run the project":
        if st.button("Start"):
            run_project_script()

def run_project_script():
    st.text("Running Hand Gesture Recognition script...")
    try:
        # Run the Code.py script using subprocess
        subprocess.run(["python", "Code.py"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        st.error(f"An error occurred: {e.stderr}")
    else:
        st.success("Hand Gesture Recognition script executed successfully.")

if __name__ == "__main__":
    main()