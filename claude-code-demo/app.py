import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
from PyPDF2 import PdfMerger
import tempfile
import shutil

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        flash('No files selected', 'error')
        return redirect(request.url)
    
    files = request.files.getlist('files')
    
    if not files or files[0].filename == '':
        flash('No files selected', 'error')
        return redirect(url_for('index'))
    
    # Create a unique session folder
    session_id = str(uuid.uuid4())
    session_folder = os.path.join(UPLOAD_FOLDER, session_id)
    os.makedirs(session_folder, exist_ok=True)
    
    uploaded_files = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(session_folder, filename)
            file.save(filepath)
            uploaded_files.append(filepath)
        else:
            flash(f'Invalid file type: {file.filename}. Only PDF files are allowed.', 'error')
    
    if uploaded_files:
        flash(f'Successfully uploaded {len(uploaded_files)} PDF files', 'success')
        return redirect(url_for('merge', session_id=session_id))
    else:
        flash('No valid PDF files uploaded', 'error')
        return redirect(url_for('index'))

@app.route('/merge/<session_id>')
def merge(session_id):
    session_folder = os.path.join(UPLOAD_FOLDER, session_id)
    if not os.path.exists(session_folder):
        flash('Session not found', 'error')
        return redirect(url_for('index'))
    
    pdf_files = [f for f in os.listdir(session_folder) if f.endswith('.pdf')]
    return render_template('merge.html', session_id=session_id, files=pdf_files)

@app.route('/merge_pdfs/<session_id>', methods=['POST'])
def merge_pdfs(session_id):
    session_folder = os.path.join(UPLOAD_FOLDER, session_id)
    if not os.path.exists(session_folder):
        flash('Session not found', 'error')
        return redirect(url_for('index'))
    
    # Get the order of files from the form
    file_order = request.form.getlist('file_order')
    
    if not file_order:
        flash('No files selected for merging', 'error')
        return redirect(url_for('merge', session_id=session_id))
    
    try:
        merger = PdfMerger()
        
        for filename in file_order:
            filepath = os.path.join(session_folder, filename)
            if os.path.exists(filepath):
                merger.append(filepath)
        
        # Create merged PDF
        output_filename = f'merged_{session_id}.pdf'
        output_path = os.path.join(session_folder, output_filename)
        
        with open(output_path, 'wb') as output_file:
            merger.write(output_file)
        
        merger.close()
        
        flash('PDFs merged successfully!', 'success')
        return redirect(url_for('download', session_id=session_id, filename=output_filename))
        
    except Exception as e:
        flash(f'Error merging PDFs: {str(e)}', 'error')
        return redirect(url_for('merge', session_id=session_id))

@app.route('/download/<session_id>/<filename>')
def download(session_id, filename):
    session_folder = os.path.join(UPLOAD_FOLDER, session_id)
    file_path = os.path.join(session_folder, filename)
    
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=filename)
    else:
        flash('File not found', 'error')
        return redirect(url_for('index'))

@app.route('/cleanup/<session_id>')
def cleanup(session_id):
    session_folder = os.path.join(UPLOAD_FOLDER, session_id)
    if os.path.exists(session_folder):
        shutil.rmtree(session_folder)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Use 0.0.0.0 to make it accessible from outside
    app.run(debug=False, host='0.0.0.0', port=port) 