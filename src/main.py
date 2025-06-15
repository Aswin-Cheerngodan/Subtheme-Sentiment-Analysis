import streamlit as st
from inference import load_model, predict, map_predictions_to_labels

# Load model and tokenizer
MODEL_PATH = "models/fine_tuned_subtheme"  # Put this folder in the same dir as app
model, tokenizer = load_model(model_path=MODEL_PATH)
# List of subthemes (ensure order matches model output)
SUBTHEMES = ['garage service positive','value for money positive','ease of booking positive','location positive','length of fitting positive',
 'ease of booking negative','tyre quality positive','garage service negative','wait time negative',
 'delivery punctuality positive','wait time positive','location negative','damage negative',
 'extra charges positive','value for money negative','mobile fitter positive','advisor/agent service positive',
 'facilities positive','change of time negative','extra charges negative','late notice negative',
 'discounts positive','delivery punctuality negative','change of date negative','booking confusion negative',
 'advisoragent service positive','advisor/agent service negative','advisoragent service negative','incorrect tyres sent negative',
 'tyre quality negative','response time negative','refund positive','no stock negative',
 'change of date positive','call wait time negative', 'refund negative','length of fitting negative',
 'balancing negative', 'mobile fitter negative', 'discounts negative', 'response time positive']

# Streamlit UI
st.title("🧠 Car Garage Subtheme Sentiment Analyzer")
st.write("Enter a user review or sentence to detect the key subthemes:")

text = st.text_area("User Text", height=150, placeholder="E.g. The staff was helpful and the tyres were reasonably priced.")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Predict
        indexes, probs = predict(text, model, tokenizer, threshold=0.2)
        threshold = 0.2

        results = [(SUBTHEMES[i], float(probs[i])) for i in range(len(probs)) if probs[i] >= threshold]

        if results:
            st.subheader("🔍 Detected Subthemes:")
            for subtheme, score in sorted(results, key=lambda x: -x[1]):
                st.write(f"**{subtheme.replace('_', ' ').title()}** — Confidence: {score:.2f}")
        else:
            st.info("No strong subthemes detected above the threshold.")

        # Optionally show all scores
        with st.expander("Show all subtheme scores"):
            for subtheme, score in zip(SUBTHEMES, probs):
                st.write(f"{subtheme.replace('_', ' ').title()}: {score:.2f}")
