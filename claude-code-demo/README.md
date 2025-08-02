# PDF Merger - Flask Web Application

A beautiful and modern web application for merging multiple PDF files into a single document. Built with Flask, PyPDF2, and Tailwind CSS.

## Features

- 🎨 **Beautiful Modern UI** - Clean, responsive design with gradient backgrounds and smooth animations
- 📁 **Drag & Drop Upload** - Easy file upload with drag-and-drop functionality
- 🔄 **Drag & Drop Reordering** - Arrange PDF files in any order using drag-and-drop
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Fast Processing** - Quick PDF merging with progress feedback
- 🔒 **Secure** - File validation and secure handling
- 🎯 **User-Friendly** - Intuitive interface with clear instructions

## Screenshots

The application features:
- Modern gradient navigation bar
- Beautiful file upload interface with drag-and-drop
- Interactive PDF arrangement page
- Responsive design that works on all devices

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

1. **Upload PDFs**: Click "Choose Files" or drag and drop PDF files onto the upload area
2. **Arrange Order**: On the merge page, drag and drop files to arrange them in your desired order
3. **Merge**: Click "Merge PDFs" to combine your files
4. **Download**: Your merged PDF will be automatically downloaded

## Project Structure

```
pdf-merger/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page with file upload
│   └── merge.html        # PDF arrangement and merge page
└── uploads/              # Temporary file storage (created automatically)
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **PDF Processing**: PyPDF2 (PDF manipulation library)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Tailwind CSS (utility-first CSS framework)
- **Icons**: Font Awesome
- **Drag & Drop**: SortableJS library

## Features in Detail

### File Upload
- Multiple file selection
- Drag and drop support
- File type validation (PDF only)
- File size display
- Progress feedback

### PDF Arrangement
- Drag and drop reordering
- Visual order indicators
- Move up/down buttons
- Real-time order updates

### PDF Merging
- Secure file processing
- Error handling
- Automatic download
- Session management

## Security Features

- File type validation (PDF only)
- Secure filename handling
- Session-based file management
- Automatic cleanup of temporary files
- Maximum file size limits

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Troubleshooting

### Common Issues

1. **"No module named 'flask'"**
   - Run: `pip install -r requirements.txt`

2. **Port already in use**
   - Change the port in `app.py` line: `app.run(debug=True, port=5001)`

3. **File upload not working**
   - Ensure you're selecting PDF files only
   - Check file size (max 16MB per file)

4. **PDF merge fails**
   - Ensure all files are valid PDFs
   - Try with smaller files first

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.

---

**Happy PDF Merging! 📄✨** 