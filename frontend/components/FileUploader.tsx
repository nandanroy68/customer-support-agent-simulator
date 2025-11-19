"use client"
import { useState } from 'react'
import API from '../lib/api'

export default function FileUploader() {
  const [files, setFiles] = useState<FileList | null>(null)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<string>("")

  const upload = async () => {
    if (!files || files.length === 0 || loading) return
    const form = new FormData()
    Array.from(files).forEach(f => form.append('files', f))
    setLoading(true)
    setResult("")
    try {
      const { data } = await API.post('/ingest', form, { headers: { 'Content-Type': 'multipart/form-data' } })
      setResult(JSON.stringify(data))
    } catch (e: any) {
      setResult(e?.response?.data?.detail || 'Upload failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-3">
      <input type="file" multiple onChange={e => setFiles(e.target.files)} className="block" />
      <button onClick={upload} disabled={!files || loading} className="px-4 py-2 rounded-md bg-blue-600 text-white disabled:opacity-50">{loading ? 'Uploading...' : 'Upload'}</button>
      {result && (
        <pre className="text-xs bg-gray-50 border p-2 rounded-md overflow-x-auto">{result}</pre>
      )}
    </div>
  )
}


