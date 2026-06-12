from app.pdf.utils import extract_text
from app.ai.detector import check_plagiarism


# inside your endpoint
text_content = extract_text(input_path)

result = check_plagiarism(text_content)

highlighted_path = highlight_pdf(
    input_pdf_path=input_path,
    matches=result["matches"],
    output_pdf_path=output_path
)