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
            

            base64_pdfs.append({
                "title": file.filename,
                "content": base64_string
            })


        data = {'base64_pdfs': base64_pdfs}


        return jsonify(data)
    

class extract_embedded_pdf(Resource):
    def post(self):

        json_data = request.files['embedded_json'].read()


        data = json.loads(json_data)


        zip_buffer = io.BytesIO()

  
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:

            for pdf_data in data['base64_pdfs']:

                decoded_content = base64.b64decode(pdf_data['content'])


                zip_file.writestr(pdf_data['title'], decoded_content)


        zip_buffer.seek(0)


        return Response(
            zip_buffer,
            mimetype='application/zip',
            headers={"Content-Disposition": "attachment;filename=files.zip"}
        )
    


