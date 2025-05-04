
import streamlit as st

# Title
st.title("Transitioning Patients from Level 3 to Level 4")

st.markdown("This assessment evaluates patient eligibility for transitioning from Level 3 to Level 4 care based on clinical scales, objective parameters, and underlying conditions.")

# === CLINICAL CONDITIONS ===
st.header("Underlying Clinical Conditions (select all that apply)")

conditions = [
    "Heart Failure (HF)",
    "Pulmonary Disease",
    "Chronic Kidney Disease (CKD)",
    "Cancer Diagnosis",
    "Liver Cirrhosis",
    "Dementia/Stroke",
    "HIV"
]

selected_conditions = st.multiselect("Select applicable conditions:", conditions)

# === CONDITION-SPECIFIC FOLLOW-UP QUESTIONS ===
st.subheader("Condition-Specific Details")

ef = oxygen_dependent = on_dialysis = ""
cancer_flags = liver_flags = dementia_flags = []
cd4_count = None

if "Heart Failure (HF)" in selected_conditions:
    ef = st.text_input("Heart Failure: Enter ejection fraction (EF) within last year (%)")

if "Pulmonary Disease" in selected_conditions:
    oxygen_dependent = st.radio("Pulmonary Disease: Is the patient dependent on supplemental oxygen?", ["Yes", "No"])

if "Chronic Kidney Disease (CKD)" in selected_conditions:
    on_dialysis = st.radio("CKD: Is the patient on dialysis?", ["Yes", "No"])

if "Cancer Diagnosis" in selected_conditions:
    cancer_flags = st.multiselect(
        "Cancer: Select all that apply",
        ["Pleural effusion", "Transfusion requirement"]
    )

if "Liver Cirrhosis" in selected_conditions:
    liver_flags = st.multiselect(
        "Liver Cirrhosis: Select complications present",
        [
            "Ascites", 
            "Hepatic encephalopathy", 
            "Variceal bleeding",
            "Hepatorenal syndrome",
            "Spontaneous bacterial peritonitis"
        ]
    )

if "Dementia/Stroke" in selected_conditions:
    dementia_flags = st.multiselect(
        "Dementia/Stroke: Select all complications present",
        [
            "Aspiration pneumonia",
            "Pyelonephritis/septicemia",
            "Pressure ulcers",
            "Recurrent falls"
        ]
    )

if "HIV" in selected_conditions:
    cd4_count = st.number_input("HIV: Enter most recent CD4 count", min_value=0, step=1)

# === GROUP 1: CLINICAL SCALES ===
st.header("Group 1: Clinical Scales")

pps = st.slider("Palliative Performance Scale (PPS) %", 0, 100, step=10)
nyha = st.selectbox("NYHA Class", ["I", "II", "III", "IV"])
mmrc = st.selectbox("mMRC Dyspnea Scale", ["0", "1", "2", "3", "4"])
fast_scale = st.selectbox("FAST Scale (Dementia Severity)", ["1", "2", "3", "4", "5", "6", "7"])

# === GROUP 2: VITALS & LABS ===
st.header("Group 2: Vitals and Laboratory Values")

bp = st.text_input("Blood Pressure (e.g., 110/70)")
current_weight = st.number_input("Current Weight (kg)", min_value=0.0, step=0.1)
weight_earlier = st.number_input("Weight 6–12 Months Ago (kg)", min_value=0.0, step=0.1)
inr = st.number_input("INR", min_value=0.0, step=0.1)
albumin = st.number_input("Serum Albumin (g/dL)", min_value=0.0, step=0.1)

# === CALCULATION AND ASSESSMENT ===
st.header("Assessment Summary")
summary = []

# Clinical condition summary
if selected_conditions:
    summary.append(f"• Clinical conditions present: {', '.join(selected_conditions)}.")
else:
    summary.append("• No underlying clinical conditions were selected.")

# Append condition-specific details to summary
if "Heart Failure (HF)" in selected_conditions and ef:
    summary.append(f"• HF with EF: {ef}%")

if "Pulmonary Disease" in selected_conditions:
    summary.append(f"• Pulmonary Disease: Oxygen dependent - {oxygen_dependent}")

if "Chronic Kidney Disease (CKD)" in selected_conditions:
    summary.append(f"• CKD: On dialysis - {on_dialysis}")

if "Cancer Diagnosis" in selected_conditions and cancer_flags:
    summary.append(f"• Cancer complications: {', '.join(cancer_flags)}")

if "Liver Cirrhosis" in selected_conditions and liver_flags:
    summary.append(f"• Liver Cirrhosis complications: {', '.join(liver_flags)}")

if "Dementia/Stroke" in selected_conditions and dementia_flags:
    summary.append(f"• Dementia/Stroke complications: {', '.join(dementia_flags)}")

if "HIV" in selected_conditions and cd4_count is not None:
    summary.append(f"• HIV: CD4 count = {cd4_count}")

# Group 1 interpretations
if pps <= 40:
    summary.append(f"• PPS score of {pps}% indicates poor functional status.")
if nyha == "IV":
    summary.append("• NYHA Class IV indicates severe cardiac limitation.")
if mmrc in ["3", "4"]:
    summary.append(f"• mMRC score of {mmrc} suggests significant dyspnea.")
if fast_scale in ["6", "7"]:
    summary.append(f"• FAST scale of {fast_scale} indicates moderate to severe dementia.")

# Group 2 interpretations
if weight_earlier > 0 and current_weight < weight_earlier:
    weight_loss_pct = ((weight_earlier - current_weight) / weight_earlier) * 100
    summary.append(f"• Weight loss of {weight_loss_pct:.1f}% over 6–12 months.")
else:
    weight_loss_pct = 0

if inr > 1.5:
    summary.append(f"• Elevated INR of {inr}, which may reflect hepatic dysfunction or anticoagulation risk.")

if albumin < 3.0:
    summary.append(f"• Low albumin level of {albumin} g/dL suggests poor nutritional or hepatic status.")

# === RECOMMENDATION LOGIC ===
st.subheader("Recommendation")

force_transition = False
reason_lines = []

# Condition 1: PPS ≤ 50% and (≥10% weight loss or albumin < 2.5)
if pps <= 50:
    weight_flag = weight_loss_pct >= 10
    albumin_flag = albumin < 2.5
    if weight_flag or albumin_flag:
        force_transition = True
        reason_lines.append(
            f"• PPS is {pps}% and {'≥10% weight loss' if weight_flag else ''}"
            f"{' and ' if weight_flag and albumin_flag else ''}"
            f"{'albumin < 2.5 g/dL' if albumin_flag else ''}."
        )

# Condition 2: HF and (NYHA IV or EF ≤ 20)
if "Heart Failure (HF)" in selected_conditions:
    ef_val = None
    try:
        ef_val = float(ef)
    except:
        ef_val = None
    if nyha == "IV":
        force_transition = True
        reason_lines.append("• HF with NYHA Class IV.")
    if ef_val is not None and ef_val <= 20:
        force_transition = True
        reason_lines.append(f"• HF with EF ≤ 20% (EF = {ef_val}%).")

# Condition 3: Pulmonary Disease, mMRC = 4, and oxygen dependent
if "Pulmonary Disease" in selected_conditions and mmrc == "4" and oxygen_dependent == "Yes":
    force_transition = True
    reason_lines.append("• Severe pulmonary disease: mMRC = 4 and oxygen dependent.")

# Condition 4: CKD with eGFR ≤ 15 and not on dialysis
if "Chronic Kidney Disease (CKD)" in selected_conditions:
    if on_dialysis == "No":
        try:
            gfr_val = float(egfr_input)
        except:
            gfr_val = 0
        if gfr_val <= 15:
            force_transition = True
            reason_lines.append("• CKD with eGFR ≤ 15 and not on dialysis.")

# Condition 5: Cancer with PPS ≤ 70 or complications
if "Cancer Diagnosis" in selected_conditions:
    if pps <= 70 or cancer_flags:
        force_transition = True
        detail = f"PPS = {pps}%" if pps <= 70 else ""
        detail += " and " if pps <= 70 and cancer_flags else ""
        detail += f"complications: {', '.join(cancer_flags)}" if cancer_flags else ""
        reason_lines.append(f"• Cancer diagnosis with {detail}.")

# Condition 6: Liver Cirrhosis with INR > 1.5, albumin < 2.5, and any complication
if "Liver Cirrhosis" in selected_conditions:
    if inr >= 1.5 and albumin <= 2.5 and liver_flags:
        force_transition = True
        reason_lines.append(
            f"• Decompensated liver cirrhosis: INR = {inr}, albumin = {albumin}, complications: {', '.join(liver_flags)}."
        )

# Condition 7: Dementia/Stroke with FAST stage 7 and complications
if "Dementia/Stroke" in selected_conditions:
    if fast_scale == "7" and dementia_flags:
        force_transition = True
        reason_lines.append(
            f"• End-stage dementia or stroke: FAST stage 7 with complications: {', '.join(dementia_flags)}."
        )

# ✅ Condition 8: HIV with CD4 ≤ 200 and PPS ≤ 50%
if "HIV" in selected_conditions:
    if cd4_count is not None and cd4_count <= 200 and pps <= 50:
        force_transition = True
        reason_lines.append(f"• Advanced HIV: CD4 = {cd4_count}, PPS = {pps}%.")

# Output final decision
if force_transition:
    st.markdown("🔴 **High-risk criteria met — recommend transitioning to Level 4 care.**")
    st.markdown("#### Justification:")
    for r in reason_lines:
        st.markdown(r)
else:
    flags = 0
    if pps <= 40: flags += 1
    if nyha == "IV": flags += 1
    if mmrc in ["3", "4"]: flags += 1
    if fast_scale in ["6", "7"]: flags += 1
    if weight_loss_pct >= 10: flags += 1
    if albumin < 3.0: flags += 1
    if inr > 1.5: flags += 1
    if selected_conditions: flags += 1

    if flags >= 4:
        st.markdown("🟠 **Patient meets multiple criteria — consider transitioning to Level 4 care.**")
    elif 2 <= flags < 4:
        st.markdown("🔵 **Partial criteria met — monitor closely and reassess periodically.**")
    else:
        st.markdown("🟢 **Patient is stable — continue Level 3 care.**")

