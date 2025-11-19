import FileUploader from '../../components/FileUploader'

export default function IngestPage() {
  return (
    <main className="min-h-screen flex flex-col">
      <header className="border-b bg-white p-4">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <h1 className="text-lg font-semibold">Document Ingestion</h1>
          <a href="/" className="text-sm text-blue-600">Back to Chat</a>
        </div>
      </header>
      <div className="max-w-6xl mx-auto w-full p-4">
        <p className="text-sm text-gray-600 mb-4">Upload PDF, TXT, or DOCX files to update the RAG index.</p>
        <FileUploader />
      </div>
    </main>
  )
}


