import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Page",
    ["Single Location Weather", 
     "Compare Locations & KPIs", 
     "Variable Selection & Timezone",
     "Summary Metrics Across Cities"]
)

if page == "Single Location Weather":
    from pages.single_location import main
elif page == "Compare Locations & KPIs":
    from pages.compare_locations import main
elif page == "Variable Selection & Timezone":
    from pages.variable_selection import main
elif page == "Summary Metrics Across Cities":
    from pages.summary_metrics import main

main()
