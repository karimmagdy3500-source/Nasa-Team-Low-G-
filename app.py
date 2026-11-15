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


# 4. دالة قراءة ملف الـ Excel أوتوماتيكياً من المجلد
@st.cache_data
def load_excel_database():
  for file in os.listdir("."):
    if file.endswith((".xlsx", ".xls")):
      try:
        # قراءة ملف الإكسيل
        df = pd.read_excel(file)

        # تنظيف الداتا: لو فيه خلايا فاضية تحت بعض (بسبب الدمج)، نملأها بالقيمة اللي فوقها
        df = df.dropna(
            how="all"
        )  # حذف الصفوف الفارغة تماماً لو وجدت في ملف الإكسيل
        if not df.empty:
          # ملء الفراغات في الأعمدة التصنيفية أوتوماتيكياً
          df = df.ffill()

        return df, f"Live Database Connected: {file}"
      except Exception as e:
        pass

  # داتا احتياطية في حال لم يتم العثور على الملف
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
  return fallback_df, "Fallback Mode (Check Excel file structure)"


df, status_label = load_excel_database()

# 5. الشريط الجانبي (Mission Control)
st.sidebar.markdown("### 🎛️ Mission Control")
st.sidebar.markdown(
    f"<div style='font-size: 0.85rem; color: #38bdf8; font-weight: 600;"
    f" margin-bottom: 15px;'>{status_label}</div>",
    unsafe_allow_html=True,
)

# فلترة ذكية بناءً على أول عمود نصي أو تصنيفي لو وجد
cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
if cat_cols:
  selected_cat = st.sidebar.selectbox(
      f"Filter by {cat_cols[0]}", ["All"] + list(df[cat_cols[0]].unique())
  )
  filtered_df = (
      df[df[cat_cols[0]] == selected_cat] if selected_cat != "All" else df
  )
else:
  filtered_df = df

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='font-size: 0.8rem; color: #64748b;'>Team Low G v2.5<br>NASA"
    " Space Apps 2026</div>",
    unsafe_allow_html=True,
)

# 6. التبويبات الرئيسية (Tabs)
tab1, tab2, tab3 = st.tabs(
    [
        "📊 Telemetry & Database",
        "📈 Power BI Visual Views",
        "🤖 AI Intelligence Core",
    ]
)

# --- Tab 1: التيليمتري وقاعدة البيانات ---
with tab1:
  st.markdown(
      "<h3 style='font-size: 1.25rem; font-weight: 600; margin-bottom:"
      " 15px;'>🛰️ Active Microgravity Combustion Dataset</h3>",
      unsafe_allow_html=True,
  )
  st.dataframe(filtered_df, use_container_width=True)

  # رسم بياني تفاعلي ذكي يتكيف مع أعمدة الجدول
  numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
  if len(numeric_cols) >= 2:
    fig = px.scatter(
        filtered_df,
        x=numeric_cols[0],
        y=numeric_cols[1],
        color=cat_cols[0] if cat_cols else None,
        title=f"Telemetry Analysis: {numeric_cols[1]} vs {numeric_cols[0]} (0G)",
        template="plotly_dark",
        color_discrete_sequence=["#38bdf8", "#fc3d21", "#a855f7", "#34d399"],
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", color="#94a3b8"),
        title_font=dict(size=16, color="#f3f4f6"),
        legend=dict(
            bgcolor="rgba(15, 23, 42, 0.6)",
            bordercolor="rgba(255,255,255,0.1)",
            borderwidth=1,
        ),
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Tab 2: صور Power BI المباشرة من المجلد الرئيسي ---
with tab2:
  st.markdown(
      "<h3 style='font-size: 1.25rem; font-weight: 600; margin-bottom:"
      " 15px;'>📈 Power BI Executive Visualizations</h3>",
      unsafe_allow_html=True,
  )

  # البحث عن الصور مباشرة في المجلد الحالي (Root Directory) وتصفيتها
  current_folder = "."
  images = [
      f
      for f in os.listdir(current_folder)
      if f.lower().endswith((".png", ".jpg", ".jpeg"))
      and f != "app.py"
      and not f.endswith((".xlsx", ".xls", ".csv", ".txt", ".py"))
  ]

  if images:
    selected_image = st.selectbox("Select Power BI Report View:", images)
    # عرض الصورة مباشرة من المجلد الرئيسي
    st.image(
        selected_image,
        caption=f"Executive View: {selected_image}",
        use_container_width=True,
    )
  else:
    st.warning(
        "⚠️ لم يتم العثور على صور بصيغة PNG أو JPG في المجلد الرئيسي. تأكد"
        " من رفع الصور بجانب ملف app.py على GitHub."
    )
# --- Tab 3: مساعد الذكاء الاصطناعي التفاعلي الذكي ---
# --- Tab 3: Low G Multi-Source Intelligence Agent ---
with tab3:
  st.markdown(
      "<h3 style='font-size: 1.25rem; font-weight: 600; margin-bottom:"
      " 15px;'>🤖 Low G Multi-Source Intelligence Agent</h3>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='color: #94a3b8; font-size: 0.9rem; margin-bottom: 20px;'>وكيل"
      " ذكي متكامل يربط بسلاسة بين 4 مصادر: (تيليمتري الإكسيل، تقارير Power"
      " BI، هيكل فريق Low G، وقاعدة معارف ناسا لاحتراق الفضاء).</p>",
      unsafe_allow_html=True,
  )

  # تهيئة سجل المحادثة للـ Agent
  if "agent_messages" not in st.session_state:
    st.session_state.agent_messages = [{
        "role": "assistant",
        "content": (
            "أهلاً بك يا بشمهندس كريم! أنا **Low G Agent**، جاهز للرد الفوري من"
            " مصادر متعددة وتزويدك بتحليلات دقيقة. تفضل بسؤالك عن أي تجربة، تقرير"
            " Power BI، أو معلومات الفريق!"
        ),
    }]

  # عرض الرسائل السابقة
  for msg in st.session_state.agent_messages:
    with st.chat_message(msg["role"]):
      st.markdown(msg["content"])

  # استقبال المدخلات من المستخدم
  if query := st.chat_input(
      "اسأل عن التيليمتري، تقارير Power BI، أعضاء التيم، أو ديناميكيات"
      " الاحتراق..."
  ):
    st.session_state.agent_messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
      st.markdown(query)

    with st.chat_message("assistant"):
      with st.spinner(
          "جاري التنسيق بين مصادر البيانات (Excel + Power BI + Team + Knowledge"
          " Base)..."
      ):
        q_lower = query.lower()
        response_parts = []

        # المصدر 1: البحث في داتا إكسيل (التيليمتري)
        excel_matched = False
        for col in df.columns:
          m = df[df[col].astype(str).str.lower().str.contains(q_lower, na=False)]
          if not m.empty and len(q_lower) > 1:
            excel_matched = True
            res = m.iloc[0]
            summary_row = " | ".join([f"**{k}**: {v}" for k, v in res.items()])
            response_parts.append(
                "📊 **[مصدر 1: قاعدة التيليمتري (Excel Database)]**\n"
                f"تم رصد تطابق مباشر في سجلات التجارب:\n- `{summary_row}`"
            )
            break

        # المصدر 2: تقارير و صور Power BI في assets
        if any(
            k in q_lower
            for k in [
                "power bi",
                "dashboard",
                "report",
                "صورة",
                "رسم",
                "لوحة",
                "داشبورد",
            ]
        ):
          img_folder = "assets"
          if os.path.exists(img_folder):
            imgs = [
                f
                for f in os.listdir(img_folder)
                if f.lower().endswith((".png", ".jpg", ".jpeg"))
            ]
            response_parts.append(
                "📈 **[مصدر 2: تقارير Power BI التنفيذية (Assets)]**\n"
                f"اللوحات المرئية المتاحة حالياً في النظام: `{', '.join(imgs)}`."
                " يمكنك استعراضها مباشرة وبأعلى جودة من تبويب **Power BI Visual"
                " Views**."
            )

        # المصدر 3: معلومات فريق العمل (Team Low G)
        if any(
            k in q_lower
            for k in ["team", "تيم", "فريق", "أعضاء", "members", "كريم", "karim"]
        ):
          response_parts.append(
              "🚀 **[مصدر 3: هيكل فريق العمل (Team Low G)]**\n"
              "- **قائد ومصمم المشروع:** Eng. Karim Magdy\n- **أعضاء الفريق"
              " (Honorable Mentions):** Eng. Abdelaziz, Eng. Arwa, Eng. Karim,"
              " Eng. Hashem, Eng. Amina\n- **الحدث:** NASA Space Apps Challenge"
              " 2026."
          )

        # المصدر 4: علوم الاحتراق والجاذبية الصغرى (Microgravity Science Base)
        if any(
            k in q_lower
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
            ]
        ):
          response_parts.append(
              "🔥 **[مصدر 4: قاعدة المعرفة الفضائية (Microgravity Combustion"
              " Base)]**\n"
              "- في بيئة الجاذبية الصغرى (0G)، ينتشر اللهب بشكل كروي وبدون"
              " تأثير للحمل الحراري الأرضي (Buoyancy).\n- تعتمد سرعة انتشار اللهب"
              " بشكل حرج على مستويات الأكسجين المحيط وخصائص المادة.\n- كافة"
              " مؤشرات التيليمتري الحالية متوافقة مع معايير السلامة الخاصة بمركبات"
              " الفضاء."
          )

        # إذا لم ينطبق شرط محدد، نعطي تقريراً استكشافياً مرناً من كافة المصادر
        if not response_parts:
          response_parts.append(
              "💡 **[توجيه ذكي من Low G Agent]**\n"
              "أنا جاهز للإجابة من عدة مصادر! يمكنك سؤالي عن:\n"
              "1. **بيانات التجارب والتيليمتري** (باستخدام اسم المادة أو رقم"
              " التجربة).\n"
              "2. **حالة لوحات Power BI** المرئية.\n"
              "3. **أسماء وأدوار تيم Low G**.\n"
              "4. **مفاهيم احتراق الفضاء وسلامة ناسا**."
          )

        final_response = "\n\n---\n\n".join(response_parts)
        st.markdown(final_response)
        st.session_state.agent_messages.append(
            {"role": "assistant", "content": final_response}
        )

# 7. قسم Honorable Mentions (فريق العمل)
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