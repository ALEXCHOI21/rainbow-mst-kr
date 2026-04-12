import markdown
from xhtml2pdf import pisa
import os

def convert_md_to_pdf(md_file_path, pdf_file_path):
    # 1. Read Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 2. Convert Markdown to HTML (with table extension)
    html_content = markdown.markdown(md_text, extensions=['tables', 'nl2br'])

    # 3. Create full HTML with CSS styling for a professional report
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}
        body {{
            font-family: "Malgun Gothic", "Apple SD Gothic Neo", sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{
            font-size: 24pt;
            color: #1a3a5f;
            border-bottom: 2px solid #1a3a5f;
            padding-bottom: 10px;
            margin-bottom: 20px;
            text-align: center;
        }}
        h2 {{
            font-size: 18pt;
            color: #2c5282;
            border-left: 5px solid #2c5282;
            padding-left: 10px;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        h3 {{
            font-size: 14pt;
            color: #2b6cb0;
            margin-top: 20px;
        }}
        p {{ margin-bottom: 10px; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            border: 1px solid #ddd;
        }}
        th {{
            background-color: #f7fafc;
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }}
        td {{
            border: 1px solid #ddd;
            padding: 10px;
        }}
        blockquote {{
            background: #f0f4f8;
            border-left: 5px solid #3182ce;
            padding: 15px;
            margin: 20px 0;
            font-style: italic;
        }}
        .footer {{
            text-align: right;
            font-size: 9pt;
            color: #718096;
            margin-top: 50px;
        }}
        hr {{
            border: 0;
            border-top: 1px solid #cbd5e0;
            margin: 20px 0;
        }}
    </style>
    </head>
    <body>
        <div class="header">
            <p style="text-align: right; color: #718096;">Rainbow MST Korea - Strategic Report</p>
        </div>
        {html_content}
        <div class="footer">
            <p>© 2026 ChoiGPT Corp. All Rights Reserved.</p>
        </div>
    </body>
    </html>
    """

    # 4. Generate PDF
    with open(pdf_file_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(styled_html, dest=pdf_file, encoding='utf-8')

    return not pisa_status.err

if __name__ == "__main__":
    md_path = r"C:\Users\say0n\.gemini\antigravity\brain\c34dd56a-c259-466c-9cd0-70c5f2954729\Email_Platform_Strategic_Report.md"
    pdf_path = r"C:\Users\say0n\.gemini\antigravity\brain\c34dd56a-c259-466c-9cd0-70c5f2954729\Email_Platform_Strategic_Report.pdf"
    
    print(f"변환 시작: {md_path}")
    if convert_md_to_pdf(md_path, pdf_path):
        print(f"성공: {pdf_path}")
    else:
        print("에러 발생: PDF 변환 실패")
