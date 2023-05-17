import streamlit as st

st.set_page_config(layout="wide")


# Using object notation
col1, col2 = st.columns(2)


#st.image("Logo.png")
st.title("Probabilistic Graphical Models")

st.write("This is a digital version of the notes I kept for Probabilistic Graphical Models (PGM) taught by [Jun. Prof. Dr. Sophie Fellenz](https://ml.cs.uni-kl.de) \
            at Rheinland-Pfälzische Technische Universität in Kaiserslautern, RP, Deutschland. The lecture series is written from \
            a storytelling perspective. The number of topics here do not correspond to the ones delivered by the professor to maintain a more thorough understanding. Hopefully, there will be good enough segues in these notes from one topic to another. The segues will help create a solid understanding of why a \
            particular topics needs to be in the lecture.")

st.write("If you want to contribute to the notes, please open an issue on the repository: [Probabilistic-Graphical-Models](https://github.com/rssr25/probabilistic-graphical-models)")

st.write("***")

st.header("Table of contents")

#TODO: Open them in the same page

col1, col2, col3 = st.columns(3)

with col1:
    st.write("[1. Bayesian Networks](1._Bayesian_Networks)")
    st.write("[2. Markov Random Fields](2._Markov_Random_Fields)")
    st.write("[3. Exact Inference and Belief Propagation ](3._Exact_Inference_and_Belief_Propagation)")
    st.write("[4. Parameter Learning ](4._Parameter_Learning)")
    st.write("[5. Mixture Models and EM Algorithm ](5._Mixture_Models_and_EM_Algorithm)")

with col2:
    st.write("[6. HMM and CRF ](6._HMM_and_CRF)")
    st.write("[7. Variational_Inference ](7._Variational_Inference)")
    st.write("[8. Sampling ](8._Sampling)")
    st.write("[9. Bayesian_Nonparametrics ](9._Bayesian_Nonparametrics)")
    st.write("[10. Structure_Learning ](10._Structure_Learning)")

with col3:
    st.write("[11. DNN_vs_GM ](11._DNN_vs_GM)")