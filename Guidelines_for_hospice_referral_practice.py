import streamlit as st 

# Title 
st.title("Hospice Clinical Eligibility Assessment") 

st.markdown("Disclaimer: This application is intended for educational and informational purposes only. It is designed to help users understand clinical concepts and care frameworks. It does not provide medical diagnosis, treatment recommendations, or personalized health guidance. Always consult a licensed healthcare professional for medical advice or care decisions.") 

# === CLINICAL CONDITIONS === 
st.header("Underlying Clinical Conditions (select all that apply)") 

conditions = [ 
    "Heart Failure (HF)", 
    "Pulmonary Disease", 
    "Chronic Kidney Disease (CKD)", 
    "Cancer Diagnosis", 
    "Liver Cirrhosis", 
    "Dementia/Stroke/Neurological Disease", 
    "HIV" 
] 

selected_conditions = st.multiselect("Select applicable conditions:", conditions)


    #===========================================================================================
# === CONDITION-SPECIFIC FOLLOW-UP QUESTIONS === 
st.subheader("Condition-Specific Details") 

ef = oxygen_dependent = on_dialysis = "" 
eGFR = None
cancer_flags = liver_flags = dementia_flags = [] 
cd4_count = viral_load = None

if "Heart Failure (HF)" in selected_conditions: 
    ef = st.text_input("Heart Failure: Enter ejection fraction (EF) within last year (%)") 

if "Pulmonary Disease" in selected_conditions: 
    oxygen_dependent = st.radio("Pulmonary Disease: Is the patient dependent on supplemental oxygen?", ["Yes", "No"]) 

if "Chronic Kidney Disease (CKD)" in selected_conditions: 
    on_dialysis = st.radio("CKD: Is the patient on dialysis?", ["Yes", "No"]) 
    

if "Cancer Diagnosis" in selected_conditions: 
    cancer_flags = st.multiselect( 
        "Cancer: Select all that apply", 
        ["Evidence of metastases", "Continued decline in spite of therapy","Declining therapy","Pleural effusion", "Transfusion requirement"] 
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

if "Dementia/Stroke/Neurological Disease" in selected_conditions: 
    dementia_flags = st.multiselect( 
        "Dementia/Stroke: Select all complications present", 
        [ 
            "Aspiration pneumonia", 
            "Pyelonephritis","septicemia", 
            "Pressure ulcers", 
            "Recurrent falls" 
        ] 
    ) 

if "HIV" in selected_conditions: 
    cd4_count = st.number_input("HIV: Enter most recent CD4 count (cells/mm³)", min_value=0, step=1)
    viral_load = st.number_input("HIV: Enter most recent viral load (virus per ml)", min_value=0, step=1)


# PPS always displayed
# === GROUP 1: CLINICAL SCALES ===
st.header("Group 1: Clinical Scales")

# --- PALLIATIVE PERFORMANCE SCALE (PPS) LOGIC ---
pps = None
ambulation = st.selectbox("PPS: What is the ambulation status?", [
    "Full", 
    "Reduced", 
    "Mainly Sit/Lie", 
    "Totally Bed Bound"
])

if ambulation == "Full":
    disease_status = st.selectbox(
        "Select the patient's disease status:",
        [
            "Normal activity, no evidence of disease",
            "Normal activity, some evidence of disease",
            "Normal activity with effort, some evidence of disease"
        ]
    )
    if disease_status == "Normal activity, no evidence of disease":
        pps = 100
    elif disease_status == "Normal activity, some evidence of disease":
        pps = "90"
    elif disease_status == "Normal activity with effort, some evidence of disease":
        pps = "80"

elif ambulation == "Reduced":
    unable_normal_work = st.radio("Unable to do normal work?", ["Yes", "No"])
    unable_hobby_care = st.radio("Unable to do hobbies/housework and needs occasional assistance in self-care?", ["Yes", "No"])
    if unable_hobby_care == "Yes":
        pps = "60"
    elif unable_normal_work == "Yes":
        pps = "70"
    

elif ambulation == "Mainly Sit/Lie":
    needs_assistance = st.radio("Need considerable assistance in self-care?", ["Yes", "No"])
    mainly_assisted = st.radio("Mainly assisted in self-care?", ["Yes", "No"])
    if mainly_assisted == "Yes":
        pps = "40"
    elif needs_assistance == "Yes":
        pps = "50"

elif ambulation == "Totally Bed Bound":
    intake = st.selectbox("What is the intake level?", [
        "Normal or reduced",
        "Minimal to sips",
        "Mouth care only"
    ])
    if intake == "Normal or reduced":
        pps = "30"
    elif intake == "Minimal to sips":
        pps = "20"
    elif intake == "Mouth care only":
        pps = "10"

if pps is not None:
    st.success(f"Calculated PPS Score: {pps}%")
pps = int(pps)






#============================================
# --- NYHA CLASS LOGIC (Only if Heart Failure is selected) ---
nyha = None
if "Heart Failure (HF)" in selected_conditions:
    nyha_description = st.selectbox("NYHA Classification: Select the description that best fits the patient:", [
        "No limitation of physical activity; ordinary physical activity does not cause undue fatigue, palpitation, or dyspnea",
        "Slight limitation of physical activity; comfortable at rest; ordinary physical activity results in fatigue, palpitation, or dyspnea",
        "Marked limitation of physical activity, comfortable at rest; less than ordinary activity causes fatigue, palpitation or dyspnea",
        "Unable to carry on any physical activity without discomfort; symptoms of heart failure at rest; if any physical activity is undertaken, discomfort increases"
    ])

    if nyha_description == "No limitation of physical activity; ordinary physical activity does not cause undue fatigue, palpitation, or dyspnea":
        nyha = "NYHA Class I"
    elif nyha_description == "Slight limitation of physical activity; comfortable at rest; ordinary physical activity results in fatigue, palpitation, or dyspnea":
        nyha = "NYHA Class II"
    elif nyha_description == "Marked limitation of physical activity, comfortable at rest; less than ordinary activity causes fatigue, palpitation or dyspnea":
        nyha = "NYHA Class III"
    elif nyha_description == "Unable to carry on any physical activity without discomfort; symptoms of heart failure at rest; if any physical activity is undertaken, discomfort increases":
        nyha = "NYHA Class IV"

    st.success(f"Determined NYHA Classification: {nyha}")

# --- mMRC DYSPNEA SCALE (Only if Pulmonary Disease is selected) ---
mmrc = None
if "Pulmonary Disease" in selected_conditions:
    mmrc_description = st.selectbox("mMRC Dyspnea Scale: Select the description that best fits the patient:", [
        "Dyspnea only with strenuous exercise",
        "Dyspnea when hurrying or walking up a slight hill",
        "Walks slower than people of same age due to dyspnea or has to stop for breath when walking at own pace",
        "Stops for breath after walking 100 meters or after a few minutes on level ground",
        "Too dyspneic to leave house or breathless when dressing"
    ])

    if mmrc_description == "Dyspnea only with strenuous exercise":
        mmrc = "mMRC Grade 0"
    elif mmrc_description == "Dyspnea when hurrying or walking up a slight hill":
        mmrc = "mMRC Grade 1"
    elif mmrc_description == "Walks slower than people of same age due to dyspnea or has to stop for breath when walking at own pace":
        mmrc = "mMRC Grade 2"
    elif mmrc_description == "Stops for breath after walking 100 meters or after a few minutes on level ground":
        mmrc = "mMRC Grade 3"
    elif mmrc_description == "Too dyspneic to leave house or breathless when dressing":
        mmrc = "mMRC Grade 4"

    st.success(f"Determined mMRC Dyspnea Scale: {mmrc}")

# --- FAST SCALE (Only if Dementia/Stroke/Neurological Disease is selected) ---
fast_scale = None
if "Dementia/Stroke/Neurological Disease" in selected_conditions:
    fast_stage_description = st.selectbox("FAST Scale: Select the stage that best matches the patient:", [
        "Normal adult with no functional decline",
        "Subjective functional deficit",
        "Objective functional deficit interfering with complex tasks",
        "Decreased ability to perform instrumental ADLs (e.g., finances, cooking, shopping)",
        "Requires assistance with choosing proper clothing",
        "Requires assistance with dressing, bathing, or toileting",
        "Incontinence, minimal to no speech, inability to walk"
    ])

    if fast_stage_description == "Normal adult with no functional decline":
        fast_scale = "FAST Stage 1"
    elif fast_stage_description == "Subjective functional deficit":
        fast_scale = "FAST Stage 2"
    elif fast_stage_description == "Objective functional deficit interfering with complex tasks":
        fast_scale = "FAST Stage 3"
    elif fast_stage_description == "Decreased ability to perform instrumental ADLs (e.g., finances, cooking, shopping)":
        fast_scale = "FAST Stage 4"
    elif fast_stage_description == "Requires assistance with choosing proper clothing":
        fast_scale = "FAST Stage 5"
    elif fast_stage_description == "Requires assistance with dressing, bathing, or toileting":
        fast_scale = "FAST Stage 6"
    elif fast_stage_description == "Incontinence, minimal to no speech, inability to walk":
        fast_scale = "FAST Stage 7"

    st.success(f"Determined FAST Scale: {fast_scale}")
# === GROUP 2: Weight and Laboratory Values ===
st.header("Group 2: Weight and Laboratory Values")

current_weight = st.number_input("Current Weight (kg)", min_value=0.0, step=0.1)
weight_earlier = st.number_input("Weight 6–12 Months Ago (kg)", min_value=0.0, step=0.1)

if current_weight:
    st.info(f"Entered Current Weight: {current_weight} kg")
if weight_earlier:
    st.info(f"Entered Past Weight: {weight_earlier} kg")

# Calculate and highlight weight loss trend
if current_weight and weight_earlier and weight_earlier > 0:
    weight_change_percent = ((weight_earlier - current_weight) / weight_earlier) * 100
    st.info(f"Weight Change: {weight_change_percent:.1f}%")
    if weight_change_percent >= 10:
        st.error("Significant weight loss (≥ 10%) detected")

# Liver Cirrhosis Labs
inr = albumin = None
if "Liver Cirrhosis" in selected_conditions:
    inr = st.number_input("INR", min_value=0.0, step=0.1)
    albumin = st.number_input("Serum Albumin (g/dL)", min_value=0.0, step=0.1)
    if inr:
        st.info(f"Entered INR: {inr}")
    if albumin:
        st.info(f"Entered Albumin: {albumin} g/dL")

# CKD Lab
egfr = None
if "Chronic Kidney Disease (CKD)" in selected_conditions:
    egfr = st.number_input("eGFR (ml/min/1.73 m²)", min_value=0.0, step=0.1)
    if egfr:
        st.info(f"Entered eGFR: {egfr} ml/min/1.73 m²")
# Dementia/Stroke/Neurological Disease Labs
inr = albumin = None
if "Dementia/Stroke/Neurological Disease" in selected_conditions:
    
    albumin = st.number_input("Serum Albumin (g/dL)", min_value=0.0, step=0.1)
    
    if albumin:
        st.info(f"Entered Albumin: {albumin} g/dL")


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

if "Dementia/Stroke/Neurological Disease" in selected_conditions and dementia_flags:
    summary.append(f"• Dementia/Stroke complications: {', '.join(dementia_flags)}")

if "HIV" in selected_conditions and cd4_count is not None:
    summary.append(f"• HIV: CD4 count = {cd4_count}")

# Group 1 interpretations
if pps <= 40:
    summary.append(f"• PPS score of {pps}% indicates poor functional status.")
if nyha == "NYHA Class IV":
    summary.append("• NYHA Class IV indicates severe cardiac limitation.")
if mmrc == "mMRC Grade 4":
    summary.append(f"• mMRC score of {mmrc} suggests significant dyspnea.")
if fast_scale == "FAST Stage 7":
    summary.append(f"• FAST scale of {fast_scale} indicates moderate to severe dementia.")

# Group 2 interpretations
if weight_earlier > 0 and current_weight < weight_earlier:
    weight_loss_pct = ((weight_earlier - current_weight) / weight_earlier) * 100
    summary.append(f"• Weight loss of {weight_loss_pct:.1f}% over 6–12 months.")
else:
    weight_loss_pct = 0

if inr is not None and inr > 1.5:
    summary.append(f"• Elevated INR of {inr}, which may reflect hepatic dysfunction or anticoagulation risk.")

if albumin is not None and albumin < 2.5 :
    summary.append(f"• Low albumin level of {albumin} g/dL suggests poor nutritional or hepatic status.")

for item in summary:
    st.markdown(item)

# === RECOMMENDATION LOGIC ===
st.subheader("Recommendation")

force_transition = False
reason_lines = []

# Condition 1: PPS ≤ 50% and (≥10% weight loss or albumin < 2.5)
if pps <= 50:
    weight_flag = weight_loss_pct >= 10
    albumin_flag = albumin and albumin < 2.5
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
    if nyha == "NYHA Class IV":
        force_transition = True
        reason_lines.append("• HF with NYHA Class IV.")
    if ef_val is not None and ef_val <= 20:
        force_transition = True
        reason_lines.append(f"• HF with EF ≤ 20% (EF = {ef_val}%).")

# Condition 3: Pulmonary Disease, mMRC = 4, and oxygen dependent
if "Pulmonary Disease" in selected_conditions and mmrc == "mMRC Grade 4" and oxygen_dependent == "Yes":
    force_transition = True
    reason_lines.append("• Severe pulmonary disease: mMRC = 4 and oxygen dependent.")

# Condition 4: CKD with eGFR ≤ 15 and not on dialysis
if "Chronic Kidney Disease (CKD)" in selected_conditions:
    if on_dialysis == "No":
        try:
            gfr_val = float(egfr)
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
    if inr is not None and inr >= 1.5 and albumin is not None and albumin <= 2.5 and liver_flags:
        force_transition = True
        reason_lines.append(
            f"• Decompensated liver cirrhosis: INR = {inr}, albumin = {albumin}, complications: {', '.join(liver_flags)}."
        )

# Condition 7: Dementia/Stroke with FAST stage 7 and complications
if "Dementia/Stroke/Neurological Disease" in selected_conditions:
    if fast_scale == "FAST Stage 7" and dementia_flags:
        force_transition = True
        reason_lines.append(
            f"• End-stage dementia or stroke: FAST stage 7 with complications: {', '.join(dementia_flags)}."
        )

# Condition 8: HIV with CD4 ≤ 200 and PPS ≤ 50%
if "HIV" in selected_conditions:
    if cd4_count is not None and cd4_count <= 200 and pps <= 50:
        force_transition = True
        reason_lines.append(f"• Advanced HIV: CD4 = {cd4_count}, PPS = {pps}%.")

# Output final decision
if force_transition:
    st.markdown("🔴 **A respectful way to begin an end-of-life conversation is to ask permission to discuss future care preferences, emphasizing that the goal is to ensure the patient’s values and wishes guide their care.**")
    st.markdown("#### Justification:")
    for r in reason_lines:
        st.markdown(r)
else:
    flags = 0
    if pps <= 40: flags += 1
    if nyha == "NYHA Class IV": flags += 1
    if mmrc in ["3", "4"]: flags += 1
    if fast_scale in ["6", "7"]: flags += 1
    if weight_loss_pct >= 10: flags += 1
    if albumin and albumin < 3.0: flags += 1
    if inr and inr > 1.5: flags += 1
    if selected_conditions: flags += 1

    if flags >= 4:
        st.markdown("🟠 **Patient meets multiple criteria- A respectful way to begin an end-of-life conversation is to ask permission to discuss future care preferences, emphasizing that the goal is to ensure the patient’s values and wishes guide their care.**")
    elif 2 <= flags < 4:
        st.markdown("🔵 **Partial criteria met — monitor closely and reassess periodically.**")
    else:
        st.markdown("🟢 **Based on the available information, the patient does not meet the clinical criteria for hospice care**")