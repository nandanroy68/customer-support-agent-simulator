export default function Loader() {
  return (
    <div className="flex items-center space-x-2 text-gray-500 text-sm">
      <div className="h-3 w-3 rounded-full bg-gray-400 animate-pulse" />
      <div className="h-3 w-3 rounded-full bg-gray-400 animate-pulse [animation-delay:150ms]" />
      <div className="h-3 w-3 rounded-full bg-gray-400 animate-pulse [animation-delay:300ms]" />
      <span>Thinking...</span>
    </div>
  )
}


