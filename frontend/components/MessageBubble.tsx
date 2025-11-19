type Props = {
  role: 'user' | 'assistant'
  content: string
  confidence?: string
  sources?: string[]
  sentiment?: string
}

export default function MessageBubble({ role, content, confidence, sources, sentiment }: Props) {
  const isUser = role === 'user'
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={`max-w-3xl px-4 py-3 rounded-lg ${isUser ? 'bg-blue-600 text-white' : 'bg-white border border-gray-200'}`}>
        <p className="text-sm whitespace-pre-wrap">{content}</p>
        {!isUser && (
          <div className="mt-2 space-y-1 text-xs text-gray-600">
            {confidence && (
              <div>
                <span className="text-gray-500">Confidence: </span>
                <span>{confidence}</span>
              </div>
            )}
            {sentiment && (
              <div>
                <span className="text-gray-500">Sentiment: </span>
                <span>{sentiment}</span>
              </div>
            )}
            {sources && sources.length > 0 && (
              <div>
                <span className="text-gray-500">Sources: </span>
                <span>{sources.join(', ')}</span>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}


