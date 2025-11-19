import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Customer Support Agent',
  description: 'GenAI RAG Support Chatbot',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}


