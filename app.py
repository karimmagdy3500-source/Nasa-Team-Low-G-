import os
import pandas as pd
import plotly.express as px
import streamlit as st

# 1. إعدادات الصفحة العالمية
st.set_page_config(
    page_title="Team Low G — NASA Space Apps",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. تصميم CSS عالمي (Vercel & Linear Style)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {
        background-color: #030712;
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .global-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(3, 7, 18, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 35px 40px;
        margin-bottom: 30px;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
        position: relative;
        overflow: hidden;
    }
    .global-hero::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, #38bdf8, #fc3d21, #a855f7);
    }

    .pill-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(252, 61, 33, 0.12);
        border: 1px solid rgba(252, 61, 33, 0.3);
        color: #ff6b4a;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    .pulse-dot {
        width: 6px; height: 6px;
        background-color: #fc3d21;
        border-radius: 50%;
        box-shadow: 0 0 8px #fc3d21;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.8; }
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(15, 23, 42, 0.6);
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px;
        color: #94a3b8;
        font-weight: 500;
        padding: 8px 18px;
        border: none;
        transition: all 0.2s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }

    .mentions-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 12px;
        margin-top: 20px;
        padding: 24px;
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        backdrop-filter: blur(10px);
    }
    .team-member-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 10px;
        padding: 12px 16px;
        text-align: center;
        font-weight: 600;
        font-size: 0.9rem;
        color: #e2e8f0;
        transition: all 0.25s ease;
    }
    .team-member-card:hover {
        border-color: rgba(56, 189, 248, 0.4);
        transform: translateY(-2px);
        background: rgba(30, 41, 59, 0.7);
        box-shadow: 0 8px 20px rgba(56, 189, 248, 0.1);
    }

    [data-testid="stSidebar"] {
        background-color: #050b14;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. الهيدر الفاخر بتوقيع المهندس كريم مجدي
st.markdown(
    """
    <div class="global-hero">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 20px;">
            <div>
                <div class="pill-badge">
                    <div class="pulse-dot"></div>
                    Team Low G — NASA Space Apps Challenge
                </div>
                <h1 style="margin: 0 0 10px 0; font-size: 2.5rem; font-weight: 800; letter-spacing: -0.03em; color: #ffffff;">
                    Flame in <span style="background: linear-gradient(90deg, #38bdf8, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Freefall</span>
                </h1>
                <p style="margin: 0; color: #94a3b8; font-size: 1.05rem; font-weight: 400; max-width: 600px;">
                    Advanced microgravity combustion telemetry, predictive fire-safety dynamics, and automated spacecraft mitigation intelligence.
                </p>
                <div style="margin-top: 15px; font-size: 0.9rem; color: #64748b;">
                    Designed & Architected by <span style="color: #38bdf8; font-weight: 600;">Eng. Karim Magdy</span>
                </div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); padding: 16px 24px; border-radius: 12px; backdrop-filter: blur(8px);">
                <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600;">System Status</div>
                <div style="font-size: 1rem; font-weight: 700; color: #34d399; display: flex; align-items: center; gap: 8px; margin-top: 4px;">
                    <span style="width: 8px; height: 8px; background: #34d399; border-radius: 50%; display: inline-block;"></span>
                    Telemetry Online (0G)
                </div>
            </div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)


# 4. دالة قراءة الإكسيل الذكية
@st.cache_data
def load_excel_database():
  for file in os.listdir("."):
    if file.endswith((".xlsx", ".xls")):
      try:
        df = pd.read_excel(file)
        df = df.dropna(how="all")
        if not df.empty:
          df = df.ffill()
        return df, f"Live Database: {file}"
      except:
        pass

  fallback_df = pd.DataFrame({
      "Experiment_Name": [
          "FLEX-1 (Heptane Droplet)",
          "FLEX-2 (Methane Flame)",
          "Saffire-I (Nomex Fabric)",
      ],
      "Fuel_Type": ["Heptane", "Methane", "Solid Composite"],
      "Oxygen_Percentage": [21.0, 30.0, 18.5],
      "Flame_Spread_Speed_mm_s": [1.4, 3.8, 0.9],
      "Safety_Risk_Level": ["Medium", "High", "Critical"],
  })
  return fallback_df, "Fallback Mode (Excel template active)"


df, status_label = load_excel_database()

# 5. الشريط الجانبي مع أدوات المحاكاة التفاعلية (Interactive Simulation Controls)
st.sidebar.markdown("### 🎛️ Mission Control")
st.sidebar.markdown(
    f"<div style='font-size: 0.8rem; color: #38bdf8; margin-bottom:"
    f" 10px;'>{status_label}</div>",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
st.sidebar.markdown("#### 🔬 Live 0G Combustion Simulator")
sim_oxygen = st.sidebar.slider(
    "Chamber Oxygen Level (%)", min_value=10.0, max_value=40.0, value=21.0
)
sim_pressure = st.sidebar.slider(
    "Cabin Pressure (kPa)", min_value=50.0, max_value=120.0, value=101.3
)

# حساب ديناميكي تقريبي للمخاطر بناءً على السلايدرات للحكام
predicted_risk = (
    "Critical 🔥"
    if sim_oxygen > 28
    else ("High ⚠️" if sim_oxygen > 22 else "Stable ✅")
)
st.sidebar.markdown(
    f"<div style='background: rgba(30, 41, 59, 0.6); padding: 10px;"
    f" border-radius: 8px; border: 1px solid rgba(255,255,255,0.1);'>"
    f"<b>Simulated Risk Status:</b> <span style='color: {'#ef4444' if 'Critical' in predicted_risk else ('#f59e0b' if 'High' in predicted_risk else '#34d399')}'>{predicted_risk}</span></div>",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
# زر الطوارئ والإخماد الآلي في الشريط الجانبي
emergency_btn = st.sidebar.button("🚨 EMERGENCY SUPPRESSION TRIGGER")

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='font-size: 0.75rem; color: #64748b;'>Team Low G v3.0<br>NASA"
    " Space Apps 2026</div>",
    unsafe_allow_html=True,
)

# تفاعل زر الطوارئ
if emergency_btn:
  st.error(
      "🚨 **EMERGENCY PROTOCOL ACTIVATED!** Automatic CO2 suppression valves"
      " opened in combustion chamber. Microgravity ignition source isolated."
  )

# 6. التبويبات الرئيسية
tab1, tab2, tab3 = st.tabs(
    [
        "📊 Telemetry & Database",
        "📈 Power BI Visual Views",
        "🤖 AI Intelligence Core",
    ]
)

# --- Tab 1 ---
with tab1:
  st.markdown(
      "<h3 style='font-size: 1.25rem; font-weight: 600; margin-bottom:"
      " 15px;'>🛰️ Active Microgravity Combustion Dataset</h3>",
      unsafe_allow_html=True,
  )
  st.dataframe(df, use_container_width=True)

  numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
  if len(numeric_cols) >= 2:
    fig = px.scatter(
        df,
        x=numeric_cols[0],
        y=numeric_cols[1],
        title="Microgravity Flame Dynamics & Telemetry Analysis",
        template="plotly_dark",
        color_discrete_sequence=["#38bdf8", "#fc3d21", "#a855f7", "#34d399"],
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color="#94a3b8"),
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Tab 2 ---
with tab2:
  st.markdown(
      "<h3 style='font-size: 1.25rem; font-weight: 600; margin-bottom:"
      " 15px;'>📈 Power BI Executive Visualizations</h3>",
      unsafe_allow_html=True,
  )

  images = [
      f
      for f in os.listdir(".")
      if f.lower().endswith((".png", ".jpg", ".jpeg"))
      and f != "app.py"
      and not f.endswith((".xlsx", ".xls", ".csv", ".txt", ".py"))
  ]
  if images:
    selected_image = st.selectbox("Select Power BI Report View:", images)
    st.image(
        selected_image,
        caption=f"Executive View: {selected_image}",
        use_container_width=True,
    )
  else:
    st.warning("⚠️ لم يتم العثور على صور مرفوعة في المجلد الرئيسي.")

# --- Tab 3: Low G Autonomous Intelligence Agent (Local & Fast) ---
with tab3:
  st.markdown(
      "<h3 style='font-size: 1.25rem; font-weight: 600; margin-bottom:"
      " 15px;'>🤖 Low G Autonomous Intelligence Agent</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color: #94a3b8; font-size: 0.9rem; margin-bottom: 20px;'>مساعد"
      " ذكي محلي بالكامل (Local Autonomous Agent) متصل مباشرة بقاعدة البيانات،"
      " تقارير Power BI، ومعارف ناسا بدون أي حاجة لمفاتيح خارجية.</p>",
      unsafe_allow_html=True,
  )

  # تهيئة سجل الشات المحلي
  if "local_agent_msgs" not in st.session_state:
    st.session_state.local_agent_msgs = [{
        "role": "assistant",
        "content": (
            "أهلاً بك يا بشمهندس كريم! أنا **Low G Autonomous Agent** المحلي."
            " جاهز للرد الفوري وتحليل التيليمتري، الرد عن أعضاء التيم، أو شرح"
            " فيزياء الاحتراق في الجاذبية الصغرى بسلاسة وبدون أي مفاتيح API!"
        ),
    }]

  # عرض الرسائل السابقة
  for msg in st.session_state.local_agent_msgs:
    with st.chat_message(msg["role"]):
      st.markdown(msg["content"])

  # استقبال المدخلات من المستخدم
  if user_prompt := st.chat_input(
      "اسأل عن التيليمتري، التجارب، التيم، أو سلوك الحريق في الفضاء..."
  ):
    st.session_state.local_agent_msgs.append(
        {"role": "user", "content": user_prompt}
    )
    with st.chat_message("user"):
      st.markdown(user_prompt)

    with st.chat_message("assistant"):
      with st.spinner("جاري تحليل الطلب والبحث في قواعد البيانات المحلية..."):
        query_lower = user_prompt.lower()
        response_chunks = []

        # 1. البحث التلقائي في بيانات الإكسيل (التيليمتري)
        data_found = False
        for col in df.columns:
          matches = df[
              df[col].astype(str).str.lower().str.contains(query_lower, na=False)
          ]
          if not matches.empty and len(query_lower) > 1:
            data_found = True
            response_chunks.append(
                f"📊 **[نتائج التيليمتري وقاعدة البيانات (Excel)]**\nتم العثور"
                f" على تطابقات مباشرة لسؤالك:"
            )
            for _, row in matches.head(3).iterrows():
              row_str = " | ".join([f"**{k}**: {v}" for k, v in row.items()])
              response_chunks.append(- `{row_str}`)
            break

        # 2. الاستعلام عن فريق العمل (Team Low G)
        if any(
            k in query_lower
            for k in [
                "team",
                "فريق",
                "تيم",
                "كريم",
                "karim",
                "أعضاء",
                "members",
                "abdelaziz",
                "arwa",
            ]
        ):
          response_chunks.append(
              "🚀 **[هيكل فريق العمل - Team Low G]**\n- **قائد ومصمم الداشبورد:"
              "** Eng. Karim Magdy\n- **أعضاء الفريق (Honorable"
              " Mentions):** Eng. Abdelaziz, Eng. Arwa, Eng. Karim, Eng."
              " Hashem, Eng. Amina\n- **الحدث:** NASA Space Apps Challenge"
              " 2026."
          )

        # 3. الاستعلام عن تقارير Power BI
        if any(
            k in query_lower
            for k in [
                "power bi",
                "dashboard",
                "report",
                "صور",
                "داشبورد",
                "تقارير",
            ]
        ):
          response_chunks.append(
              "📈 **[تقارير Power BI التنفيذية]**\nالمنصة مرتبطة بلوحات"
              " تحليلية متقدمة تعرض مقارنات انتشار اللهب وتغيرات الأكسجين."
              " يمكنك استعراضها مباشرة من تبويب **Power BI Visual Views**."
          )

        # 4. علوم الفضاء والاحتراق (Microgravity Science & NASA Challenge)
        if any(
            k in query_lower
            for k in [
                "combustion",
                "fire",
                "safety",
                "oxygen",
                "gravity",
                "احتراق",
                "حريق",
                "أكسجين",
                "جاذبية",
                "ناسا",
                "freefall",
                "flame",
            ]
        ):
          response_chunks.append(
              "🔥 **[قاعدة معارف ناسا لاحتراق الفضاء (Flame in"
              " Freefall)]**\n- في بيئة الجاذبية الصغرى (0G)، تفتقر"
              " الحرائق إلى ظاهرة الحمل الحراري الأرضي (Buoyancy)، مما يجعل"
              " اللهب يتخذ شكلاً كروياً ونقياً.\n- تعتمد سرعة انتشار اللهب"
              " بشكل أساسي على تركيز الأكسجين والضغط المحيط في الكبسولة.\n-"
              " توفر منصتنا مراقبة تنبؤية فورية لضمان سلامة الرواد والكبسولة."
          )

        # إذا لم يتم العثور على كلمة مفتاحية محددة
        if not response_chunks:
          response_chunks.append(
              "💡 **[Low G Autonomous Agent]**\nلقد قمت بتحليل طلبك بنجاح."
              " يمكنك سؤالي عن:\n1. تفاصيل أي تجربة أو رقم تيليمتري في ملف"
              " الإكسيل.\n2. أعضاء فريق Low G ومصمم النظام (Eng. Karim"
              " Magdy).\n3. تقارير ومؤشرات Power BI.\n4. فيزياء الاحتراق"
              " في الجاذبية الصغرى ومعايير ناسا."
          )

        final_bot_reply = "\n\n---\n\n".join(response_chunks)
        st.markdown(final_bot_reply)
        st.session_state.local_agent_msgs.append(
            {"role": "assistant", "content": final_bot_reply}
        )

# 7. Honorable Mentions
st.markdown(
    """
    <div style="margin-top: 50px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 15px;">
            <div>
                <span style="color: #38bdf8; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;">Contributors</span>
                <h3 style="margin: 2px 0 0 0; font-size: 1.2rem; color: #ffffff;">Honorable Mentions — Team Low G</h3>
            </div>
            <div style="color: #64748b; font-size: 0.85rem;">NASA Space Apps Challenge 2026</div>
        </div>
        <div class="mentions-grid">
            <div class="team-member-card">👨‍🚀 Eng. Abdelaziz</div>
            <div class="team-member-card">👩‍🚀 Eng. Arwa</div>
            <div class="team-member-card">👨‍🚀 Eng. Karim</div>
            <div class="team-member-card">👨‍🚀 Eng. Hashem</div>
            <div class="team-member-card">👩‍🚀 Eng. Amina</div>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)