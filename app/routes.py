#routes.py
from flask_restful import Resource
from flask import request, jsonify, Response
from flask import render_template
import base64
import zipfile
import io
import json



class create_embedded_pdf(Resource):
    def post(self):
        files = request.files.getlist('files')

        base64_pdfs = []

        for file in files:
            pdf_content = file.read()
            base64_content = base64.b64encode(pdf_content)
            base64_string = base64_content.decode('utf-8')
            
            # Construct dictionary with title and content
            base64_pdfs.append({
                "title": file.filename,
                "content": base64_string
            })

        # Construct response data
        data = {'base64_pdfs': base64_pdfs}

        # Return the data as JSON response
        return jsonify(data)
    

class extract_embedded_pdf(Resource):
    def post(self):
        # Read the embedded.json file
        json_data = request.files['embedded_json'].read()

        # Parse JSON data
        data = json.loads(json_data)

        # Initialize a BytesIO object to hold the ZIP file in memory
        zip_buffer = io.BytesIO()

        # Create a ZIP file and add the PDF files to it
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Loop through each PDF data in the JSON
            for pdf_data in data['base64_pdfs']:
                # Decode base64 content
                decoded_content = base64.b64decode(pdf_data['content'])

                # Write PDF file to the ZIP file
                zip_file.writestr(pdf_data['title'], decoded_content)

        # Set the buffer's position to the beginning
        zip_buffer.seek(0)

        # Return the ZIP file as a response
        return Response(
            zip_buffer,
            mimetype='application/zip',
            headers={"Content-Disposition": "attachment;filename=files.zip"}
        )
    


