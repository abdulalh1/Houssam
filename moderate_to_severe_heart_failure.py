import streamlit as st

# ============================================
# Progressive Decompensated Heart Failure Workflow
# ============================================
def show_title_and_disclaimer():
    st.title("Progressive Decompensated Heart Failure Workflow")
    st.markdown("""
    ---
    **DISCLAIMER:**  
    This application is for **educational and training purposes only**.  
    The protocol serves as a **general guideline** and **does not replace clinical judgment**.  
    Clinical decisions must always be individualized to each patient's unique situation.

    ℹ️ The acute heart failure episode is managed over a **6-day period**.  
    **Day 1** is the initial evaluation by the **Advanced Care Paramedic**.
    ---
    """)

# ================================
# Workflow Display Functions
# ================================
def triage_nurse_workflow(day):
    if day == "Day 1":
        st.subheader("Triage Nurse - Day 1 Responsibilities")
        st.markdown("""
1. After identifying and stratifying a patient with progressive moderate to severe symptoms, send a message to the Advanced Care Paramedic via Teams.  
   ➤ Include: NCCC, CRNP, and YC Physician.  
   ➤ Add the Cardiologist and Nephrologist if available in the Blue Sticky Note.

2. Upon receipt of the Medic’s Day 1 Summary via Teams:  
   a. Complete a summary in **Epic**.  
   b. Send a **priority telephonic encounter** to:  
      - NCCC  
      - CRNP  
      - YC Physician  
      - Scheduling  
      - Community Health Worker (CHW)
""")
    else:
        st.subheader("Triage Nurse - Day 2 Responsibilities")
        st.markdown("""
1. Upon receipt of the Medic’s Day 2 Summary in Teams:  
   a. Transfer the Day 2 summary to **Epic** as a **Priority Telephonic Encounter**.  
   b. Share with:  
      - NCCC  
      - CRNP  
      - YC Physician  
      - Community Health Worker (CHW)  
      - Scheduling
""")


def advanced_care_paramedic_workflow(day):
    if day == "Day 1":
        st.subheader("Advanced Care Paramedic - Day 1 Responsibilities")
        st.markdown("""
**Clinical Assessment & Treatment**  
1. Determine the need for IV loop diuretic.  
2. Order CBC, CMP, BNP, TSH, chest X-ray, EKG if necessary.  
3. Document historical & current weight.  
4. Take a clinical image of lower extremities and upload to Epic via **Haiku**.  
5. Provide tools to measure urine output (urinal/hat/graduated cylinder).  
6. Decide on leaving IV access (follow home IV policy).

**Communication**  
1. Confirm Day 2 follow-up method with patient/family.  
2. Leave a phone appointment card.  
3. Send Day 1 summary to the Triage Nurse via Teams.
""")
    else:
        st.subheader("Advanced Care Paramedic - Day 2 Responsibilities")
        st.markdown("""
**Follow-Up**  
1. Perform a follow-up phone call to the patient or family.  
2. Confirm response to treatment (**>3 lbs weight loss when possible**).  
3. Review testing results.  
4. Determine the need for a second-day medic's visit.  
5. Send Day 2 summary with recommendations to the Triage Nurse via Teams.

**If Unreachable**  
1. Request a **Community Health Worker (CHW)** to perform a wellness visit.
""")


def scheduling_coordinator_workflow(day):
    if day == "Day 1":
        st.subheader("Scheduling Coordinator - Day 1 Responsibilities")
        st.markdown("""
1. Upon receipt of the Medic’s Day 1 Summary via Teams (from Intake):  
   - Schedule in-person visit with **CRNP or YC Physician** on Day 2 (based on Zip Code distribution & availability).  
   - Schedule an **NCCC** in-person visit on Day 4.  
   - Add to **CRNP acute list** & **IDT weekly list**.  
   - Create an acute episode in the **Excel acute spreadsheet**.
""")
    else:
        st.subheader("Scheduling Coordinator - Day 6 Responsibilities")
        st.markdown("""
1. Upon receipt of the **NCCC message** via Epic:  
   - Close the acute episode in the **Excel acute spreadsheet**.
""")


def chw_workflow(day):
    if day == "Day 1":
        st.subheader("Community Health Worker - Day 1 Responsibilities")
        st.markdown("1. Plan to schedule a wellness visit on Day 2 if necessary.")
    else:
        st.subheader("Community Health Worker - Day 2 Responsibilities")
        st.markdown("""
1. Perform a wellness visit if the medics cannot reach the patient.  
2. Inform **Physician, CRNP, and NCCC** scheduled to see the patient of the visit’s outcome.
""")


def crnp_physician_workflow(day):
    if day == "Day 1":
        st.subheader("Physician / CRNP - Day 1 Responsibilities")
        st.markdown("""
- Upon receipt of Day 1 Medic's Summary (**priority telephonic message** in Epic):  
  **If an in-person visit is not scheduled on Day 2, schedule one.**  
- Share a brief of Day 1 Summary with **PCP, Cardiology, and Nephrology**.  
- Inform them of the planned in-person visit on Day 2.
""")
    elif day == "Day 2":
        st.subheader("Physician / CRNP - Day 2 (In-Person Visit Goals)")
        st.markdown("""
1. Assess response to treatment (**symptoms, weight, urine output**).  
2. Take a clinical image of lower extremities, upload to Epic via **Haiku**.  
3. Review labs ordered by medics on Day 1.  
4. Review hospitalist recommendations.  
5. Place a request for a **STAT lab** on Day 4 (**CBC, CMP, BMP, BNP, Mg, TSH**).  
6. Initiate goals-of-care discussion; identify end-of-life patients.  
7. Notify the **Clinical Operations Manager** to add to the end-of-life workflow (**Epic Staff message**).  
8. Update **NCCC, PCP, Cardiology, and Nephrology**.
""")
    else:
        st.subheader("Physician / CRNP - Day 5 Responsibilities")
        st.markdown("""
1. Review lab results and discuss with the patient or family.  
2. Share findings with **NCCC, PCP, Cardiology, and Nephrology**.  
3. Schedule a **routine follow-up visit**.
""")


def nccc_workflow(day):
    if day == "Day 1":
        st.subheader("NCCC - Day 1 Responsibilities")
        st.markdown("""
- Upon receipt of Day 1 Medic's Summary (**priority telephonic encounter**):  
  ▪ Schedule a phone call for **Day 3**.  
  ▪ If not already done, arrange an in-person visit on **Day 4**.  
  ▪ Prepare to obtain labs (**CBC, BMP, BNP, Mg, TSH**) on Day 4.
""")
    elif day == "Day 3":
        st.subheader("NCCC - Day 3 (Phone Call)")
        st.markdown("""
1. Confirm stability (**weight loss, SOB, weakness, dizziness**).  
2. Reinforce **CRNP/YC diuretic instructions**.
""")
    elif day == "Day 4":
        st.subheader("NCCC - Day 4 (In-Person Visit Goals)")
        st.markdown("""
1. Assess response to treatment (**symptoms, weight, urine output**).  
2. Identify causes of recent decompensation.  
3. Obtain labs ordered by CRNP/YC on Day 2.  
4. Confirm updated diuretic treatment.  
5. Take a clinical image of lower extremities, upload to Epic via **Haiku**.  
6. Engage behavioral health/social work as needed.  
7. Align care with goals of care.  
8. Schedule **follow-up phone call** for Day 6.
""")
    else:
        st.subheader("NCCC - Day 6 (Follow-Up Phone Call)")
        st.markdown("""
1. Confirm return to baseline.  
2. Confirm current medications & update Epic EMR.  
3. Schedule a routine NCCC visit.  
4. Encourage follow-up with **PCP, Cardiology, Nephrology**.  
5. Close acute episode & report to Scheduling.
""")

# ================================
# Main Streamlit App
# ================================
def main():
    show_title_and_disclaimer()

    role = st.selectbox(
        "Select your role:",
        [
            "Triage Nurse",
            "Advanced Care Paramedic",
            "Scheduling Coordinator",
            "Community Health Worker",
            "CRNP",
            "Physician",
            "Nurse Clinical Care Coordinator"
        ]
    )

    day_options = {
        "Triage Nurse": ["Day 1", "Day 2"],
        "Advanced Care Paramedic": ["Day 1", "Day 2"],
        "Scheduling Coordinator": ["Day 1", "Day 6"],
        "Community Health Worker": ["Day 1", "Day 2"],
        "CRNP": ["Day 1", "Day 2", "Day 5"],
        "Physician": ["Day 1", "Day 2", "Day 5"],
        "Nurse Clinical Care Coordinator": ["Day 1", "Day 3", "Day 4", "Day 6"]
    }

    day = st.selectbox("Select the day:", day_options[role])

    st.markdown("---")

    # Display selected workflow
    if role == "Triage Nurse":
        triage_nurse_workflow(day)
    elif role == "Advanced Care Paramedic":
        advanced_care_paramedic_workflow(day)
    elif role == "Scheduling Coordinator":
        scheduling_coordinator_workflow(day)
    elif role == "Community Health Worker":
        chw_workflow(day)
    elif role in ["CRNP", "Physician"]:
        crnp_physician_workflow(day)
    elif role == "Nurse Clinical Care Coordinator":
        nccc_workflow(day)

if __name__ == "__main__":
    main()
