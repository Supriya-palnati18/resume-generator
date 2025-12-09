from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        # Header manually placed in body
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def section_title(self, title):
        self.ln(6)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(0, 51, 102)  # Navy Blue
        self.cell(0, 6, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_draw_color(0, 51, 102)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

    def job_header(self, role, company, location, date):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 5, role, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        self.set_font('Helvetica', 'B', 10)
        self.cell(60, 5, company, new_x=XPos.RIGHT, new_y=YPos.TOP)
        
        self.set_font('Helvetica', 'I', 10)
        self.set_xy(10, self.get_y()) 
        self.cell(0, 5, date, align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def bullet_point(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(20, 20, 20)
        self.set_x(12) 
        self.cell(5, 5, chr(149), new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_x(17)
        self.multi_cell(180, 5, text)
        self.ln(1)

# --- SETUP ---
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_margins(10, 10, 10)

# --- HEADER ---
pdf.set_font('Helvetica', 'B', 20)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 10, 'LEELA SUPRIYA PALNATI', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(0, 0, 0)
contact_line = "Sricity, Tirupati  |  +91 7780498081  |  palnatileelasupriya@gmail.com"
pdf.cell(0, 5, contact_line, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

linkedin_url = "https://www.linkedin.com/in/leela-supriya-palnati-133926245/"
pdf.set_font('Helvetica', 'U', 10)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 5, "linkedin.com/in/leela-supriya-palnati", align='C', link=linkedin_url, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(3)

# --- SUMMARY (Your Preferred "Strong" Version) ---
pdf.section_title("Professional Profile")
summary = (
    "Performance-driven Full Stack Engineer with expertise in architecting high-availability real-time systems and "
    "secure digital ecosystems. Proven track record of optimizing API latency by 30% and engineering scalable dashboards "
    "processing sub-second data streams. Adept at translating complex business logic into production-grade MERN and "
    "Django solutions. Specializes in database optimization, secure authentication protocols, and building responsive, "
    "ADA-compliant user interfaces."
)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(0, 0, 0)
pdf.multi_cell(0, 5, summary)

# --- SKILLS (Safe: Git/Agile, no Deployment ops) ---
pdf.section_title("Technical Expertise")
def add_skill(category, skills):
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(40, 5, category, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font('Helvetica', '', 10)
    pdf.cell(0, 5, f":  {skills}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

add_skill("Core Stack", "Python, JavaScript (ES6+), React.js, Node.js, Django")
add_skill("Backend & Data", "Django REST Framework (DRF), PostgreSQL, MySQL, SQLite")
add_skill("Tools & Workflow", "Git, GitHub, Postman, VS Code, Agile/Scrum")
add_skill("Frontend UI", "Tailwind CSS, Material UI, Chart.js, Figma-to-Code")

# --- EXPERIENCE ---
pdf.section_title("Professional Experience")

# --- JOB 1: FULL TIME ---
pdf.job_header("Full Stack Developer (SDE)", "Station-S", "Tirupati, India", "Apr 2025 - Present")

# Architecture/Scale
pdf.bullet_point(
    "Promoted to Full-Time SDE to lead the architecture of 'FACT.Signs'; engineered secure "
    "PDF rendering logic and backend workflows, reducing document turnaround time by 60%."
)
# Real-Time/Sockets
pdf.bullet_point(
    "Developed the 'WEEWA' real-time dashboard using React and Django Channels, optimizing WebSocket data "
    "handling to visualize inputs from 10+ industrial sensors with sub-second latency."
)
# Optimization (Numbers)
pdf.bullet_point(
    "Refactored complex database queries and API views, successfully slashing server response times by 30% "
    "(500ms to 350ms) and improving application responsiveness for end-users."
)
# Security/Compliance
pdf.bullet_point(
    "Implemented rigorous Role-Based Access Control (RBAC) and drag-and-drop features, ensuring code compliance "
    "with data security protocols before handing off for deployment."
)

pdf.ln(2)

# --- JOB 2: INTERNSHIP ---
pdf.job_header("Full Stack Developer Intern", "Station-S", "Tirupati, India", "Nov 2024 - Mar 2025")

# The Conversion Hook
pdf.bullet_point(
    "Transformed 15+ complex Figma wireframes into pixel-perfect, responsive React components; high code quality "
    "and delivery speed were key factors in securing a full-time employment offer."
)
# Backend Integration
pdf.bullet_point(
    "Integrated Django REST APIs with frontend architectures, facilitating dynamic state management and improving "
    "data retrieval efficiency for internal tools."
)
# Bug Fixes / Stability
pdf.bullet_point(
    "Collaborated closely with QA teams to resolve 20+ critical bugs, ensuring application stability and "
    "smooth release cycles."
)
# Version Control (Safe DevOps)
pdf.bullet_point(
    "Maintained strict version control standards using Git and GitHub, ensuring clean code merges and facilitating "
    "seamless updates for the deployment team."
)

# --- EDUCATION ---
pdf.section_title("Education")

pdf.set_font('Helvetica', 'B', 11)
pdf.cell(140, 5, "B.Tech, Electrical and Electronics Engineering", new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.set_font('Helvetica', 'I', 11)
# Assuming 2024 Grad
pdf.cell(0, 5, "Graduated: 2024", align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font('Helvetica', '', 10)
pdf.cell(0, 5, "NRI Institute of Technology", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# --- SAVE ---
output_filename = "Leela_Supriya_Palnati_Resume.pdf"
pdf.output(output_filename)

print(f"Success! High-Impact Resume generated: {output_filename}")
