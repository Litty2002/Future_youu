from random import choices

import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder, Normalizer


st.title(":red[Express Yourself]")


st.session_state['selected_data'] = {}


def get_other_jobs():
    ops = [
        'Software Quality Assurance (QA) / Testing',
        'Mobile Applications Developer',
        'Portal Administrator',
        'Project Manager',
        'Design & UX',
        'Technical Support',
        'Data Architect',
        'Database Developer',
        'Solutions Architect',
        'Software Developer',
        'Systems Security Administrator',
        'Quality Assurance Associate',
        'Software Systems Engineer',
        'Network Security Administrator',
        'Technical Services/Help Desk/Tech Support',
        'Information Security Analyst',
        'E-Commerce Analyst',
        'Technical Engineer',
        'Information Technology Auditor',
        'CRM Business Analyst',
        'Applications Developer',
        'Software Engineer',
        'CRM Technical Developer',
        'Database Manager',
        'Business Systems Analyst',
        'Database Administrator',
        'Network Engineer',
        'Web Developer',
        'Business Intelligence Analyst',
        'Systems Analyst',
        'UX Designer',
        'Information Technology Manager',
        'Programmer Analyst',
        'Network Security Engineer',
    ]

    return choices(ops, k=3)


def predict_job() -> str:
    global t
    # columns in order
    df = pd.read_csv('./roo_data.csv')
    columns_io = df.columns[:-1]

    data_df = pd.DataFrame({i: [st.session_state[i]] for i in columns_io})
    data = data_df.iloc[:, :].values
    label = df.iloc[:, -1].values

    label_encoder = LabelEncoder()
    for i in range(14, 38):
        data[:, i] = label_encoder.fit_transform(data[:, i])

    data1 = data[:, :14]
    normalized_data = Normalizer().fit_transform(data1)

    data2 = data[:, 14:]
    df1 = np.append(normalized_data, data2, axis=1)

    X1 = pd.DataFrame(df1, columns=columns_io)

    label_encoder = LabelEncoder()
    label_encoder.fit(label)

    with open('./model.joblib', 'rb') as f:
        model = joblib.load(f)

    X1 = pd.to_numeric(X1.values.flatten())
    X1 = X1.reshape((1, 38))

    a = model.predict(X1)

    st.session_state['prediction'] = label_encoder.inverse_transform(a)[0]
    st.session_state['suggestions'] = get_other_jobs()
    print(st.session_state['prediction'])


def on_submit() -> None:
    predict_job()


@st.cache_data
def get_options(csv_file: str) -> dict[str, str | list[str]]:
    data = pd.read_csv(csv_file)

    # col 0 to 13 are all number values
    options = {i: "num" for i in data.columns[:14]}

    a = {i: list(data[i].unique()) for i in data.columns[14:-1]}

    return {**options, **a}


options = get_options("roo_data.csv")

for option, val in options.items():
    if val == "num":
        st.number_input(label=option.strip().title(), min_value=0, max_value=100, step=1, key=option)

    else:
        st.selectbox(label=option.strip().title(), options=val, key=option)

if st.button("Get My Job"):
    on_submit()
    st.switch_page("pages/prediction.py")



