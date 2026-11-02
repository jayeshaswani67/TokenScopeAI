
import streamlit as st
import pandas as pd
import plotly.express as px

from src.tokenizer import count_tokens
from src.cost_calculator import calculate_cost
from src.context_analyser import analyze_context


# ==========================================
# TOKENSCOPE AI
# AI Token & Cost Analytics Dashboard
# ==========================================

st.set_page_config(
    page_title="TokenScope AI",
    page_icon="🧠",
    layout="wide"
)


# ==========================================
# MODEL CONFIGURATION
# ==========================================

MODELS = {
    "GPT-4o": {
        "tokenizer": "gpt-4o",
        "input_price": 2.50,
        "output_price": 10.00,
        "context_window": 128000
    },
    "GPT-4o mini": {
        "tokenizer": "gpt-4o-mini",
        "input_price": 0.15,
        "output_price": 0.60,
        "context_window": 128000
    },
    "GPT-4.1": {
        "tokenizer": "gpt-4.1",
        "input_price": 2.00,
        "output_price": 8.00,
        "context_window": 1047576
    }
}


# ==========================================
# CUSTOM STYLING
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #0B1120;
    color: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
}

.metric-card {
    background-color: #151F32;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #263449;
}

.metric-title {
    color: #94A3B8;
    font-size: 14px;
}

.metric-value {
    color: #F8FAFC;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.title("🧠 TokenScope AI")

st.caption(
    "AI Token Estimation, Context Analysis "
    "and API Cost Intelligence"
)

st.divider()


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("⚙️ Configuration")

selected_model = st.sidebar.selectbox(
    "Select AI Model",
    list(MODELS.keys())
)

model_config = MODELS[selected_model]

st.sidebar.info(
    f"""
    **Model:** {selected_model}

    **Context Window:** 
    {model_config['context_window']:,} tokens

    **Input Price:** 
    ${model_config['input_price']} / 1M tokens

    **Output Price:** 
    ${model_config['output_price']} / 1M tokens
    """
)

st.sidebar.caption(
    "Pricing is configurable and should be "
    "verified against current provider pricing."
)


# ==========================================
# PROMPT INPUT
# ==========================================

st.subheader("📝 Prompt Analyzer")

prompt = st.text_area(
    "Enter your AI prompt",
    height=180,
    placeholder=(
        "Example: Explain how artificial "
        "intelligence and neural networks work."
    )
)

col1, col2 = st.columns(2)

with col1:
    output_tokens = st.number_input(
        "Expected output tokens",
        min_value=0,
        max_value=1000000,
        value=500,
        step=100
    )

with col2:
    st.metric(
        "Selected Model",
        selected_model
    )


# ==========================================
# ANALYSIS
# ==========================================

if st.button(
    "🚀 Analyze Prompt",
    use_container_width=True
):

    if not prompt.strip():

        st.warning(
            "Please enter a prompt before analysis."
        )

    else:

        # Token count
        input_tokens = count_tokens(
            prompt,
            model_config["tokenizer"]
        )

        # Cost calculation
        cost_data = calculate_cost(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            input_price=model_config["input_price"],
            output_price=model_config["output_price"]
        )

        # Context analysis
        context_data = analyze_context(
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            context_window=model_config["context_window"]
        )

        # Store results
        st.session_state["analysis"] = {
            "prompt": prompt,
            "model": selected_model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost_data,
            "context": context_data
        }


# ==========================================
# RESULTS DASHBOARD
# ==========================================

if "analysis" in st.session_state:

    result = st.session_state["analysis"]

    input_tokens = result["input_tokens"]
    output_tokens = result["output_tokens"]

    cost_data = result["cost"]
    context_data = result["context"]

    total_tokens = context_data["total_tokens"]

    st.divider()

    st.subheader("📊 Analysis Results")


    # --------------------------------------
    # METRICS
    # --------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Input Tokens",
            f"{input_tokens:,}"
        )

    with col2:

        st.metric(
            "Output Tokens",
            f"{output_tokens:,}"
        )

    with col3:

        st.metric(
            "Total Tokens",
            f"{total_tokens:,}"
        )

    with col4:

        st.metric(
            "Estimated Cost",
            f"${cost_data['total_cost']:.6f}"
        )


    # --------------------------------------
    # TOKEN VISUALIZATION
    # --------------------------------------

    st.subheader("Token Distribution")

    token_df = pd.DataFrame({
        "Category": [
            "Input Tokens",
            "Output Tokens"
        ],
        "Tokens": [
            input_tokens,
            output_tokens
        ]
    })

    fig_tokens = px.bar(
        token_df,
        x="Category",
        y="Tokens",
        color="Category",
        text="Tokens",
        title="Input vs Output Token Usage"
    )

    fig_tokens.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        showlegend=False
    )

    st.plotly_chart(
        fig_tokens,
        use_container_width=True
    )


    # --------------------------------------
    # COST VISUALIZATION
    # --------------------------------------

    st.subheader("💰 Cost Analysis")

    cost_df = pd.DataFrame({
        "Category": [
            "Input Cost",
            "Output Cost"
        ],
        "Cost": [
            cost_data["input_cost"],
            cost_data["output_cost"]
        ]
    })

    fig_cost = px.pie(
        cost_df,
        names="Category",
        values="Cost",
        title="API Cost Distribution",
        hole=0.5
    )

    fig_cost.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0B1120"
    )

    st.plotly_chart(
        fig_cost,
        use_container_width=True
    )


    # --------------------------------------
    # CONTEXT WINDOW
    # --------------------------------------

    st.subheader("🧠 Context Window Analysis")

    usage_percentage = min(
        context_data["usage_percentage"],
        100
    )

    st.progress(
        usage_percentage / 100
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Context Usage",
            f"{context_data['usage_percentage']:.2f}%"
        )

    with col2:

        st.metric(
            "Remaining Tokens",
            f"{context_data['remaining_tokens']:,}"
        )

    with col3:

        st.metric(
            "Status",
            context_data["status"]
        )

    if context_data["exceeds_limit"]:

        st.error(
            "Context window exceeded. "
            "Reduce input or output tokens."
        )

    elif context_data["status"] == "Critical":

        st.warning(
            "Context usage is above 90%."
        )

    elif context_data["status"] == "High":

        st.info(
            "Context usage is above 70%."
        )

    else:

        st.success(
            "Context usage is within a comfortable range."
        )


    # --------------------------------------
    # EXPORT RESULTS
    # --------------------------------------

    st.divider()

    st.subheader("📥 Export Analysis")

    export_df = pd.DataFrame({
        "Model": [result["model"]],
        "Input Tokens": [input_tokens],
        "Output Tokens": [output_tokens],
        "Total Tokens": [total_tokens],
        "Estimated Cost USD": [
            cost_data["total_cost"]
        ],
        "Context Usage %": [
            context_data["usage_percentage"]
        ]
    })

    csv_data = export_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download CSV Report",
        data=csv_data,
        file_name="tokenscope_analysis.csv",
        mime="text/csv"
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "TokenScope AI v0.2 | Built with Python, "
    "Streamlit, Plotly and tiktoken"
)
