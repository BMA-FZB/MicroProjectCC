#routes.py
from flask_restful import Resource
from flask import request, jsonify, Response
from flask import render_template
import zipfile
import io

from PyPDF2 import PdfMerger, PdfReader, PdfWriter


        
class create_embedded_pdf(Resource):
    def post(self):
        base_pdf_file = request.files['pdf_Base_file']
        pdf_files = request.files.getlist('pdf_files')

        merger = PdfMerger()
        merger.append(base_pdf_file)

        for pdf_file in pdf_files:
            merger.append(pdf_file)

        output = io.BytesIO()
        merger.write(output)
        merger.close()
        output.seek(0)

        response = Response(output, content_type='application/pdf')
        response.headers['Content-Disposition'] = 'attachment; filename=embedded_file.pdf'
        return response


class extract_embedded_pdf(Resource):
    def post(self):
        embedded_file = request.files['embedded_file']

        reader = PdfReader(embedded_file)
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                pdf_output = io.BytesIO()
                writer.write(pdf_output)
                pdf_output.seek(0)
                zip_file.writestr(f"page_{i+1}.pdf", pdf_output.read())

        zip_buffer.seek(0)
        return Response(
            zip_buffer,
            mimetype='application/zip',
            headers={"Content-Disposition": "attachment; filename=files.zip"}
        )



