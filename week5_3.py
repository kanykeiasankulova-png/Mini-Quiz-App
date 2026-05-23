import streamlit as st

st.set_page_config(page_title="Mini Quiz App", layout="wide")

st.title("Quiz")
st.write("Quiz App")

questions = [
    {
        "question": "1.What is capital of Malaysia?",
    "options": ["Penang", "Punjabi", "Kua Lumpur"],
        "answer": "Punjabi"
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "3. What is 12 × 8?",
        "options": ["86", "96", "106", "116"],
        "answer": "96"
    }
]

answer = []

for i, q in enumerate(questions):
    st.subheader(q["question"])
    choice = st.radio(f"Select your answer {i+1}", q["options"], index=None, key=f"q{i}", label_visibility="collapsed")
    answer.append(choice)

    if i < len(questions)-1:
        st.divider()

st.divider()

if st.button("Submit", use_container_width=True):
    if None in answer:
        st.warning("You have not selected any answer")
    else:
        score = 0
        st.subheader(f"Your score is {score}")

        for i, q in enumerate(questions):
            if answer[i] == q["answer"]:
                st.success(f"Your answer is {q['options'][i]}")
                score += 1
            else:
                st.error(f"Your answer is {q['options'][i]}")

                st.divider()

                if score == 3:
                    st.balloons()
                    st.success(f"Perfect! Your score is {score}")
                elif score == 2:
                    st.info(f"Good!Your score is {score}")
                elif score == 1:
                    st.warning(f"You can better!Your score is {score}")
                else:
                    st.error(f"Try again!Your score is {score}")
