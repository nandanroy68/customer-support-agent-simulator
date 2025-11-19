"use client"
import { useEffect, useRef, useState } from 'react'
import API from '../lib/api'
import Loader from './Loader'
import MessageBubble from './MessageBubble'

type Msg = { role: 'user' | 'assistant'; content: string; confidence?: string; sources?: string[]; sentiment?: string }

export default function ChatWindow() {
  const [messages, setMessages] = useState<Msg[]>([])
  const [input, setInput] = useState("")
  const [loading, setLoading] = useState(false)
  const [sessionId, setSessionId] = useState("")
  const endRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    setSessionId(`session_${Date.now()}_${Math.random().toString(36).slice(2,8)}`)
  }, [])

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const send = async () => {
    if (!input.trim() || loading) return
    const text = input.trim()
    setInput("")
    setMessages(prev => [...prev, { role: 'user', content: text }])
    setLoading(true)
    try {
      const { data } = await API.post('/chat', { session_id: sessionId, message: text })
      setMessages(prev => [...prev, { role: 'assistant', content: data.response, confidence: data.confidence, sources: data.sources, sentiment: data.sentiment }])
    } catch (e) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, something went wrong.' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col h-[calc(100vh-4rem)]">
      <div className="flex-1 overflow-y-auto space-y-3 p-4 bg-gray-50">
        {messages.map((m, i) => (
          <MessageBubble key={i} role={m.role} content={m.content} confidence={m.confidence} sources={m.sources} sentiment={m.sentiment} />
        ))}
        {loading && <Loader />}
        <div ref={endRef} />
      </div>
      <div className="border-t bg-white p-3">
        <div className="flex gap-2">
          <input
            className="flex-1 border rounded-md px-3 py-2"
            placeholder="Type your message..."
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => { if (e.key === 'Enter') send() }}
          />
          <button onClick={send} className="px-4 py-2 rounded-md bg-blue-600 text-white disabled:opacity-50" disabled={!input.trim() || loading}>Send</button>
        </div>
      </div>
    </div>
  )
}


