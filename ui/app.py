import streamlit as st
from agent.rag_agent import run_rag_agent

st.set_page_config(page_title="IAM Agent", layout="wide")

st.title("IAM Decision Agent")

st.markdown("""
This UI simulates:
- End User
- IAM Decision Agent
- IAM Security Agent
""")

user_input = st.text_input("Enter request")

if st.button("Submit"):

    if user_input:

        response = run_rag_agent(user_input)

        st.subheader("IAM Decision Agent Response")

        # Main decision
        st.success(f"Decision: {response.get('decision').upper()}")

        # Risk
        st.warning(f"Risk Level: {response.get('risk')}")

        # Reason
        st.markdown("### Reason")
        st.write(response.get("reason"))

        # Tool info
        if response.get("tool"):
            st.markdown("### Tool Execution")
            st.code(response.get("tool"))

        # Tool result
        if response.get("tool_result"):
            st.markdown("### Tool Result")
            st.write(response.get("tool_result"))

        # Next step
        if response.get("next_step"):
            st.markdown("### Next Step")
            st.write(response.get("next_step"))

        # Planning steps
        if response.get("plan"):

            st.markdown("### Planning Steps")

            for idx, step in enumerate(response["plan"], start=1):
                st.write(f"{idx}. {step}")

        # Personas
        st.markdown("### Personas Involved")

        st.info("End User → Submitted access request")
        st.info("IAM Decision Agent → Evaluated request and coordinated workflow")
        st.info("IAM Security Agent → Applied policy and risk validation")

        # Full JSON
        with st.expander("View Full JSON Response"):
            st.json(response)
