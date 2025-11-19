import ChatWindow from '../components/ChatWindow'

export default function Page() {
  return (
    <main className="min-h-screen flex flex-col">
      <header className="border-b bg-white p-4">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <h1 className="text-lg font-semibold">Customer Support Agent</h1>
          <a href="/ingest" className="text-sm text-blue-600">Ingest Documents</a>
        </div>
      </header>
      <div className="max-w-6xl mx-auto w-full flex-1">
        <ChatWindow />
      </div>
    </main>
  )
}


