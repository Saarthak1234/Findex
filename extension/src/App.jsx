import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ChatSidebar from './components/ChatSidebar'
import SidebarController from './components/YouTubeQAApp'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <SidebarController />
      </div>
    </>
  )
}

export default App
